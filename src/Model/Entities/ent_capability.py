from src.Model.Entities.ent_capability_category import EntityCapabilityCategory


class EntityCapability:
    def __init__(self):
        self.category: EntityCapabilityCategory = EntityCapabilityCategory()
        self.data: str = ""

