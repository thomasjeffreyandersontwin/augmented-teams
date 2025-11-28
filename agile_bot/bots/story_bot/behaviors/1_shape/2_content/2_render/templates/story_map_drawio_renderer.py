"""
DrawIO Story Map Renderer

Renders story graph JSON to DrawIO XML format.
Based on DrawIOStoryShapeBuilder from agents/story_bot/src/story_agent.py
"""

from pathlib import Path
from typing import Dict, Any, Optional
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys


class DrawIOStoryShapeRenderer:
    STORY_WIDTH = 50
    STORY_HEIGHT = 50
    STORY_SPACING_X = 60
    STORY_SPACING_Y = 55
    FEATURE_HEIGHT = 60
    FEATURE_SPACING_X = 10
    EPIC_Y = 130
    FEATURE_Y = 200
    STORY_START_Y = 350  # Increased to make room for users above stories
    USER_LABEL_OFFSET = 60  # Distance above element (accounts for 50px label height)
    USER_LABEL_X_OFFSET = 5  # Offset to the right from element x position
    
    def render(self, story_graph_path: Path, output_path: Optional[Path] = None) -> Dict[str, Any]:
        """
        Render story graph JSON to DrawIO XML.
        
        Args:
            story_graph_path: Path to story_graph.json file
            output_path: Optional output path for DrawIO file. If None, uses story_graph_path parent / story-map.drawio
        
        Returns:
            Dictionary with output_path and summary
        """
        # Load story graph
        with open(story_graph_path, 'r', encoding='utf-8') as f:
            story_graph = json.load(f)
        
        # Load layout JSON if it exists (for outline mode)
        layout_data = {}
        layout_path = story_graph_path.parent / f"{story_graph_path.stem}-layout.json"
        if layout_path.exists():
            with open(layout_path, 'r', encoding='utf-8') as f:
                layout_data = json.load(f)
        
        # Determine output path
        if output_path is None:
            output_path = story_graph_path.parent / "story-map.drawio"
        else:
            output_path = Path(output_path)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Generate diagram
        xml_output = self._generate_diagram(story_graph, layout_data)
        
        # Write output
        output_path.write_text(xml_output, encoding='utf-8')
        
        return {
            "output_path": str(output_path),
            "summary": {
                "epics": len(story_graph.get("epics", [])),
                "diagram_generated": True
            }
        }
    
    def _generate_diagram(self, story_graph: Dict[str, Any], layout_data: Dict[str, Dict[str, float]] = None) -> str:
        """
        Generate DrawIO XML from story graph.
        
        Args:
            story_graph: Story graph JSON data
            layout_data: Optional layout data with story coordinates (key: "epic_name|feature_name|story_name")
        """
        if layout_data is None:
            layout_data = {}
        root = ET.Element('mxfile', host='65bd71144e')
        diagram = ET.SubElement(root, 'diagram', id='story-map', name='Story Map')
        graph_model = ET.SubElement(diagram, 'mxGraphModel', 
                                    dx='2656', dy='1035', grid='1', gridSize='10', 
                                    guides='1', tooltips='1', connect='1', arrows='1', 
                                    fold='1', page='1', pageScale='1', 
                                    pageWidth='4000', pageHeight='3000', math='0', shadow='0')
        root_elem = ET.SubElement(graph_model, 'root')
        ET.SubElement(root_elem, 'mxCell', id='0')
        ET.SubElement(root_elem, 'mxCell', id='1', parent='0')
        
        epic_group = ET.SubElement(root_elem, 'mxCell', id='epic-group', value='', 
                     style='group', parent='1', vertex='1', connectable='0')
        epic_group_geom = ET.SubElement(epic_group, 'mxGeometry', x='0', y='0', width='1', height='1')
        epic_group_geom.set('as', 'geometry')
        
        x_pos = 20
        shown_users = set()  # Track which users have been shown
        
        for epic_idx, epic in enumerate(story_graph.get('epics', []), 1):
            features = epic.get('features', [])
            
            feature_x = x_pos + 10
            epic_width = 0
            
            feature_positions = []
            for feature in features:
                stories = feature.get('stories', [])
                
                # Group stories by sequential_order and create a mapping to position index
                stories_by_seq = {}
                seq_orders = []
                for story in stories:
                    seq_order = story.get('sequential_order', 1)
                    if seq_order not in stories_by_seq:
                        stories_by_seq[seq_order] = []
                    stories_by_seq[seq_order].append(story)
                    if seq_order not in seq_orders:
                        seq_orders.append(seq_order)
                
                # Sort sequential orders and create position mapping
                sorted_seq_orders = sorted(seq_orders)
                seq_to_position = {seq: idx for idx, seq in enumerate(sorted_seq_orders)}
                max_position = len(sorted_seq_orders) - 1 if sorted_seq_orders else 0
                feature_width = (max_position + 1) * self.STORY_SPACING_X + 20
                
                feature_positions.append({
                    'feature': feature,
                    'x': feature_x,
                    'width': feature_width,
                    'stories_by_seq': stories_by_seq,
                    'seq_to_position': seq_to_position
                })
                
                feature_x += feature_width + self.FEATURE_SPACING_X
                epic_width += feature_width + self.FEATURE_SPACING_X
            
            epic_width -= self.FEATURE_SPACING_X
            epic_width += 20
            
            # Track actual bounds for shrinking epics/features after layout
            epic_min_x = float('inf')
            epic_max_x = -float('inf')
            feature_geometries = []  # Store feature geometries to update later
            
            # Collect and place epic-level users horizontally (tracking bounds)
            epic_users = epic.get('users', [])
            epic_user_x_offset = 0
            for user in epic_users:
                if user not in shown_users:
                    user_x = x_pos + epic_user_x_offset
                    user_label = ET.SubElement(root_elem, 'mxCell',
                                              id=f'user_epic{epic_idx}_{user}',
                                              value=user,
                                              style='whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#000000;fontSize=8;',
                                              parent='1', vertex='1')
                    user_geom = ET.SubElement(user_label, 'mxGeometry', 
                                             x=str(user_x), 
                                             y=str(self.EPIC_Y - self.USER_LABEL_OFFSET),
                                             width=str(self.STORY_WIDTH), height=str(self.STORY_HEIGHT))
                    user_geom.set('as', 'geometry')
                    
                    # Track epic-level user bounds
                    epic_min_x = min(epic_min_x, user_x)
                    epic_max_x = max(epic_max_x, user_x + self.STORY_WIDTH)
                    
                    shown_users.add(user)
                    epic_user_x_offset += self.STORY_SPACING_X
            
            epic_cell = ET.SubElement(root_elem, 'mxCell', id=f'epic{epic_idx}', 
                                     value=epic['name'],
                                     style='rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontColor=#000000;',
                                     parent='epic-group', vertex='1')
            epic_geom = ET.SubElement(epic_cell, 'mxGeometry', x=str(x_pos), y=str(self.EPIC_Y), width=str(epic_width), 
                         height='60')
            epic_geom.set('as', 'geometry')
            
            for feat_idx, feat_data in enumerate(feature_positions, 1):
                feature = feat_data['feature']
                feat_x = feat_data['x']
                feat_width = feat_data['width']
                stories_by_seq = feat_data['stories_by_seq']
                seq_to_position = feat_data['seq_to_position']
                
                # Initialize feature bounds tracking
                feature_min_x = float('inf')
                feature_max_x = -float('inf')
                
                # Collect all users for this feature (epic/feature/story level)
                all_feature_users = []
                feature_users = feature.get('users', [])
                for user in feature_users:
                    if user not in shown_users:
                        all_feature_users.append(user)
                        shown_users.add(user)
                
                # Place feature-level users horizontally
                user_x_offset = 0
                for user in all_feature_users:
                    user_x = feat_x + user_x_offset
                    user_label = ET.SubElement(root_elem, 'mxCell',
                                              id=f'user_e{epic_idx}f{feat_idx}_{user}',
                                              value=user,
                                              style='whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#000000;fontSize=8;',
                                              parent='1', vertex='1')
                    user_geom = ET.SubElement(user_label, 'mxGeometry', 
                                             x=str(user_x), 
                                             y=str(self.FEATURE_Y - self.USER_LABEL_OFFSET),
                                             width=str(self.STORY_WIDTH), height=str(self.STORY_HEIGHT))
                    user_geom.set('as', 'geometry')
                    
                    # Track feature-level user bounds for feature shrinking
                    feature_min_x = min(feature_min_x, user_x)
                    feature_max_x = max(feature_max_x, user_x + self.STORY_WIDTH)
                    
                    user_x_offset += self.STORY_SPACING_X
                
                # If story_count exists, always show estimate (even if some stories are enumerated - partial enumeration)
                # If no story_count but stories are enumerated, don't show count (all stories are known)
                # If no story_count and no stories, show nothing
                if 'story_count' in feature and feature['story_count']:
                    # Estimated stories - show the estimate (even if some stories are already enumerated)
                    story_count_text = f"<br><i style=\"border-color: rgb(218, 220, 224); font-size: 8px;\"><span style=\"border-color: rgb(218, 220, 224); text-align: left;\">{feature['story_count']}&nbsp;</span><span style=\"border-color: rgb(218, 220, 224); text-align: left;\">stories</span></i>"
                elif feature.get('stories') and len(feature.get('stories', [])) > 0:
                    # Stories are fully enumerated (no story_count) - don't show count in feature label
                    story_count_text = ""
                else:
                    # No stories and no estimate - show nothing
                    story_count_text = ""
                feature_cell = ET.SubElement(root_elem, 'mxCell', 
                                             id=f'e{epic_idx}f{feat_idx}',
                                             value=f"{feature['name']}{story_count_text}",
                                             style='rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontColor=#000000;',
                                             parent='1', vertex='1')
                feature_geom = ET.SubElement(feature_cell, 'mxGeometry', x=str(feat_x), y=str(self.FEATURE_Y),
                             width=str(feat_width), height=str(self.FEATURE_HEIGHT))
                feature_geom.set('as', 'geometry')
                
                # Store feature geometry for later shrinking
                feature_geometries.append({
                    'geom': feature_geom,
                    'x': feat_x
                })
                
                story_idx = 1
                story_user_x_offset = {}  # Track user X position per story row
                
                # Group stories by base sequential_order (integer part) to handle nested stories
                base_story_positions = {}  # Maps base seq_order to its Y position
                nested_story_groups = {}  # Maps base seq_order to list of nested stories (decimal sequential_order)
                
                # First pass: identify base stories and group nested stories (decimal sequential_order)
                for seq_order in sorted(stories_by_seq.keys()):
                    seq_float = float(seq_order) if isinstance(seq_order, (int, float, str)) else float(seq_order)
                    base_seq = int(seq_float)
                    is_decimal = (seq_float != base_seq)  # Check if sequential_order has decimal part
                    
                    stories_in_seq = stories_by_seq[seq_order]
                    
                    for story in stories_in_seq:
                        if is_decimal:
                            # Story with decimal sequential_order (e.g., 1.1, 2.1) - treat as nested
                            if base_seq not in nested_story_groups:
                                nested_story_groups[base_seq] = []
                            nested_story_groups[base_seq].append((seq_order, story))
                        else:
                            # Base story (integer sequential_order) - store its position and users
                            if base_seq not in base_story_positions:
                                # Check if layout data exists for this story
                                layout_key = f"{epic['name']}|{feature['name']}|{story['name']}"
                                if layout_key in layout_data:
                                    # Use layout coordinates
                                    base_story_positions[base_seq] = {
                                        'x': layout_data[layout_key]['x'],
                                        'y': layout_data[layout_key]['y'],
                                        'seq_order': seq_order,
                                        'users': set(story.get('users', []))  # Store base story users for comparison
                                    }
                                else:
                                    # Use calculated position
                                    position = seq_to_position[seq_order]
                                    base_story_positions[base_seq] = {
                                        'x': feat_x + position * self.STORY_SPACING_X + 2,
                                        'y': self.STORY_START_Y,
                                        'seq_order': seq_order,
                                        'users': set(story.get('users', []))  # Store base story users for comparison
                                    }
                
                # Second pass: render base stories first (integer sequential_order only)
                for seq_order in sorted(stories_by_seq.keys()):
                    seq_float = float(seq_order) if isinstance(seq_order, (int, float, str)) else float(seq_order)
                    base_seq = int(seq_float)
                    is_decimal = (seq_float != base_seq)
                    
                    # Skip decimal sequential_order stories in this pass
                    if is_decimal:
                        continue
                    
                    stories_in_seq = sorted(stories_by_seq[seq_order], 
                                           key=lambda s: s.get('vertical_order') or 0)
                    
                    for story in stories_in_seq:
                        # Render base story
                        # Check if layout data exists for this story (may override initial position)
                        layout_key = f"{epic['name']}|{feature['name']}|{story['name']}"
                        if layout_key in layout_data:
                            # Use layout coordinates from DrawIO
                            story_x = layout_data[layout_key]['x']
                            story_y = layout_data[layout_key]['y']
                            # Update base_story_positions for nested stories
                            if base_seq in base_story_positions:
                                base_story_positions[base_seq]['x'] = story_x
                                base_story_positions[base_seq]['y'] = story_y
                        else:
                            # Use calculated position
                            base_pos = base_story_positions[base_seq]
                            story_x = base_pos['x']
                            story_y = base_pos['y']
                        
                        # Collect users for this story (if not already shown)
                        story_users = story.get('users', [])
                        new_story_users = []
                        for user in story_users:
                            if user not in shown_users:
                                new_story_users.append(user)
                                shown_users.add(user)
                        
                        # Place story-level users horizontally above the story
                        if new_story_users:
                            if story_y not in story_user_x_offset:
                                story_user_x_offset[story_y] = 0
                            for user in new_story_users:
                                user_x = story_x + story_user_x_offset[story_y]
                                user_label = ET.SubElement(root_elem, 'mxCell',
                                                          id=f'user_e{epic_idx}f{feat_idx}s{story_idx}_{user}',
                                                          value=user,
                                                          style='whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#000000;fontSize=8;',
                                                          parent='1', vertex='1')
                                user_geom = ET.SubElement(user_label, 'mxGeometry', 
                                                         x=str(user_x), 
                                                         y=str(story_y - self.USER_LABEL_OFFSET),
                                                         width=str(self.STORY_WIDTH), height=str(self.STORY_HEIGHT))
                                user_geom.set('as', 'geometry')
                                
                                # Track user bounds for feature shrinking
                                feature_min_x = min(feature_min_x, user_x)
                                feature_max_x = max(feature_max_x, user_x + self.STORY_WIDTH)
                                
                                story_user_x_offset[story_y] += self.STORY_SPACING_X
                        
                        story_cell = ET.SubElement(root_elem, 'mxCell',
                                                   id=f'e{epic_idx}f{feat_idx}s{story_idx}',
                                                   value=story['name'],
                                                   style='whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#000000;fontSize=8;',
                                                   parent='1', vertex='1')
                        story_geom = ET.SubElement(story_cell, 'mxGeometry', x=str(story_x), y=str(story_y),
                                     width=str(self.STORY_WIDTH), height=str(self.STORY_HEIGHT))
                        story_geom.set('as', 'geometry')
                        
                        # Track story bounds for feature shrinking
                        feature_min_x = min(feature_min_x, story_x)
                        feature_max_x = max(feature_max_x, story_x + self.STORY_WIDTH)
                        
                        story_idx += 1
                
                # Third pass: render nested stories (decimal sequential_order)
                # All nested stories are positioned vertically below base story
                # Stories with different users get extra spacing to make room for user cards above
                for base_seq in sorted(nested_story_groups.keys()):
                    if base_seq not in base_story_positions:
                        continue  # Skip if base story doesn't exist
                    
                    base_pos = base_story_positions[base_seq]
                    base_x = base_pos['x']
                    base_y = base_pos['y']
                    base_users = base_pos['users']
                    
                    # Sort nested stories by their sequential_order
                    nested_stories = sorted(nested_story_groups[base_seq], 
                                           key=lambda x: (float(x[0]), x[1].get('vertical_order', 0)))
                    
                    # Track vertical position, adding extra space for stories with different users
                    cumulative_vertical_offset = 0
                    
                    for nest_idx, (seq_order, story) in enumerate(nested_stories, 1):
                        # Check if layout data exists for this nested story
                        layout_key = f"{epic['name']}|{feature['name']}|{story['name']}"
                        if layout_key in layout_data:
                            # Use layout coordinates from DrawIO
                            story_x = layout_data[layout_key]['x']
                            story_y = layout_data[layout_key]['y']
                        else:
                            # Use calculated position
                            story_users = set(story.get('users', []))
                            has_different_users = (story_users != base_users)
                            
                            # If different users, add extra spacing for user cards above this story
                            if has_different_users:
                                cumulative_vertical_offset += self.USER_LABEL_OFFSET  # Extra space for user cards
                            
                            story_x = base_x  # Same X as base story
                            story_y = base_y + cumulative_vertical_offset + nest_idx * self.STORY_SPACING_Y  # Below base story
                        
                        # Collect users for this story (if not already shown)
                        story_users_list = story.get('users', [])
                        new_story_users = []
                        for user in story_users_list:
                            if user not in shown_users:
                                new_story_users.append(user)
                                shown_users.add(user)
                        
                        # Place story-level users horizontally above the story
                        if new_story_users:
                            if story_y not in story_user_x_offset:
                                story_user_x_offset[story_y] = 0
                            for user in new_story_users:
                                user_x = story_x + story_user_x_offset[story_y]
                                user_label = ET.SubElement(root_elem, 'mxCell',
                                                          id=f'user_e{epic_idx}f{feat_idx}s{story_idx}_{user}',
                                                          value=user,
                                                          style='whiteSpace=wrap;html=1;aspect=fixed;fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#000000;fontSize=8;',
                                                          parent='1', vertex='1')
                                user_geom = ET.SubElement(user_label, 'mxGeometry', 
                                                         x=str(user_x), 
                                                         y=str(story_y - self.USER_LABEL_OFFSET),
                                                         width=str(self.STORY_WIDTH), height=str(self.STORY_HEIGHT))
                                user_geom.set('as', 'geometry')
                                
                                # Track user bounds for feature shrinking
                                feature_min_x = min(feature_min_x, user_x)
                                feature_max_x = max(feature_max_x, user_x + self.STORY_WIDTH)
                                
                                story_user_x_offset[story_y] += self.STORY_SPACING_X
                        
                        story_cell = ET.SubElement(root_elem, 'mxCell',
                                                   id=f'e{epic_idx}f{feat_idx}s{story_idx}',
                                                   value=story['name'],
                                                   style='whiteSpace=wrap;html=1;aspect=fixed;fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#000000;fontSize=8;',
                                                   parent='1', vertex='1')
                        story_geom = ET.SubElement(story_cell, 'mxGeometry', x=str(story_x), y=str(story_y),
                                     width=str(self.STORY_WIDTH), height=str(self.STORY_HEIGHT))
                        story_geom.set('as', 'geometry')
                        
                        # Track nested story bounds for feature shrinking
                        feature_min_x = min(feature_min_x, story_x)
                        feature_max_x = max(feature_max_x, story_x + self.STORY_WIDTH)
                        
                        story_idx += 1
                
                # Shrink feature to fit actual story bounds (with padding)
                if feature_min_x != float('inf') and feature_max_x != -float('inf'):
                    actual_feature_width = feature_max_x - feature_min_x + 20  # Add padding
                    actual_feature_x = feature_min_x - 10  # Adjust X to align with stories
                    feature_geometries[-1]['geom'].set('width', str(actual_feature_width))
                    feature_geometries[-1]['geom'].set('x', str(actual_feature_x))
                    
                    # Track feature bounds for epic shrinking (use actual shrunk position)
                    epic_min_x = min(epic_min_x, actual_feature_x)
                    epic_max_x = max(epic_max_x, actual_feature_x + actual_feature_width)
                else:
                    # No stories, use original width
                    epic_min_x = min(epic_min_x, feat_x)
                    epic_max_x = max(epic_max_x, feat_x + feat_width)
            
            # Shrink epic to fit actual feature bounds (with padding)
            if epic_min_x != float('inf') and epic_max_x != -float('inf'):
                actual_epic_width = epic_max_x - epic_min_x + 20  # Add padding
                actual_epic_x = epic_min_x - 10  # Adjust X to align with features
                epic_geom.set('width', str(actual_epic_width))
                epic_geom.set('x', str(actual_epic_x))
                
                # Update x_pos for next epic using actual epic width
                x_pos = actual_epic_x + actual_epic_width + 20
            else:
                # Fallback to original calculation
                x_pos += epic_width + 20
        
        rough_string = ET.tostring(root, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent='    ')


def render_story_map_drawio(
    story_graph_path: str,
    output_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Render story graph JSON to DrawIO XML.
    
    Args:
        story_graph_path: Path to story_graph.json file
        output_path: Optional output path for DrawIO file
    
    Returns:
        Dictionary with output_path and summary
    """
    renderer = DrawIOStoryShapeRenderer()
    return renderer.render(Path(story_graph_path), Path(output_path) if output_path else None)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: story_map_drawio_renderer.py <config.json> [project_path]")
        print("   OR: story_map_drawio_renderer.py <story_graph.json> [output.drawio]")
        sys.exit(1)
    
    first_arg = Path(sys.argv[1])
    
    # Check if first argument is a config JSON (render system interface)
    if first_arg.suffix == '.json' and first_arg.name.startswith('render_'):
        # Render system interface: config.json + project_path
        config_path = first_arg
        project_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        
        # Load config
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Find story_graph.json in project
        story_graph_path = project_path / "docs" / "stories" / "story_graph.json"
        if not story_graph_path.exists():
            print(f"Error: story_graph.json not found at {story_graph_path}")
            sys.exit(1)
        
        # Determine output path from config
        output_path = project_path / config.get('path', 'docs/stories') / config.get('output', 'story-map-outline.drawio')
        
        result = render_story_map_drawio(str(story_graph_path), str(output_path))
        print(f"Generated DrawIO diagram: {result['output_path']}")
        print(f"Epics: {result['summary']['epics']}")
    else:
        # Direct interface: story_graph.json + output.drawio
        story_graph_path = first_arg
        output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
        
        result = render_story_map_drawio(str(story_graph_path), str(output_path) if output_path else None)
        print(f"Generated DrawIO diagram: {result['output_path']}")
        print(f"Epics: {result['summary']['epics']}")

