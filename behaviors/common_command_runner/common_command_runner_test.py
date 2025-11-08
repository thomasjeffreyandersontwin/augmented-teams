"""Common Domain Objects Tests - Reusable Domain Model"""
# type: ignore  # noqa: E402, F401
# pylint: disable=all
# mypy: ignore-errors
# pyright: reportUndefinedVariable=false
# pyright: reportMissingImports=false
# pyright: reportGeneralTypeIssues=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportCallIssue=false
# pyright: reportAssignmentType=false
# pyright: reportOperatorIssue=false
# pyright: reportUnboundVariable=false
# pyright: reportUnknownParameterType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownLambdaType=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportMissingParameterType=false
# pyright: reportMissingTypeArgument=false
# pyright: reportOptionalMemberAccess=false
# pyright: reportOptionalOperand=false
# pyright: reportOptionalSubscript=false
# pyright: typeCheckingMode=off
# fmt: off

from mamba import description, context, it, before  # type: ignore
from expects import expect, equal, be_true, be_false, contain, have_length, be_none
from unittest.mock import patch

# Import domain classes
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from common_command_runner.common_command_runner import (
    Content,
    SpecializingRule,
    FrameworkSpecializingRule,
    SpecializedRule,
    Principle,
    Example,
    CodeHeuristic,
    Violation,
    ViolationReport,
    Run,
    RunHistory,
    Command,
    CodeGuidingCommand,
    IncrementalCommand,
    PhaseCommand,
    Workflow,
    PhaseState,
    IncrementalState
)

with description('a piece of content'):
    """Base capability: specializing behavior for different file types"""
    
    with context('that is being processed by a command'):
        with before.each:
            self.content = Content('test.java', '.java')
        
        def create_test_specializing_rule_from_file(base_rule_file_name):
            """Create test specializing rule from base file name - discovers specialized rules internally"""
            class TestSpecializingRule(SpecializingRule):
                def extract_match_key(self, content):
                    if content.file_extension == '.java':
                        return 'servlet'
                    elif content.file_extension == '.pl':
                        return 'cgiscript'
                    return None
            return TestSpecializingRule(base_rule_file_name=base_rule_file_name)
        
        def create_test_specializing_rule_with_both():
            specializing_rule = create_test_specializing_rule_from_file('base-rule.mdc')
            servlet_rule = specializing_rule.specialized_rules.get('servlet')
            cgiscript_rule = specializing_rule.specialized_rules.get('cgiscript')
            return specializing_rule, servlet_rule, cgiscript_rule
        
        def create_test_specializing_rule_with_servlet():
            specializing_rule = create_test_specializing_rule_from_file('base-rule.mdc')
            servlet_rule = specializing_rule.specialized_rules.get('servlet')
            return specializing_rule, servlet_rule
        
        with context('that implements a specializing rule'):
            with before.each:
                self.specializing_rule, self.servlet_specialized, self.cgiscript_specialized = create_test_specializing_rule_with_both()

            with it('should use template method pattern to select specialized rule'):
                # Arrange
                command = Command(self.content, self.specializing_rule)
                
                # Act
                selected_specialized = command.specialized_rule
                
                # Assert
                expect(selected_specialized).to(equal(self.servlet_specialized))
                expect(self.content.file_extension).to(equal('.java'))
            
            with it('should include base rule principles'):
                # Arrange - stub file reading to return test content for base rule
                test_base_rule_content = """---
description: Test rule
---

## 1. First Principle
Test content for first principle.

## 2. Second Principle  
Test content for second principle.
"""
                with patch.object(SpecializingRule, '_read_file_content', return_value=test_base_rule_content):
                    specializing_rule, specialized_rule = create_test_specializing_rule_with_servlet()
                    command = Command(self.content, specializing_rule)
                    
                    # Act
                    selected_specialized = command.specialized_rule
                    principles = selected_specialized.principles if selected_specialized else []
                    
                    # Assert - principles should be SpecializedPrinciple wrappers
                    expect(principles).to(have_length(2))
                    expect(principles[0].principle_number).to(equal(1))
                    expect(principles[0].principle_name).to(equal("First Principle"))
                    expect(principles[0].content).to(equal("Test content for first principle."))
                    expect(principles[1].principle_number).to(equal(2))
                    expect(principles[1].principle_name).to(equal("Second Principle"))
                    expect(principles[1].content).to(equal("Test content for second principle."))
            
            with context('and the specializing rules has been loaded'):
                with before.each:
                    # self.content inherited from parent context
                    test_base_rule_content = """---
description: Test rule
---

## 1. Test Principle
Test content for test principle.
"""
                    with patch.object(SpecializingRule, '_read_file_content', return_value=test_base_rule_content):
                        self.specializing_rule = create_test_specializing_rule_from_file('base-rule.mdc')
                        self.servlet_specialized = self.specializing_rule.specialized_rules.get('servlet')
                        self.principle = self.servlet_specialized.principles[0] if self.servlet_specialized and self.servlet_specialized.principles else None
                
                with it('should have access to the base rule and its principles'):
                    # Arrange
                    command = Command(self.content, self.specializing_rule)
                    
                    # Act
                    accessed_specialized = command.specialized_rule
                    principles = accessed_specialized.principles if accessed_specialized else []
                    
                    # Assert
                    expect(principles).to(have_length(1))
                    expect(principles[0].principle_number).to(equal(1))
                    expect(principles[0].principle_name).to(equal("Test Principle"))
                    expect(principles[0].content).to(equal("Test content for test principle."))
                
                with it('should provide access to specialized examples with DOs and DONTs for each principle'):
                    # Arrange - stub specialized rule file with examples
                    test_specialized_rule_content = """---
description: Test specialized rule
---

## 1. Test Principle
Restate principle briefly.

**✅ DO:**
```java
// Good example code
public class TestServlet {
    // DO example
}
```

**❌ DON'T:**
```java
// Bad example code
public class BadServlet {
    // DON'T example
}
```
"""
                    # Stub both base rule and specialized rule file reading
                    test_base_rule_content = """---
description: Test rule
---

## 1. Test Principle
Test content for test principle.
"""
                    with patch.object(SpecializingRule, '_read_file_content', return_value=test_base_rule_content):
                        with patch.object(SpecializedRule, '_read_file_content', return_value=test_specialized_rule_content):
                            specializing_rule = create_test_specializing_rule_from_file('base-rule.mdc')
                            command = Command(self.content, specializing_rule)
                            
                            # Act
                            accessed_specialized = command.specialized_rule
                            accessed_principles = accessed_specialized.principles if accessed_specialized else []
                            examples = []
                            for principle in accessed_principles:
                                examples.extend(principle.examples)
                            
                            # Assert
                            expect(examples).to(have_length(2))
                            expect(examples[0].example_type).to(equal("DO"))
                            expect(examples[0].content).to(contain("Good example code"))
                            expect(examples[1].example_type).to(equal("DONT"))
                            expect(examples[1].content).to(contain("Bad example code"))
            
            
            with context('that performs code augmented AI guidance'):
                with context('that is being validated against its rules'):
                    with before.each:
                        # self.content inherited from parent context
                        self.specializing_rule = create_test_specializing_rule_from_file('base-rule.mdc')
                        self.servlet_specialized = self.specializing_rule.specialized_rules.get('servlet')
                        self.principle = self.servlet_specialized.principles[0] if self.servlet_specialized and self.servlet_specialized.principles else Principle(1, "Test")
                        self.heuristic = self.principle.heuristics[0] if self.principle.heuristics else CodeHeuristic("test_pattern")
                    
                    with it('should load code heuristics for each principle from associated specializing rule'):
                        # Arrange
                        command = CodeGuidingCommand(self.content, self.specializing_rule)
                        
                        # Act
                        accessed_specialized = command.specialized_rule
                        accessed_principles = accessed_specialized.principles if accessed_specialized else []
                        heuristics = []
                        for principle in accessed_principles:
                            heuristics.extend(principle.heuristics)
                        
                        # Assert
                        expect(heuristics).to(contain(self.heuristic))
                    
                    with it('should analyze content for violations using the heuristic'):
                        # Arrange
                        command = CodeGuidingCommand(self.content, self.specializing_rule)
                        
                        # Act
                        violations = self.heuristic.violations
                        
                        # Assert
                        expect(violations).to(have_length(0))
                        expect(self.content.file_extension).to(equal('.java'))
                    
                    with it('should assemble related violations, principles, and examples into a checklist based report'):
                        # Arrange
                        violation = Violation(10, "Test violation")
                        command = CodeGuidingCommand(self.content, self.specializing_rule)
                        
                        # Act
                        violation_report = ViolationReport([violation], [self.principle], 'CHECKLIST')
                        
                        # Assert
                        expect(violation_report.report_format).to(equal('CHECKLIST'))
                        expect(violation.line_number).to(equal(10))
                    
                    with it('should create violation report with principles'):
                        # Arrange
                        violation_report = ViolationReport([], [self.principle], 'CHECKLIST')
                        command = CodeGuidingCommand(self.content, self.specializing_rule)
                        
                        # Act & Assert
                        expect(violation_report.principles).to(contain(self.principle))
                        expect(violation_report.violations).to(have_length(0))
                        expect(violation_report.report_format).to(equal('CHECKLIST'))
                    
                    with it('should apply fix suggestions from AI'):
                        # Arrange
                        command = CodeGuidingCommand(self.content, self.specializing_rule)
                        
                        # Act
                        self.content.apply_fixes()
                        
                        # Assert
                        expect(self.content.violations).to(have_length(0))
                        expect(command).not_to(be_none)
                        expect(command.content).to(equal(self.content))
                        expect(command.validation_mode).to(equal("STRICT"))
                        expect(self.content.file_extension).to(equal('.java'))
        
        with context('that implements incremental runs'):
            with before.each:
                # self.content inherited from parent context
                self.max_sample_size = 18
                specializing_rule, _ = create_test_specializing_rule_with_servlet()
                self.command = IncrementalCommand(self.content, specializing_rule, self.max_sample_size)
            
            with it('should provide the sample size based on code analysis and configured maximum'):
                # Arrange
                command = self.command
                
                # Act
                sample_size = command.sample_size
                max_sample_size = command.max_sample_size
                
                # Assert
                expect(max_sample_size).to(equal(18))
                expect(sample_size).to(be_none)
            
            with it('should confirm sample size'):
                # Arrange
                command = self.command
                
                # Act
                confirmed = command.sample_size_confirmed
                
                # Assert
                expect(confirmed).to(be_true)
                expect(command.max_sample_size).to(equal(self.max_sample_size))
                expect(command.content).to(equal(self.content))
            
            with it('should submit sample size instructions'):
                # Arrange
                command = self.command
                
                # Act
                command.submit_sample_size_instructions()
                
                # Assert
                expect(command.max_sample_size).to(equal(self.max_sample_size))
                expect(command.content).to(equal(self.content))
            
            with context('that has completed a run'):
                with before.each:
                    self.run = Run(1, "IN_PROGRESS")
                    self.run_history = RunHistory()
                
                with it('should mark run complete'):
                    # Arrange
                    command = self.command
                    command.current_run = self.run
                    
                    # Act
                    self.run.status = 'COMPLETE'
                    
                    # Assert
                    expect(self.run.status).to(equal('COMPLETE'))
                    expect(self.run.run_number).to(equal(1))
                
                with it('should save run to history'):
                    # Arrange
                    command = self.command
                    command.run_history = self.run_history
                    self.run.status = "COMPLETE"
                    
                    # Act
                    self.run_history.runs.append(self.run)
                    
                    # Assert
                    expect(self.run_history.runs).to(contain(self.run))
                    expect(self.run_history.runs).to(have_length(1))
                
                with it('should save state to disk'):
                    # Arrange
                    command = self.command
                    
                    # Act
                    command.state.persist_to_disk()
                    
                    # Assert
                    expect(command.state.persisted_at).not_to(be_none)
                    expect(command).not_to(be_none)
                    expect(command.content).to(equal(self.content))
                    expect(command.run_history).not_to(be_none)
                    expect(self.content.file_path).to(equal('test.java'))
                
                with it('should provide the user with the option to repeat the run, start next run, abandon run, or expand to do all remaining'):
                    # Arrange
                    command = self.command
                    command.current_run = self.run
                    
                    # Act
                    options = command.get_user_options()
                    
                    # Assert
                    expect(options).to(contain('repeat'))
                    expect(options).to(contain('next'))
                    expect(options).to(contain('abandon'))
                    expect(options).to(contain('expand'))
                    expect(command).not_to(be_none)
                    expect(command.current_run).to(equal(self.run))
                    expect(command.run_history).not_to(be_none)
                    expect(self.run.status).to(equal('IN_PROGRESS'))
                
                with context('that has been repeated'):
                    with it('should revert current run results'):
                        # Arrange
                        command = self.command
                        command.current_run = self.run
                        self.run.snapshot_before_run = "snapshot_data"
                        
                        # Act
                        self.run.status = 'REVERTED'
                        
                        # Assert
                        expect(self.run.status).to(equal('REVERTED'))
                        expect(self.run.run_number).to(equal(1))
                    
                    with it('should restart same run from beginning'):
                        # Arrange
                        command = self.command
                        self.run.status = "REVERTED"
                        
                        # Act
                        self.run.status = 'IN_PROGRESS'
                        self.run.completed_at = None
                        
                        # Assert
                        expect(self.run.status).to(equal('IN_PROGRESS'))
                        expect(self.run.completed_at).to(be_none)
                        expect(self.run.run_number).to(equal(1))
            
            with context('that is proceeding to the next run'):
                with before.each:
                    self.current_run = Run(1, "COMPLETE")
                
                with it('should proceed to next run with same sample size'):
                    # Arrange
                    command = self.command
                    command.current_run = self.current_run
                    command.sample_size = 6
                    
                    # Act
                    command.proceed_to_next_run()
                    
                    # Assert
                    expect(command.current_run_number).to(equal(2))
                    expect(command.current_run.sample_size).to(equal(6))
                    expect(command).not_to(be_none)
                    expect(command.sample_size).to(equal(6))
                    expect(command.current_run).not_to(equal(self.current_run))  # Should be a new run object
                    expect(command.current_run.run_number).to(equal(2))  # New run should have incremented number
                    expect(command.max_sample_size).to(equal(self.max_sample_size))
                    expect(self.current_run.run_number).to(equal(1))  # Original run unchanged
            
            with context('that is proceeding to expand to all work'):
                with before.each:
                    self.run_history = RunHistory()
                
                with it('should extract lessons from previous runs'):
                    # Arrange
                    previous_run = Run(1, "COMPLETE")
                    self.run_history.runs = [previous_run]
                    command = self.command
                    command.run_history = self.run_history
                    
                    # Act
                    lessons = command.run_history.extract_lessons()
                    
                    # Assert
                    expect(lessons).to(have_length(0))
                    expect(command).not_to(be_none)
                    expect(command.run_history).to(equal(self.run_history))
                    expect(self.run_history.runs).to(contain(previous_run))
                    expect(previous_run.status).to(equal("COMPLETE"))
                    expect(previous_run.run_number).to(equal(1))
                
                with it('should execute all remaining work'):
                    # Arrange
                    command = self.command
                    
                    # Act
                    command.expand_to_all_work()
                    
                    # Assert
                    expect(command.sample_size).to(equal(90))
                    expect(command.completed_work_units).to(equal(100))
                    expect(command).not_to(be_none)
                    expect(command.max_sample_size).to(equal(self.max_sample_size))
                    expect(command.content).to(equal(self.content))
                    expect(self.max_sample_size).to(equal(18))
            
            with context('with more work remaining'):
                with it('should enable next run option'):
                    # Arrange
                    command = self.command
                    
                    # Act
                    has_more = command.has_more_work_remaining()
                    
                    # Assert
                    expect(has_more).to(be_true)
                    expect(command).not_to(be_none)
                    expect(command.max_sample_size).to(equal(self.max_sample_size))
                    expect(command.content).to(equal(self.content))
                    expect(self.max_sample_size).to(equal(18))
            
            with context('with all work complete'):
                with before.each:
                    # self.content inherited from parent context
                    self.max_sample_size = 18
                    specializing_rule, _ = create_test_specializing_rule_with_servlet()
                    self.command = IncrementalCommand(self.content, specializing_rule, self.max_sample_size)
                
                with it('should mark the command as complete'):
                    # Arrange
                    command = self.command
                    command._has_more_work = False
                    
                    # Act
                    is_complete = command.is_complete()
                    
                    # Assert
                    expect(is_complete).to(be_true)
                    expect(command).not_to(be_none)
                    expect(command.max_sample_size).to(equal(self.max_sample_size))
                    expect(command.content).to(equal(self.content))
                    expect(self.max_sample_size).to(equal(18))
        
        with context('that is a phase in a workflow'):
            with before.each:
                # self.content inherited from parent context
                self.workflow = Workflow()
                self.phase_number = 0
                self.phase_name = "Test Phase"
                self.phase_command = PhaseCommand(self.content, self.workflow, self.phase_number, self.phase_name)
            
            with it('should initialize workflow phase'):
                # Arrange
                phase_command = self.phase_command
                
                # Act
                
                # Assert
                expect(phase_command.phase_state.phase_status).to(equal("STARTING"))
                expect(self.phase_number).to(equal(0))
            
            with it('should set state of phase to starting'):
                # Arrange
                phase_command = self.phase_command
                
                # Act
                phase_command.phase_state.phase_status = "STARTING"
                
                # Assert
                expect(phase_command.phase_state.phase_status).to(equal("STARTING"))
                expect(self.phase_name).to(equal("Test Phase"))
            
            with it('should save state to disk'):
                # Arrange
                phase_command = self.phase_command
                
                # Act
                phase_command.save_state_to_disk()
                
                # Assert
                expect(phase_command.phase_state.persisted_at).not_to(be_none)
                expect(phase_command).not_to(be_none)
                expect(phase_command.phase_state).not_to(be_none)
                expect(phase_command.content).to(equal(self.content))
                expect(phase_command.workflow).to(equal(self.workflow))
                expect(self.content.file_path).to(equal('test.py'))
            
            with context('in the correct phase order'):
                with it('should invoke the command'):
                    # Arrange
                    phase_command = self.phase_command
                    
                    # Act
                    phase_command.start()
                    
                    # Assert
                    expect(self.workflow.can_execute_phase.called).to(be_true)
                    expect(phase_command.phase_state.phase_status).to(equal("IN_PROGRESS"))
                    expect(phase_command).not_to(be_none)
                    expect(phase_command.workflow).to(equal(self.workflow))
                    expect(phase_command.phase_number).to(equal(self.phase_number))
                    expect(phase_command.phase_name).to(equal(self.phase_name))
                    expect(phase_command.phase_state).not_to(be_none)
                    expect(self.phase_number).to(equal(0))
            
            with context('that is being resumed from previous session'):
                with it('should load state from disk'):
                    # Arrange
                    phase_state = PhaseState(self.phase_number, "STARTING")
                    test_file = Path("test_phase_state.json")
                    
                    try:
                        # Act
                        loaded_state = PhaseState.load_from_disk(str(test_file))
                        
                        # Assert
                        expect(loaded_state.phase_status).to(equal("STARTING"))
                        expect(loaded_state.phase_number).to(equal(self.phase_number))
                        expect(phase_state).not_to(be_none)
                    finally:
                        if test_file.exists():
                            test_file.unlink()
                    expect(phase_state.phase_status).to(equal("STARTING"))
                    expect(phase_state.phase_number).to(equal(self.phase_number))
                    expect(self.phase_number).to(equal(0))
                
                with it('should start from current phase'):
                    # Arrange
                    phase_command = self.phase_command
                    phase_state = PhaseState(self.phase_number, "STARTING")
                    phase_command.phase_state = phase_state
                    
                    # Act
                    phase_command.resume_from_phase()
                    
                    # Assert
                    expect(phase_command).not_to(be_none)
                    expect(phase_command.phase_number).to(equal(phase_command.phase_state.phase_number))
                    expect(phase_command.phase_state.phase_status).to(equal("STARTING"))
                    expect(phase_command.content).to(equal(self.content))
                    expect(phase_command.start.called).to(be_true)
                    expect(self.phase_number).to(equal(0))
                
                with it('should start from current run'):
                    # Arrange
                    phase_command = self.phase_command
                    incremental_state = IncrementalState(current_run=5)
                    
                    # Act
                    phase_command.resume_from_run()
                    
                    # Assert
                    expect(phase_command.current_run_number).to(equal(5))
                    expect(phase_command).not_to(be_none)
                    expect(incremental_state).not_to(be_none)
                    expect(incremental_state.current_run).to(equal(5))
                    expect(phase_command.phase_number).to(equal(self.phase_number))
                    expect(self.phase_number).to(equal(0))
            
            with context('that has been invoked out of phase order'):
                with it('should block execution'):
                    # Arrange
                    phase_command = PhaseCommand(self.content, self.workflow, 1, "Wrong Phase")
                    self.workflow.current_phase_number = 0
                    
                    # Act
                    phase_command.block_execution("Phase out of order")
                    phase_command.phase_state.phase_status = "BLOCKED"
                    
                    # Assert
                    expect(phase_command.can_execute).to(be_false)
                    expect(phase_command).not_to(be_none)
                    expect(phase_command.phase_number).to(equal(1))
                    expect(phase_command.phase_name).to(equal("Wrong Phase"))
                    expect(phase_command.phase_state.phase_status).to(equal("BLOCKED"))
                    expect(self.workflow.current_phase_number).to(equal(0))
                    expect(self.phase_number).to(equal(0))
                
                with it('should report on current phase that needs to be completed'):
                    # Arrange
                    self.workflow.current_phase_number = 0
                    self.workflow.phases = [PhaseCommand(self.content, self.workflow, 0, "Test Phase")]
                    
                    # Act
                    status_report = self.workflow.get_current_phase_status()
                    
                    # Assert
                    expect(status_report.phase_name).to(equal("Test Phase"))
                    expect(status_report.phase_number).to(equal(0))
                    expect(self.workflow).not_to(be_none)
                    expect(self.workflow.phases).to(have_length(1))
                    expect(self.workflow.phases[0].phase_name).to(equal("Test Phase"))
                    expect(self.workflow.phases[0].phase_number).to(equal(0))
                    expect(self.workflow.current_phase_number).to(equal(0))
                    expect(self.phase_name).to(equal("Test Phase"))
            
            with context('that has completed all steps for the command'):
                with it('should provide the user with the option to proceed to next phase, verify against rules, or redo the phase'):
                    # Arrange
                    phase_command = self.phase_command
                    
                    # Act
                    options = phase_command.check_completion()
                    
                    # Assert
                    expect(options).to(contain('proceed_to_next_phase'))
                    expect(options).to(contain('verify'))
                    expect(options).to(contain('redo'))
                    expect(phase_command).not_to(be_none)
                    expect(phase_command.phase_name).to(equal(self.phase_name))
                    expect(phase_command.phase_number).to(equal(self.phase_number))
                    expect(phase_command.phase_state).not_to(be_none)
                    expect(self.phase_name).to(equal("Test Phase"))
            
            with context('that has been approved to proceed'):
                with it('should determine next action from state'):
                    # Arrange
                    phase_command = self.phase_command
                    phase_state = PhaseState(self.phase_number, "COMPLETE")
                    phase_command.phase_state = phase_state
                    
                    # Act
                    next_action = phase_command.phase_state.determine_next_action()
                    
                    # Assert
                    expect(next_action).to(equal("PROCEED_TO_NEXT_PHASE"))
                    expect(phase_command).not_to(be_none)
                    expect(phase_command.phase_state).not_to(be_none)
                    expect(phase_command.phase_state.phase_status).to(equal("COMPLETE"))
                    expect(phase_command.phase_state.phase_number).to(equal(self.phase_number))
                    expect(phase_command.content).to(equal(self.content))
                    expect(self.phase_number).to(equal(0))
                
                with it('should mark the phase as complete in the Workflow'):
                    # Arrange
                    phase_command = self.phase_command
                    self.workflow.phases = [phase_command]
                    self.workflow.current_phase_number = 0
                    
                    # Act
                    self.workflow.mark_phase_complete(0)
                    phase_command.phase_state.phase_status = "COMPLETE"
                    self.workflow.current_phase_number = 1
                    
                    # Assert
                    expect(phase_command).not_to(be_none)
                    expect(phase_command.phase_state.phase_status).to(equal("COMPLETE"))
                    expect(self.workflow.phases).to(contain(phase_command))
                    expect(self.workflow.current_phase_number).to(equal(1))
                    expect(self.phase_number).to(equal(0))
                
                with it('should start the next phase command in the workflow'):
                    # Arrange
                    phase_command = self.phase_command
                    next_phase_command = PhaseCommand(self.content, self.workflow, 1, "Next Phase")
                    self.workflow.phases = [phase_command, next_phase_command]
                    self.workflow.current_phase_number = 1
                    
                    # Act
                    self.workflow.start_next_phase()
                    next_phase_command.start()
                    
                    # Assert
                    expect(next_phase_command.start.called).to(be_true)
                    expect(self.workflow).not_to(be_none)
                    expect(self.workflow.phases).to(have_length(2))
                    expect(self.workflow.phases[0]).to(equal(phase_command))
                    expect(self.workflow.phases[1]).to(equal(next_phase_command))
                    expect(self.workflow.current_phase_number).to(equal(1))
                    expect(next_phase_command.phase_number).to(equal(1))
                    expect(next_phase_command.phase_name).to(equal("Next Phase"))
                    expect(next_phase_command.content).to(equal(self.content))
                    expect(self.phase_number).to(equal(0))

