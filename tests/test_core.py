import pytest


class TestRunabq:
    @pytest.mark.parametrize('keyword, version', [('user=job1.f', '2020')])
    def test_runabq(self, keyword, version):
        from runabq.core import runabq
        assert runabq(keyword, version) == None
