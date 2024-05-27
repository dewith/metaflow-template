"""Utility functions for working with the yml file."""

from pathlib import Path

import yaml


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


def get_catalog() -> dict:
    """
    Read the catalog.yml file and return the contents as a dictionary.

    Returns
    -------
    dict
        The contents of the catalog.yml file as a dictionary.
    """
    return read_yaml('../conf/base/catalog.yml')


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

    dataset_folder = catalog['layers'][dataset_layer]
    dataset_filename = catalog[dataset]['path']
    return Path(dataset_folder) / dataset_filename


def get_parameters() -> dict:
    """
    Read the parameters.yml file and return the contents as a dictionary.

    Returns
    -------
    dict
        The contents of the parameters.yml file as a dictionary.
    """
    return read_yaml('../conf/base/params.yml')
