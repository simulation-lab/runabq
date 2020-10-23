import subprocess
from shutil import get_terminal_size


def run_command(solver_version: str,
                arg_terms: str,
                target_input_files: list,
                total_job_num: int):
    columns = get_terminal_size().columns
    for num, target in enumerate(target_input_files, start=1):
        inpfile = target.rstrip('.inp')
        if not arg_terms:
            arg_terms = ''
        command_list = [solver_version,
                        'interactive', '-j', inpfile, arg_terms]

        print('-' * columns)
        print(f'job: {target}')
        print(f'progress: {num}/{total_job_num}')
        print('-' * columns)
        print(command_list)
        # subprocess.run(command_list)
