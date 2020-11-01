import subprocess
import os
from shutil import get_terminal_size


def run_command(solver_version: str,
                arg_terms: str,
                target_input_files: list,
                total_job_num: int,
                debug=True) -> None:
    columns = get_terminal_size().columns
    for num, target in enumerate(target_input_files, start=1):
        inpfile = target.rstrip('.inp')
        command_list = [solver_version,
                        'interactive', '-j', inpfile]
        if arg_terms:
            command_list.append(arg_terms)

        print('-' * columns)
        print(f'job: {target}')
        print(f'progress: {num}/{total_job_num}')
        print('-' * columns)

        if debug:
            print(command_list)
        else:
            subprocess.run(command_list, shell=True, cwd=os.getcwd())
