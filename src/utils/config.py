"""Utility functions for working with the yml file."""

from pathlib import Path

import yaml


def check_cwd() -> str:
    """
    Check the current working directory and determines the appropriate prefix based
    on the directory structure. The prefix is used to construct relative paths in the code.

    Returns
    -------
    str
        The prefix to be used for constructing relative paths.

    Raises
    ------
    ValueError
        If the working directory is invalid.
    """
    cwd = Path.cwd()
    if (cwd / 'setup.py').exists():
        prefix = ''
    elif cwd.parts[-1] == 'src':
        prefix = '../'
    else:
        raise ValueError(f'Invalid working directory: {cwd}')

    return prefix


def read_yaml(path: str) -> dict:
    """
    Read a YAML file and return the contents as a dictionary.

    Parameters
    ----------
    path : str
        The path to the YAML file.

    Returns
    -------
    dict
        The contents of the YAML file as a dictionary.
    """
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_parameters() -> dict:
    """
    Read the parameters.yml file and return the contents as a dictionary.

    Returns
    -------
    dict
        The contents of the parameters.yml file as a dictionary.
    """
    prefix = check_cwd()
    return read_yaml(prefix + '../conf/base/params.yml')


def get_catalog() -> dict:
    """
    Read the catalog.yml file and return the contents as a dictionary.

    Returns
    -------
    dict
        The contents of the catalog.yml file as a dictionary.
    """
    prefix = check_cwd()
    return read_yaml(prefix + 'conf/base/catalog.yml')


def get_dataset_path(dataset: str) -> Path:
    """
    Return the path to the dataset.

    Parameters
    ----------
    dataset : str
        The name of the dataset.

    Returns
    -------
    Path
        The path to the dataset.
    """
    catalog = get_catalog()
    dataset_layer = catalog[dataset]['layer']

    prefix = check_cwd()
    dataset_folder = prefix + catalog['layers'][dataset_layer]
    dataset_filename = catalog[dataset]['path']
    return Path(dataset_folder) / dataset_filename


if __name__ == '__main__':
    working_dir = Path.cwd()
    if (working_dir / 'setup.py').exists():
        print(f'In the project root: {working_dir}')
    elif working_dir.parts[-1] == 'src':
        print(f'In the src folder: {working_dir}')
    else:
        print(f'Invalid working directory: {working_dir}')
