from .classes import Type, Item, Mesh
from .functions import normalize_list, contains
from .constants import components

class Prefab(Item):

    def __init__(self, type: Type, name: str = None, active: bool = True, meshes: list[Mesh] = list(), circular: bool = False):
        super(Prefab, self).__init__(
            type=type,
            name=name,
            active=active
        )
        self.components = list()
        self.meshes = meshes
        self.circular = circular

    def to_dict(self):
        return {
            "$id": 0,
            "$type": self._type.string(),
            "name": self.name,
            "active": self.active,
            "components": normalize_list(obj=self.components, type=Type("System.Collections.Generic.List`1[[Game.Prefabs.ComponentBase, Game]]", "mscorlib")),
            "m_Meshes": normalize_list(obj=self.meshes, type=Type("Game.Prefabs.ObjectMeshInfo[]", "Game")),
            "m_Circular": self.circular
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("name", "active", "components", "m_Meshes", "m_Circular")):
            self.name = data["name"]
            self.active = data["active"]
            self.circular = data["m_Circular"]
            self.meshes = []
            for mesh in data["m_Meshes"]["$rcontent"]:
                self.meshes.append(Mesh().from_dict(mesh))

            self.components = []
            for component in data["components"]["$rcontent"]:
                comp_type = Type().from_string(component["$type"])
                for component_check in components:
                    if component_check._type.name == comp_type.name and component_check._type.lib == comp_type.lib:
                        self.components.append(component_check.__class__().from_dict(component))

        return self
    

class BuildingPrefab(Prefab):

    def __init__(self, name: str = None, meshes: list[Mesh] = list(), circular: bool = False, access_type: int = 0, lot_width: int = 0, lot_depth: int = 0):
        super(BuildingPrefab, self).__init__(
            type=Type("Game.Prefabs.BuildingPrefab", "Game"),
            name=name,
            active=True,
            meshes=meshes,
            circular=circular
        )
        self.access_type = access_type
        self.lot_width = lot_width
        self.lot_depth = lot_depth

    def to_dict(self):
        return {
            "$id": 0,
            "$type": self._type.string(),
            "name": self.name,
            "active": self.active,
            "components": normalize_list(obj=self.components, type=Type("System.Collections.Generic.List`1[[Game.Prefabs.ComponentBase, Game]]", "mscorlib")),
            "m_Meshes": normalize_list(obj=self.meshes, type=Type("Game.Prefabs.ObjectMeshInfo[]", "Game")),
            "m_Circular": self.circular,
            "m_AccessType": self.access_type,
            "m_LotWidth": self.lot_width,
            "m_LotDepth": self.lot_depth,
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("name", "active", "components", "m_Meshes", "m_Circular", "m_AccessType", "m_LotWidth", "m_LotDepth")):
            self.name = data["name"]
            self.active = data["active"]
            self.circular = data["m_Circular"]
            self.access_type = data["m_AccessType"]
            self.lot_width = data["m_LotWidth"]
            self.lot_depth = data["m_LotDepth"]
            self.meshes = []
            for mesh in data["m_Meshes"]["$rcontent"]:
                self.meshes.append(Mesh().from_dict(mesh))
            
            self.components = []
            for component in data["components"]["$rcontent"]:
                comp_type = Type().from_string(component["$type"])
                for component_check in components:
                    if component_check._type.name == comp_type.name and component_check._type.lib == comp_type.lib:
                        self.components.append(component_check.__class__().from_dict(component))

        return self

class BuildingExtensionPrefab(Prefab):

    def __init__(self, name: str = None, meshes: list[Mesh] = list(), circular: bool = False):
        super(BuildingExtensionPrefab, self).__init__(
            type=Type("Game.Prefabs.BuildingExtensionPrefab", "Game"),
            name=name,
            active=True,
            meshes=meshes,
            circular=circular
        )

    def to_dict(self):
        return {
            "$id": 0,
            "$type": self._type.string(),
            "name": self.name,
            "active": self.active,
            "components": normalize_list(obj=self.components, type=Type("System.Collections.Generic.List`1[[Game.Prefabs.ComponentBase, Game]]", "mscorlib")),
            "m_Meshes": normalize_list(obj=self.meshes, type=Type("Game.Prefabs.ObjectMeshInfo[]", "Game")),
            "m_Circular": self.circular,
            "m_Position": {
                "$type": "Unity.Mathematics.float3, Unity.Mathematics",
                "x": 0,
                "y": 0,
                "z": 0
            },
            "m_OverrideLotSize": {
                "$type": 0,
                "x": 0,
                "y": 0
            },
            "m_OverrideHeight": 0
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("name", "active", "components", "m_Meshes", "m_Circular")):
            self.name = data["name"]
            self.active = data["active"]
            self.circular = data["m_Circular"]
            self.meshes = []
            for mesh in data["m_Meshes"]["$rcontent"]:
                self.meshes.append(Mesh().from_dict(mesh))
            
            self.components = []
            for component in data["components"]["$rcontent"]:
                comp_type = Type().from_string(component["$type"])
                for component_check in components:
                    if component_check._type.name == comp_type.name and component_check._type.lib == comp_type.lib:
                        self.components.append(component_check.__class__().from_dict(component))
                        
        return self