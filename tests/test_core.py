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
        assert out.strip() == 'abq-command not found.'
        assert err == ''
