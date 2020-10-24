import pytest


class TestFiles:

    @pytest.fixture
    def input_file_list(self):
        return ['test1.inp', 'test2.inp', 'test3.inp']

    @pytest.mark.parametrize(
        'expected', [([
            {'cnt': 1, 'file_name': 'test1.inp'},
            {'cnt': 2, 'file_name': 'test2.inp'},
            {'cnt': 3, 'file_name': 'test3.inp'},
        ])]
    )
    def test_get_input_files(self, mocker, input_file_list, expected):
        from runabq.files import glob
        from runabq import files
        mocker.patch.object(files.glob, 'glob', return_value=input_file_list)
        assert files._get_input_files() == expected
