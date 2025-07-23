from .classes import Type, Item, GUID, CID
from .functions import normalize_list, contains

class Component(Item):

    def __init__(self, type: Type, name: str, active: bool = True):
        super(Component, self).__init__(
            type=type,
            name=name,
            active=active
        )

    def from_dict(self, data: dict):
        if contains(data, ("name", "active")):
            self.name = data["name"]
            self.active = data["active"]
        return self

class UIObject(Component):

    def __init__(self, group: GUID = None, priority: int = 0, icon: str = None, isdebug: bool = False):
        super(UIObject, self).__init__(
            type=Type("Game.Prefabs.UIObject", "Game"),
            name="UIObject",
            active=True
        )
        self.group = group
        self.priority = priority
        self.icon = icon
        self.isdebug = isdebug

    def to_dict(self):
        return {
            "$id": 0,
            "$type": self._type.string(),
            "name": self.name,
            "active": self.active,
                "m_Group": (self.group.string() if self.group else None),
            "m_Priority": self.priority,
            "m_Icon": self.icon,
            "m_IsDebugObject": self.isdebug,
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("name", "active", "m_Group", "m_Priority", "m_Icon", "m_IsDebugObject")):
            self.name = data["name"]
            self.active = data["active"]
            if isinstance(data["m_Group"], str):
                self.group = GUID().from_string(data["m_Group"])
            self.priority = data["m_Priority"]
            self.icon = data["m_Icon"]
            self.isdebug = data["m_IsDebugObject"]
        return self

class ServiceUpgrade(Component):

    def __init__(self, buildings: list[CID] = None, upgrade_cost: int = 0, xp_reward: int = 0, max_placement_offset: int = -1, max_placement_distance: int = 0):
        super(ServiceUpgrade, self).__init__(
            type=Type("Game.Prefabs.ServiceUpgrade", "Game"),
            name="ServiceUpgrade",
            active=True
        )
        self.buildings = buildings
        self.upgrade_cost = upgrade_cost
        self.xp_reward = xp_reward
        self.max_placement_offset = max_placement_offset
        self.max_placement_distance = max_placement_distance

    def to_dict(self):
        return {
            "$id": 0,
            "$type": self._type.string(),
            "name": self.name,
            "active": self.active,
            "m_Buildings": normalize_list(self.buildings, type=Type("Game.Prefabs.BuildingPrefab[]", "Game")),
            "m_UpgradeCost": self.upgrade_cost,
            "m_XPReward": self.xp_reward,
            "m_MaxPlacementOffset": self.max_placement_offset,
            "m_MaxPlacementDistance": self.max_placement_distance,
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("name", "active", "m_Buildings", "m_UpgradeCost", "m_XPReward", "m_MaxPlacementOffset", "m_MaxPlacementDistance")):
            self.name = data["name"]
            self.active = data["active"]
            self.upgrade_cost = data["m_UpgradeCost"]
            self.xp_reward = data["m_XPReward"]
            self.max_placement_offset = data["m_MaxPlacementOffset"]
            self.max_placement_distance = data["m_MaxPlacementDistance"]
            self.buildings = []
            for building in data["m_Buildings"]:
                self.buildings.append(CID().from_string(building))
        return self
