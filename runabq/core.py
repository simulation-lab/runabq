import os
import click
from runabq.args import get_solver_version, get_arg_terms
from runabq.files import get_target_files
from runabq.command import run_command

description = """
runabq is a command tool that can execute multiple input data files
of FEA software Abaqus in succession."""


@click.command(help=description)
@click.option('--version', '-v', default='latest', type=str,
              help='Abaqus version. example: if abq2021 then "-v 2021".')
@click.argument('keyword', nargs=-1)
def run(keyword: list, version: str):
    debug = False
    runabq(keyword, version, debug)
    click.echo('finished.')


def runabq(keyword: list, version: str, debug=True) -> None:
    current_dir = os.getcwd()
    if solver_version := get_solver_version(version):
        arg_terms = get_arg_terms(keyword)
        files = get_target_files(current_dir)
        if files:
            run_command(solver_version=solver_version,
                        arg_terms=arg_terms,
                        target_input_files=files['target_input_files'],
                        total_job_num=files['total_job_num'],
                        debug=debug)
    else:
        print('abaqus command not found.')
