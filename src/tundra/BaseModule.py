from .Entity import Permission_entity


class BaseModule:
    def __init__(self, type):
        self.type = type
        self.entitiees = {}

    def add_entity(self, entity):
        if not isinstance(entity, Permission_entity):
            raise ValueError(f"Invalid entity type: {type(entity)}")

        self.entitiees[entity.name] = entity

    def get_entity(self, name):
        return self.entitiees[name]

    def get_entities(self):
        return self.entitiees

    def get_type(self):
        return self.type

    def __repr__(self):
        return f"BaseModule(type={self.type}, entitiees={self.entitiees})"
