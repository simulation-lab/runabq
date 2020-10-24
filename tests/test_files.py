import pytest


class TestFiles:

    @pytest.fixture
    def simple_files_list(self):
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
    def test_get_input_files(self, mocker, simple_files_list, expected):
        from runabq import files
        mocker.patch.object(files.glob, 'glob', return_value=simple_files_list)
        assert files._get_input_files() == expected

    @pytest.mark.parametrize(
        'code, expected', [
            ('2:3', ['test2.inp', 'test3.inp']),
            ('3:1', ['test3.inp', 'test2.inp', 'test1.inp']),
        ]
    )
    def test_get_coron_code_files(self, code, expected, inpfile_dirlist):
        from runabq import files
        result = files._get_coron_code_files(code, inpfile_dirlist)
        assert result == expected

    @pytest.mark.parametrize(
        'code, expected', [
            (['1', '3'],
             {'target_input_files': (f for f in ['test1.inp', 'test3.inp']),
              'total_job_num': len(['test1.inp', 'test3.inp'])})
        ]
    )
    def test_get_target_files(self, mocker, code, expected, inpfile_dirlist):
        from runabq import files
        mocker.patch.object(files, '_get_input_files',
                            return_value=inpfile_dirlist)
        mocker.patch.object(files, '_display_file_list',
                            return_value=None)
        mocker.patch.object(files, '_get_file_code',
                            return_value=code)
        result = files.get_target_files()
        result_target_files = [a for a in result['target_input_files']]
        expected_target_files = [b for b in expected['target_input_files']]
        assert result_target_files == expected_target_files
        assert result['total_job_num'] == expected['total_job_num']
