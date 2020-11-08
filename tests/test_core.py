import pytest


class TestCore:

    @pytest.fixture
    def scenario_data(self):
        target_files = {
            'target_input_files': (f for f in ['job1.inp', 'job2.inp']),
            'total_job_num': 2
        }
        return {
            'solver_version': 'abq2020',
            'arg_terms': 'user=sub.f',
            'files': target_files,
            'expected': None
        }

    def test_runabq_stdout(self, capfd, scenario_data):
        from runabq.core import runabq
        from runabq import core

        keyword = scenario_data['arg_terms']
        version = scenario_data['solver_version']
        runabq(keyword, version)
        out, err = capfd.readouterr()
        assert out.strip() == 'abaqus command not found.'
        assert err == ''

    def test_run_function(self, mocker):
        from click.testing import CliRunner
        from runabq.core import run
        from runabq import core
        mocker.patch.object(core, 'runabq', return_value=None)
        runner = CliRunner()
        result = runner.invoke(run)
        assert result.exit_code == 0
        assert result.output == 'finished.\n'

    @pytest.fixture
    def commandline_option(self):
        target_files = ['test1.inp', 'test2.inp', 'test3.inp']
        return {
            'keyword': ['cpus=5'],
            'version': 'latest',
            'solver_version': 'abaqus',
            'arg_terms': 'cpus=5 user=test.f90',
            'get_target_files': {
                'target_input_files': (f for f in target_files),
                'total_job_num': len(target_files)
            },
            'debug': True
        }

    def test_runabq(self, mocker, commandline_option):
        from runabq import core
        co = commandline_option
        mocker.patch.object(core, 'get_solver_version',
                            return_value=co['solver_version'])
        mocker.patch.object(core, 'get_arg_terms',
                            return_value=co['arg_terms'])
        mocker.patch.object(core, 'get_target_files',
                            return_value=co['get_target_files'])
        mocker.patch.object(core, 'run_command', return_value=None)
        result = core.runabq(
            keyword=co['keyword'], version=co['version'], debug=co['debug'])
        assert result == None
