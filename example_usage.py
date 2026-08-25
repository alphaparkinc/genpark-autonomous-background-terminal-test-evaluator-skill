from client import AutonomousBackgroundTerminalTestEvaluatorClient

def main():
    client = AutonomousBackgroundTerminalTestEvaluatorClient()
    res = client.run_background_test_iteration('cargo test --all-targets --locked')
    print('Terminal Session: ' + res['terminal_session_id'] + ' (Exit Code: ' + str(res['exit_code']) + ')')
    print('Passed: ' + str(res['tests_passed_count']) + ' | Failed: ' + str(res['tests_failed_count']) + ' (Coverage: ' + str(res['coverage_percentage']) + '%)')
    print('Autonomous Fix Success: ' + str(res['autonomous_fix_iteration_succeeded']))

if __name__ == '__main__':
    main()
