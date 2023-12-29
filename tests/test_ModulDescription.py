import pytest
from src.tundra.ModuleDescription import ModuleDescription

def test_module_description_gather_description(databases_object):
    description = ModuleDescription("databases")
    description.gather_description(databases_object)
    assert description.count == 3
    assert description.entities == ["database1", "database2", "database3"]

@pytest.mark.skip(reason="Not implemented")
def test_module_description_return_description(databases_object):
    description = ModuleDescription("databases")
    description.gather_description(databases_object)
    assert description.return_description() == {
        "count": 3,
        "entities": ["database1", "database2", "database3"],
    }
