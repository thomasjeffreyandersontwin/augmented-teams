"""
BDD Domain Object Helper Factories
BDD-specific helper functions for creating domain objects in tests
"""

# Import common helpers
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from common_command_runner.common_command_runner import (
    Content,
    FrameworkSpecializingRule,
    SpecializedRule,
    Workflow,
    PhaseCommand,
    PhaseState,
    IncrementalState,
    CodeGuidingCommand
)

def create_content(file_path='test.py', file_extension='.py'):
    return Content(file_path=file_path, file_extension=file_extension)

def create_specializing_rule(specialized_rules=None):
    if specialized_rules is None:
        specialized_rules = {}
    return FrameworkSpecializingRule(specialized_rules=specialized_rules)

def create_specialized_rule():
    return SpecializedRule(parent=None)

def create_workflow():
    return Workflow()

def create_phase_command(content, workflow, phase_number=0, phase_name="Test Phase"):
    return PhaseCommand(content=content, workflow=workflow, phase_number=phase_number, phase_name=phase_name)

def create_phase_state(phase_number=0, phase_status="STARTING"):
    return PhaseState(phase_number=phase_number, phase_status=phase_status)

def create_incremental_state(current_run=1):
    return IncrementalState(current_run=current_run)

def create_code_guiding_command(content, specializing_rule, validation_mode="STRICT"):
    return CodeGuidingCommand(content=content, specializing_rule=specializing_rule, validation_mode=validation_mode)

# ============================================================================
# BDD-SPECIFIC HELPER FACTORIES
# ============================================================================

def create_bdd_command(content, specializing_rule=None):
    """Helper factory for creating real BDDCommand domain object"""
    # BDDCommand not implemented yet - will fail in RED phase
    # from bdd.domain import BDDCommand
    # return BDDCommand(content=content, specializing_rule=specializing_rule)
    # For now, use CodeGuidingCommand as placeholder
    return create_code_guiding_command(content, specializing_rule)

def create_bdd_phase_command(content, workflow, phase_number, phase_name):
    """Helper factory for creating real BDDPhaseCommand domain object"""
    # BDDPhaseCommand not implemented yet - will fail in RED phase
    # from bdd.domain import BDDPhaseCommand
    # return BDDPhaseCommand(content=content, workflow=workflow, phase_number=phase_number, phase_name=phase_name)
    # For now, use PhaseCommand as placeholder
    return create_phase_command(content, workflow, phase_number, phase_name)







