class Permission_entity:
    def __init__(self, permision_type="udefined", name="none", data=None):
        self.name = name
        self.type = permision_type
        self.data = data
