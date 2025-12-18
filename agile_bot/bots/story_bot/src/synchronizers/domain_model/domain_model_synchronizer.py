"""
Domain Model Synchronizers

Handles rendering of domain model documents from story graph JSON.
Three separate synchronizers, one per output type.
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, Union


def _load_domain_concepts(input_path: Path) -> Dict[str, Dict]:
    """Load and deduplicate domain concepts from story graph, tracking namespace (sub-epic)."""
    with open(input_path, 'r', encoding='utf-8') as f:
        story_graph = json.load(f)
    
    domain_concepts = {}
    for epic in story_graph.get('epics', []):
        epic_name = epic.get('name', '')
        # Concepts at epic level - assign to epic name as namespace (or first sub-epic if exists)
        epic_namespace = None
        sub_epics = epic.get('sub_epics', [])
        if sub_epics:
            # Use first sub-epic as namespace for epic-level concepts
            epic_namespace = sub_epics[0].get('name', epic_name)
        else:
            # No sub-epics, use epic name as namespace
            epic_namespace = epic_name
        
        for concept in epic.get('domain_concepts', []):
            name = concept['name']
            if name not in domain_concepts:
                concept_with_namespace = concept.copy()
                concept_with_namespace['namespace'] = epic_namespace
                domain_concepts[name] = concept_with_namespace
        
        # Concepts at sub-epic level - use sub-epic name as namespace
        for sub_epic in sub_epics:
            sub_epic_name = sub_epic.get('name', '')
            for concept in sub_epic.get('domain_concepts', []):
                name = concept['name']
                if name not in domain_concepts:
                    concept_with_namespace = concept.copy()
                    concept_with_namespace['namespace'] = sub_epic_name
                    domain_concepts[name] = concept_with_namespace
    
    return domain_concepts


def _normalize_namespace(namespace: str, class_names: list) -> str:
    """
    Normalize namespace name to avoid conflicts with class names.
    If namespace matches a class name, add underscore prefix.
    
    Args:
        namespace: Original namespace name
        class_names: List of all class names in the domain
    
    Returns:
        Normalized namespace name
    """
    normalized = namespace
    # Check if namespace conflicts with any class name
    if normalized in class_names:
        normalized = f"_{normalized}"
    return normalized




def _get_solution_info(project_path: Path, kwargs: Dict) -> tuple:
    """Extract solution name, slug, and purpose from project or kwargs."""
    solution_name = kwargs.get('solution_name')
    solution_name_slug = kwargs.get('solution_name_slug')
    if not solution_name:
        # Try to extract from project path
        solution_name = project_path.name.replace('_', ' ').replace('-', ' ').title()
    if not solution_name_slug:
        solution_name_slug = solution_name.lower().replace(' ', '-')
    
    # Try to get solution purpose from clarification.json
    solution_purpose = kwargs.get('solution_purpose')
    if not solution_purpose:
        clarification_path = project_path / 'docs' / 'stories' / 'clarification.json'
        if clarification_path.exists():
            try:
                with open(clarification_path, 'r', encoding='utf-8') as f:
                    clarification = json.load(f)
                    shape_data = clarification.get('shape', {})
                    key_questions = shape_data.get('key_questions', {})
                    goals = key_questions.get('goals', '')
                    if goals:
                        solution_purpose = goals
            except Exception:
                pass
    
    if not solution_purpose:
        solution_purpose = f"Domain model for {solution_name}"
    
    return solution_name, solution_name_slug, solution_purpose


def _get_source_material(project_path: Path) -> str:
    """Generate source material section."""
    input_file = project_path / 'input.txt'
    if not input_file.exists():
        input_file = project_path / 'docs' / 'context' / 'input.txt'
    
    input_path_str = str(input_file.relative_to(project_path.parent.parent)) if input_file.exists() else 'input.txt'
    
    return f"""**Primary Source:** `{input_path_str}`
**Date Generated:** 2025-01-27
**Context:** Shape phase - Domain model extracted from story-graph.json"""


class DomainModelDescriptionSynchronizer:
    """Synchronizer for rendering domain model description markdown."""
    
    def render(self, input_path: Union[str, Path], output_path: Union[str, Path], 
               renderer_command: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Render domain model description markdown from story graph JSON.
        
        Args:
            input_path: Path to story graph JSON file
            output_path: Path for output file (or directory, will append filename)
            renderer_command: Optional command variant (unused)
            **kwargs: Additional arguments:
                - solution_name: Solution name (default: extracted from path)
                - solution_name_slug: Slug version (default: extracted from path)
                - solution_purpose: Purpose text (default: from clarification.json if available)
                - project_path: Base project path (default: parent of input_path)
        
        Returns:
            Dictionary with output_path and summary
        """
        input_path = Path(input_path)
        project_path = kwargs.get('project_path', input_path.parent.parent.parent)
        project_path = Path(project_path)
        
        solution_name, solution_name_slug, solution_purpose = _get_solution_info(project_path, kwargs)
        domain_concepts = _load_domain_concepts(input_path)
        
        # Generate domain descriptions
        domain_descriptions = []
        for concept_name, concept in sorted(domain_concepts.items()):
            desc_lines = [f"### {concept_name}\n"]
            
            # Build description from responsibilities
            responsibilities = concept.get('responsibilities', [])
            if responsibilities:
                desc_lines.append("**Key Responsibilities:**")
                for resp in responsibilities:
                    resp_name = resp.get('name', '')
                    collaborators = resp.get('collaborators', [])
                    if collaborators:
                        desc_lines.append(f"- **{resp_name}**: This responsibility involves collaboration with {', '.join(collaborators)}.")
                    else:
                        desc_lines.append(f"- **{resp_name}**: {resp_name}")
            
            domain_descriptions.append("\n".join(desc_lines))
        
        domain_model_descriptions_text = "\n\n".join(domain_descriptions)
        source_material = _get_source_material(project_path)
        
        # Determine output path
        output_path = Path(output_path)
        if output_path.is_dir() or not output_path.suffix:
            # If directory or no extension, append filename
            output_path = output_path / f'{solution_name_slug}-domain-model-description.md'
        
        # Template
        content = f"""# Domain Model Description: {solution_name}

**File Name**: `{solution_name_slug}-domain-model-description.md`
**Location**: `{project_path.name}/docs/stories/{solution_name_slug}-domain-model-description.md`

## Solution Purpose
{solution_purpose}

---

## Domain Model Descriptions

{domain_model_descriptions_text}

---

## Source Material

{source_material}
"""
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {
            'output_path': str(output_path),
            'summary': {
                'domain_concepts': len(domain_concepts),
                'file': str(output_path.name)
            }
        }


class DomainModelDiagramSynchronizer:
    """Synchronizer for rendering domain model diagram markdown with Mermaid."""
    
    def render(self, input_path: Union[str, Path], output_path: Union[str, Path], 
               renderer_command: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Render domain model diagram markdown from story graph JSON.
        
        Args:
            input_path: Path to story graph JSON file
            output_path: Path for output file (or directory, will append filename)
            renderer_command: Optional command variant (unused)
            **kwargs: Additional arguments:
                - solution_name: Solution name (default: extracted from path)
                - solution_name_slug: Slug version (default: extracted from path)
                - solution_purpose: Purpose text (default: from clarification.json if available)
                - project_path: Base project path (default: parent of input_path)
        
        Returns:
            Dictionary with output_path and summary
        """
        input_path = Path(input_path)
        project_path = kwargs.get('project_path', input_path.parent.parent.parent)
        project_path = Path(project_path)
        
        solution_name, solution_name_slug, solution_purpose = _get_solution_info(project_path, kwargs)
        domain_concepts = _load_domain_concepts(input_path)
        
        # Group concepts by namespace
        concepts_by_namespace = {}
        for concept_name, concept in domain_concepts.items():
            namespace = concept.get('namespace', 'Default')
            if namespace not in concepts_by_namespace:
                concepts_by_namespace[namespace] = []
            concepts_by_namespace[namespace].append((concept_name, concept))
        
        # Get all class names for namespace normalization
        all_class_names = list(domain_concepts.keys())
        
        # Normalize namespace names
        namespace_mapping = {}  # original_namespace -> normalized_namespace
        
        for namespace in concepts_by_namespace.keys():
            normalized_namespace = _normalize_namespace(namespace, all_class_names)
            namespace_mapping[namespace] = normalized_namespace
        
        # Generate Mermaid diagram grouped by namespace
        mermaid_classes = []
        mermaid_relationships = []
        seen_relationships = set()
        
        # Generate classes grouped by namespace using namespace blocks
        for namespace in sorted(concepts_by_namespace.keys()):
            normalized_namespace = namespace_mapping[namespace]
            concepts_in_namespace = sorted(concepts_by_namespace[namespace], key=lambda x: x[0])
            
            # Start namespace block
            namespace_block = [f"    namespace {normalized_namespace} {{"]
            
            for concept_name, concept in concepts_in_namespace:
                responsibilities = concept.get('responsibilities', [])
                resp_methods = []
                for resp in responsibilities:
                    resp_name = resp.get('name', '').replace(' ', '_').lower()
                    resp_methods.append(f"            +{resp_name}()")
                
                # Class definition with methods - single closing brace
                if resp_methods:
                    class_def = f"        class {concept_name} {{\n" + "\n".join(resp_methods) + "\n        }"
                else:
                    class_def = f"        class {concept_name}"
                namespace_block.append(class_def)
            
            # Close namespace block
            namespace_block.append("    }")
            mermaid_classes.extend(namespace_block)
            mermaid_classes.append("")  # Blank line between namespaces
        
        # Generate relationships using original class names (Mermaid handles namespace resolution)
        for concept_name, concept in domain_concepts.items():
            responsibilities = concept.get('responsibilities', [])
            
            for resp in responsibilities:
                collaborators = resp.get('collaborators', [])
                for collab in collaborators:
                    if collab in domain_concepts:
                        # Use original class names - Mermaid will resolve namespaces automatically
                        rel_key = f"{concept_name}->{collab}"
                        if rel_key not in seen_relationships:
                            seen_relationships.add(rel_key)
                            mermaid_relationships.append(f"    {concept_name} --> {collab} : uses")
        
        # Generate pure Mermaid syntax (no markdown wrapper)
        mermaid_content = "classDiagram\n" + "\n".join(mermaid_classes) + "\n    \n    %% Associations\n" + "\n".join(mermaid_relationships)
        
        # Determine output path - use .mmd extension
        output_path = Path(output_path)
        if output_path.is_dir() or not output_path.suffix:
            # If directory or no extension, append filename with .mmd extension
            output_path = output_path / f'{solution_name_slug}-domain-model-diagram.mmd'
        elif output_path.suffix == '.md':
            # If .md extension, change to .mmd
            output_path = output_path.with_suffix('.mmd')
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(mermaid_content)
        
        return {
            'output_path': str(output_path),
            'summary': {
                'domain_concepts': len(domain_concepts),
                'file': str(output_path.name)
            }
        }


class DomainModelOutlineSynchronizer:
    """Synchronizer for rendering domain outline markdown for src/ directory."""
    
    def render(self, input_path: Union[str, Path], output_path: Union[str, Path], 
               renderer_command: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Render domain outline markdown from story graph JSON.
        
        Args:
            input_path: Path to story graph JSON file
            output_path: Path for output file (or directory, will use domain_outline.md)
            renderer_command: Optional command variant (unused)
            **kwargs: Additional arguments:
                - project_path: Base project path (default: parent of input_path)
        
        Returns:
            Dictionary with output_path and summary
        """
        input_path = Path(input_path)
        project_path = kwargs.get('project_path', input_path.parent.parent.parent)
        project_path = Path(project_path)
        
        domain_concepts = _load_domain_concepts(input_path)
        
        # Generate outline
        outline_lines = []
        for concept_name, concept in sorted(domain_concepts.items()):
            outline_lines.append(concept_name)
            for resp in concept.get('responsibilities', []):
                collaborators = resp.get('collaborators', [])
                collab_str = ",".join(collaborators) if collaborators else ""
                outline_lines.append(f"    {resp.get('name', '')}: {collab_str}")
            outline_lines.append("")
        
        content = "\n".join(outline_lines)
        
        # Determine output path
        output_path = Path(output_path)
        if output_path.is_dir() or not output_path.suffix:
            # If directory or no extension, use domain_outline.md
            output_path = output_path / 'domain_outline.md'
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return {
            'output_path': str(output_path),
            'summary': {
                'domain_concepts': len(domain_concepts),
                'file': str(output_path.name)
            }
        }
