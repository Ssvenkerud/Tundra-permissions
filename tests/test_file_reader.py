import pytest
import yaml

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
