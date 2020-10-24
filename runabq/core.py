import click
from runabq.args import get_solver_version, get_arg_terms
from runabq.files import get_target_files
from runabq.command import run_command


@click.command()
@click.option('--version', '-v', default='latest', type=str)
@click.argument('keyword', nargs=-1)
def run(keyword, version):
    runabq(keyword, version)
    click.echo('finished.')


def runabq(keyword, version):
    if solver_version := get_solver_version(version):
        arg_terms = get_arg_terms(keyword)
        files = get_target_files()
        if files:
            run_command(solver_version=solver_version,
                        arg_terms=arg_terms,
                        target_input_files=files['target_input_files'],
                        total_job_num=files['total_job_num'],
                        debug=False)
        else:
            print('file not found.')
    else:
        print('abq-command not found.')
