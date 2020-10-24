import pytest


class TestCommand:

    @pytest.mark.parametrize(
        'command_args, expected', [
            ({
                'solver_version': '2020',
                'arg_terms': 'cpus=3',
                'target_input_files': ['job1.inp', 'job3.inp'],
                'total_job_num': 3,
                'debug': True,
            },
                "['2020', 'interactive', '-j', 'job3', 'cpus=3']",
            ),
        ])
    def test_run_command(self, capfd, command_args, expected):
        from runabq.command import run_command
        run_command(
            solver_version=command_args['solver_version'],
            arg_terms=command_args['arg_terms'],
            target_input_files=command_args['target_input_files'],
            total_job_num=command_args['total_job_num'],
            debug=command_args['debug']
        )
        out, err = capfd.readouterr()
        out_list = out.split('\n')
        out_list = [a for a in out_list if a.strip()]
        assert out_list[-1] == expected
        assert err == ''
