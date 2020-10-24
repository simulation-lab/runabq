import pytest


class TestFiles:

    @pytest.fixture
    def input_files_list(self):
        return ['test1.inp', 'test2.inp', 'test3.inp']

    @pytest.fixture
    def inpfile_dirlist(self):
        return [
            {'cnt': 1, 'file_name': 'test1.inp'},
            {'cnt': 2, 'file_name': 'test2.inp'},
            {'cnt': 3, 'file_name': 'test3.inp'},
            {'cnt': 4, 'file_name': 'test4.inp'},
            {'cnt': 5, 'file_name': 'test5.inp'},
        ]

    @pytest.mark.parametrize(
        'expected', [
            ([{'cnt': 1, 'file_name': 'test1.inp'},
              {'cnt': 2, 'file_name': 'test2.inp'},
              {'cnt': 3, 'file_name': 'test3.inp'}, ])
        ]
    )
    def test_get_input_files(self, mocker, input_files_list, expected):
        from runabq import files
        mocker.patch.object(files.glob, 'glob', return_value=input_files_list)
        assert files._get_input_files() == expected

    @pytest.mark.parametrize(
        'code, expected', [
            ('2:3', ['test2.inp', 'test3.inp']),
            ('3:1', ['test3.inp', 'test2.inp', 'test1.inp']),
        ]
    )
    def test_get_coron_code_files(self, code, inpfile_dirlist, expected):
        from runabq import files
        result = files._get_coron_code_files(code, inpfile_dirlist)
        assert result == expected
