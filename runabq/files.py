import glob


def _get_input_files() -> list:
    input_files_list = glob.glob('*.inp')
    if not input_files_list:
        return None
    return [{'cnt': cnt, 'file_name': file}
            for cnt, file in enumerate(input_files_list, start=1)]


def _display_file_list(input_files_list: list):
    print("files list:")
    for unit in input_files_list:
        print(f"{unit['cnt']:6d}: {unit['file_name']:s}")
    print("     a: all")
    print("     x: exit")


def _get_file_code() -> list:
    code_list = input("code = ")
    unit_code_list = code_list.split(',')
    return [code.strip() for code in unit_code_list]


def _get_coron_code_files(code: str, input_files_list: list) -> list:
    first, last = code.split(':')
    if int(first) <= int(last):
        gen_range = range(int(first), int(last) + 1)
    else:
        gen_range = range(int(first), int(last) - 1, -1)
    filelist = []
    for num in gen_range:
        target = [file for file in input_files_list if file['cnt'] == num]
        filelist.append(target[0]['file_name'])
    return filelist


def get_target_files() -> dict:
    if input_files_list := _get_input_files():
        _display_file_list(input_files_list)
    else:
        print("no item.")
        return None

    codelist = [target['cnt'] for target in input_files_list]
    target_files = []
    for code in _get_file_code():
        code = code.strip()
        if code == 'x' or code == 'exit':
            return None
        elif code == 'a' or code == 'all':
            target_files = [target['file_name'] for target in input_files_list]
            break
        elif code != 'a' or code != 'all':
            if ':' in code:
                filelist = _get_coron_code_files(code, input_files_list)
                target_files.extend(filelist)
            else:
                try:
                    int_code = int(code)
                except ValueError as e:
                    print(f'{e}')
                    return None
                if not int_code in codelist:
                    print("No such file is found.")
                    return None
                for target in input_files_list:
                    if target['cnt'] == int_code:
                        target_files.append(target['file_name'])
                        break
    return {
        'target_input_files': (f for f in target_files),
        'total_job_num': len(target_files)
    }
