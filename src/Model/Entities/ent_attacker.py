from src.Model.Entities.ent_actor import EntityActor
from src.Model.Entities.ent_country import EntityCountry
from src.Model.Entities.ent_organisation import EntityOrganisation


class EntityAttacker:
    def __init__(self):
        self.country: EntityCountry = EntityCountry()
        self.organisation: EntityOrganisation = EntityOrganisation()
        self.actor: EntityActor = EntityActor()
        self.other: str = ""
