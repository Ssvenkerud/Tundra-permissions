import pytest
import logging

from src.tundra.BaseModule import BaseModule
from src.tundra.Entity import Permission_entity

logging.basicConfig(level=logging.DEBUG)


entity1 = Permission_entity(name="TestEntity", data={"key1": "value1", "key2": "value2"})
entity2 = Permission_entity(name="TestEntity2", data={"key1": "value1", "key2": "value2"})
entity3 = Permission_entity(name="TestEntity3", data={"key1": "value1", "key2": "value2"})
multiple_entities = [entity1, entity2, entity3]


def test_base_module_setup():
    base_module = BaseModule(type='test')
    assert base_module is not None
    assert base_module.type == 'test'
    assert base_module.entitiees == {}


def test_base_module_add_entity():
    base_module = BaseModule(type='test')
    base_module.add_entity(entity1)

    assert base_module.get_entity("TestEntity") is not None
    assert base_module.get_entity("TestEntity").name == "TestEntity"
    assert base_module.get_entity("TestEntity").data == {"key1": "value1", "key2": "value2"}


def test_base_module_add_entity_with_invalid_type():
    base_module = BaseModule(type='test')
    with pytest.raises(ValueError):
        base_module.add_entity("test")


def test_base_module_get_entity_not_found():
    base_module = BaseModule(type='test')
    with pytest.raises(KeyError):
        base_module.get_entity("TestEntity")

def test_base_module_add_multiple_entities():
    base_module = BaseModule(type='test')
    for entity in multiple_entities:
        base_module.add_entity(entity)

    assert base_module.get_entity("TestEntity") is not None
    assert base_module.get_entity("TestEntity").name == "TestEntity"
    assert base_module.get_entity("TestEntity").data == {"key1": "value1", "key2": "value2"}

    assert base_module.get_entity("TestEntity2") is not None
    assert base_module.get_entity("TestEntity2").name == "TestEntity2"
    assert base_module.get_entity("TestEntity2").data == {"key1": "value1", "key2": "value2"}

    assert base_module.get_entity("TestEntity3") is not None
    assert base_module.get_entity("TestEntity3").name == "TestEntity3"
    assert base_module.get_entity("TestEntity3").data == {"key1": "value1", "key2": "value2"}

def test_base_module_get_entities():
    base_module = BaseModule(type='test')
    for entity in multiple_entities:
        base_module.add_entity(entity)

    assert base_module.get_entities() is not None
    assert base_module.get_entities() == {"TestEntity": entity1, "TestEntity2": entity2, "TestEntity3": entity3}
