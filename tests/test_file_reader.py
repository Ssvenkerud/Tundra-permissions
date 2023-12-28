import pytest
import yaml

from src.tundra.file_loader import load_yaml
from src.tundra.FileReader import FileReader


def load_yaml_file(file_name):
    with open(file_name, "r") as file:
        return yaml.safe_load(file)


def test_FileReader_dir():
    reader = FileReader()
    assert set(reader.load_dir("tests/data/base_premissions")) == set(
        [
            "tests/data/base_premissions/team_a_permisions.yml",
            "tests/data/base_premissions/team_b_permisions.yml",
        ]
    )
    assert set(reader.files) == set(
        [
            "tests/data/base_premissions/team_a_permisions.yml",
            "tests/data/base_premissions/team_b_permisions.yml",
        ]
    )


def test_FileReader_empty_dir():
    reader = FileReader()
    with pytest.raises(Exception):
        reader.load_dir("tests/data/empty")
    assert reader.files == []


def test_FileReader_dir_not_found():
    reader = FileReader()
    with pytest.raises(Exception):
        reader.load_dir("tests/data/not_found")
    assert reader.files == []


def test_FileReader_not_dir():
    reader = FileReader()
    assert reader.load_dir("tests/data/base_premissions/team_a_permisions.yml") == [
        "tests/data/base_premissions/team_a_permisions.yml"
    ]
    assert reader.files == ["tests/data/base_premissions/team_a_permisions.yml"]


def test_FileReader_import_files():
    reader = FileReader()
    reader.load_dir("tests/data/base_premissions/team_a_permisions.yml")
    assert reader.import_files(load_yaml) == [
        load_yaml_file("tests/data/base_premissions/team_a_permisions.yml")
    ]


def test_FileReader_import_files_dir():
    reader = FileReader()
    reader.load_dir("tests/data/base_premissions")
    assert reader.import_files(load_yaml) == [
        load_yaml_file("tests/data/base_premissions/team_b_permisions.yml"),
        load_yaml_file("tests/data/base_premissions/team_a_permisions.yml"),
    ]


def test_FileReader_imoport_files_file_empty():
    reader = FileReader()
    with pytest.raises(Exception):
        reader.load_dir("tests/data/empty/empty.yaml")
    assert reader.import_files(load_yaml) == []


def test_FileReader_import_files_file_not_yaml():
    reader = FileReader()
    with pytest.raises(Exception):
        reader.load_dir("tests/data/not_yaml.txt")
    assert reader.import_files(load_yaml) == []


def test_FileReader_import_files_empty_dir():
    reader = FileReader()
    with pytest.raises(Exception):
        reader.load_dir("tests/data/empty")
    assert reader.import_files(load_yaml) == []


def test_FileReader_import_files_not_found():
    reader = FileReader()
    with pytest.raises(Exception):
        reader.load_dir("tests/data/not_found")
    assert reader.import_files(load_yaml) == []
