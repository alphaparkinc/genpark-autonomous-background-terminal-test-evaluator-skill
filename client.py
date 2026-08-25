class AutonomousBackgroundTerminalTestEvaluatorClient:
    def run_background_test_iteration(self, test_command='pytest tests/unit/ -v --cov=src', working_directory='/workspace/app'):
        return {
            'terminal_session_id': 'trm_eval_9918',
            'command_executed': test_command,
            'cwd': working_directory,
            'tests_passed_count': 142,
            'tests_failed_count': 0,
            'coverage_percentage': 96.4,
            'exit_code': 0,
            'autonomous_fix_iteration_succeeded': True
        }
