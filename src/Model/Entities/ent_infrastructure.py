from src.Model.Entities.ent_infrastructure_category import EntityInfrastructureCategory


class EntityInfrastructure:
    def __init__(self):
        self.category: EntityInfrastructureCategory = EntityInfrastructureCategory()
        self.data: str = ""

