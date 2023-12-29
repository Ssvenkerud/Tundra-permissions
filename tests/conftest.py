import pytest
import yaml

from src.tundra.BaseModule import BaseModule
from src.tundra.DatabasesModule import DatabasesModule

space = " " * 2


def load_yaml(yaml_file):
    with open(yaml_file, "r") as in_fh:
        file = yaml.safe_load(in_fh)
    return file

# Base Module


@pytest.fixture
def object1():
    return [{"entitiy1": {"key": "value"}}, {"entitiy2": {"key": "value"}}]


@pytest.fixture
def object2():
    return [{"entitiy2": {"key": "value"}}, {"entitiy3": {"key": "value"}}]


@pytest.fixture
def base_module_loaded():
    base_module = BaseModule()
    base_module.spesification = {
        "entitiy1": {"key": "value"},
        "entitiy2": {"key": "value"},
        "entitiy3": {"key": "value"},
    }
    return base_module


@pytest.fixture
def base_module_loaded_with_dependencies():
    base_module = BaseModule()
    base_module.spesification = {
        "entitiy1": {"key": "value"},
        "entitiy2": {"member_of": "dependency1"},
        "entitiy3": {"member_of": "dependency2"},
        "entitiy4": {"warehouse": "dependency4"},
    }
    return base_module

# Databases


@pytest.fixture
def databases_object():
    databases = DatabasesModule()
    databases.spesification = {
        "database1": {"shared": "yes", "owner": "loader_qlik"},
        "database2": {"shared": "no", "owner": "loader_qlik"},
        "database3": {"shared": "yes"},
    }
    return databases


@pytest.fixture
def databases_object1():
    return [
        {"database1": {"shared": "yes", "owner": "loader_qlik"}},
        {"database2": {"shared": "no", "owner": "loader_qlik"}},
    ]


@pytest.fixture
def databases_object2():
    return [
        {"database3": {"shared": "yes"}},
        {"database2": {"shared": "no", "owner": "loader_qlik"}},
    ]


@pytest.fixture
def single_database_object():
    database = DatabasesModule()
    database.spesification = {"database1": {"shared": "yes", "owner": "loader_qlik"}}
    return database


@pytest.fixture
def databases(databases_object):
    return databases_object.describe()


@pytest.fixture
def single_database_object_str_results():
    return f"""databases:\n{space*1}- database1:\n{space*3}shared: yes\n{space*3}owner: loader_qlik\n"""


@pytest.fixture
def databases_object_str_results(single_database_object_str_results):
    return (
        single_database_object_str_results
        + f"""{space*1}- database2:\n{space*3}shared: no\n{space*3}owner: loader_qlik\n{space*1}- database3:\n{space*3}shared: yes\n"""
    )



