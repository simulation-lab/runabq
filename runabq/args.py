from shutil import which


def get_solver_version(version: list) -> str:
    if version == 'latest':
        abc = 'abaqus'
    else:
        abc = 'abq' + version
    if which(abc):
        return abc
    else:
        return None


def get_arg_terms(keyword: list) -> str:
    if keyword:
        return ' '.join(keyword)
    else:
        return None
