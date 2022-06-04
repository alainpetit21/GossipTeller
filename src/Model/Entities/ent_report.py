from datetime import date

from src.Model.Entities.ent_attacker import EntityAttacker
from src.Model.Entities.ent_capability import EntityCapability
from src.Model.Entities.ent_infrastructure import EntityInfrastructure
from src.Model.Entities.ent_victim import EntityVictim


class EntityReport:
    def __init__(self):
        self.classification: str = ""
        self.serial_number: str = ""
        self.url_source: str = ""
        self.url_referred: str = ""
        self.url_saved: str = ""
        self.title: str = ""
        self.date_report:date = date(1970, 1, 1)
        self.date_saved:date = date(1970, 1, 1)
        self.product_id: str = ""
        self.attackers: list[EntityAttacker] = []
        self.victims: EntityVictim = EntityVictim()
        self.infrastructures: EntityInfrastructure = EntityInfrastructure()
        self.capabilities: EntityCapability = EntityCapability()
