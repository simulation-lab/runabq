import pytest


class TestArgs:

    @pytest.mark.parametrize('version, expected', [
        ('latest', 'abaqus'),
        ('2020', 'abq2020'),
        ('2020se', 'abq2020se')
    ])
    def test_get_solver_version(self, mocker, version, expected):
        from runabq.args import get_solver_version
        from runabq import args
        mocker.patch.object(args, 'which', return_value=version)
        assert get_solver_version(version) == expected

    @ pytest.mark.parametrize('keyword, expected', [
        (['user=sub.f', ], 'user=sub.f'),
        (['user=job1.f', 'cpus=3', ], 'user=job1.f cpus=3'),
    ])
    def test_get_arg_terms(self, keyword, expected):
        from runabq.args import get_arg_terms
        assert get_arg_terms(keyword) == expected
