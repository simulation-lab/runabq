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
    def test_get_input_files(self, mocker, tmpdir, simple_files_list, expected):
        from runabq import files
        mocker.patch.object(files.pathlib.Path, 'glob',
                            return_value=simple_files_list)
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        assert files._get_input_files(current_dir) == expected

    def test_get_input_files_none(self, mocker, tmpdir):
        from runabq import files
        mocker.patch.object(files.pathlib.Path, 'glob', return_value=list())
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        expected = list()
        assert files._get_input_files(current_dir) == expected

    def test_display_file_list(self, inpfile_dirlist):
        from runabq import files
        result = files._display_file_list(inpfile_dirlist)
        expected = None
        assert result == expected

    def test_get_file_code(self, mocker):
        from runabq import files
        mocker.patch.object(files, 'input', return_value=' 1, 3')
        result = files._get_file_code()
        expected = ['1', '3']
        assert result == expected

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
            # simple code
            (['1', '3'],
             {'target_input_files': (f for f in ['test1.inp', 'test3.inp']),
              'total_job_num': len(['test1.inp', 'test3.inp'])}),
            # coron code
            (['1:3'],
             {'target_input_files': (f for f in ['test1.inp', 'test2.inp', 'test3.inp']),
                'total_job_num': len(['test1.inp', 'test2.inp', 'test3.inp'])}),
        ]
    )
    def test_get_target_files(self, mocker, tmpdir, code, expected, inpfile_dirlist):
        from runabq import files
        mocker.patch.object(files, '_get_input_files',
                            return_value=inpfile_dirlist)
        mocker.patch.object(files, '_display_file_list',
                            return_value=None)
        mocker.patch.object(files, '_get_file_code',
                            return_value=code)
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        result = files.get_target_files(current_dir)
        result_target_files = [a for a in result['target_input_files']]
        expected_target_files = [b for b in expected['target_input_files']]
        assert result_target_files == expected_target_files
        assert result['total_job_num'] == expected['total_job_num']

    def test_get_target_files_noinput(self, mocker, tmpdir):
        from runabq import files
        mocker.patch.object(files.pathlib.Path, 'glob', return_value=list())
        mocker.patch.object(files, '_get_input_files', return_value=list())
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        result = files.get_target_files(current_dir)
        assert result == dict()

    def test_get_target_files_code_exit(self, mocker, tmpdir, inpfile_dirlist):
        from runabq import files
        code = 'x'  # exit
        mocker.patch.object(files, '_get_input_files',
                            return_value=inpfile_dirlist)
        mocker.patch.object(files, '_display_file_list',
                            return_value=None)
        mocker.patch.object(files, '_get_file_code',
                            return_value=code)
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        result = files.get_target_files(current_dir)
        expected = dict()
        assert result == expected

    def test_get_target_files_code_all(self, mocker, tmpdir, inpfile_dirlist):
        from runabq import files
        code = 'a'  # all
        mocker.patch.object(files, '_get_input_files',
                            return_value=inpfile_dirlist)
        mocker.patch.object(files, '_display_file_list',
                            return_value=None)
        mocker.patch.object(files, '_get_file_code',
                            return_value=code)
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        result_dict = files.get_target_files(current_dir)
        result = [a for a in result_dict['target_input_files']]
        expected = [target['file_name'] for target in inpfile_dirlist]
        assert set(result) == set(expected)

    def test_get_target_files_unsupport_code(self, mocker, tmpdir, inpfile_dirlist):
        from runabq import files
        code = ['askldf']  # unsupport code
        mocker.patch.object(files, '_get_input_files',
                            return_value=inpfile_dirlist)
        mocker.patch.object(files, '_display_file_list',
                            return_value=None)
        mocker.patch.object(files, '_get_file_code',
                            return_value=code)
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        result = files.get_target_files(current_dir)
        expected = dict()
        assert result == expected

    def test_get_target_files_notmatch_code(self, mocker, tmpdir, inpfile_dirlist):
        from runabq import files
        code = ['35000']  # not match code
        mocker.patch.object(files, '_get_input_files',
                            return_value=inpfile_dirlist)
        mocker.patch.object(files, '_display_file_list',
                            return_value=None)
        mocker.patch.object(files, '_get_file_code',
                            return_value=code)
        current_dir = tmpdir.mkdir('runabq_test_currentdir')
        result = files.get_target_files(current_dir)
        expected = dict()
        assert result == expected
