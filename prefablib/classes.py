from .functions import contains, is_int

class Type:

    def __init__(self, name: str = None, lib: str = None):
        self.name = name
        self.lib = lib
    
    def string(self):
        if self.name and self.lib:
            return f"{self.name}, {self.lib}"
    
    def from_string(self, string: str):
        if is_int(string[:1]) and string.find("|") != -1:
            string = string[string.find("|")+1:]
            self.lib = string[string.rfind(", ")+2:]
            self.name = string[:string.rfind(", ")]
        return self
    
class GUID:

    def __init__(self, guid: str = None):
        self.guid = guid
    
    def string(self):
        return self.__str__()
    
    def __str__(self):
        return f"$fstrref:GUID:{self.guid}" if self.guid else None
    
    def from_string(self, string: str):
        if string.startswith("$fstrref:"):
            string = string[9:]
        if string.startswith("GUID:"):
            self.guid = string[5:]
        return self
    
class CID:

    def __init__(self, cid: str = None):
        self.cid = cid
    
    def string(self):
        return self.__str__()
    
    def __str__(self):
        return f"$fstrref:CID:{self.cid}" if self.cid else None
    
    def from_string(self, string: str):
        if string.startswith("$fstrref:"):
            string = string[9:]
        if string.startswith("CID:"):
            self.guid = string[4:]
        return self


class Item:

    def __init__(self, type: Type, name: str = None, active: bool = True):
        self._type = type
        self.active = active
        
        self.name = name

    def to_dict(self):
        return {
            "$id": 0,
            "$type": self._type.string(),
            "name": self.name,
            "active": self.active,
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("name", "active")):
            self.name = data["name"]
            self.active = data["active"]
        return self
    
    def __str__(self):
        return self.name
    
class Position:

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def to_dict(self):
        return {
            "$type": 0,
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("x", "y", "z")): 
            self.x = data["x"]
            self.y = data["y"]
            self.z = data["z"]
        return self


class Rotation:

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: int = 1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def to_dict(self):
        return {
            "$type": 0,
            "value": {
                "$type": 0,
                "x": self.x,
                "y": self.x,
                "z": self.y,
                "w": self.w
            }
        }
    
    def from_dict(self, data: dict):
        if "value" in data:
            if contains(data["value"], ("x", "y", "z", "w")): 
                self.x = data["value"]["x"]
                self.y = data["value"]["y"]
                self.z = data["value"]["z"]
                self.w = data["value"]["w"]
        return self
    
class Mesh(Item):

    def __init__(self, mesh: GUID = None, position: Position = Position(), rotation: Rotation = Rotation(), require_state: bool = False):
        super(Mesh, self).__init__(
            type=Type("Game.Prefabs.ObjectMeshInfo", "Game"),
            name="ObjectMeshInfo",
            active=True
        )
        self.mesh = mesh
        self.position = position
        self.rotation = rotation
        self.require_state = require_state

    def to_dict(self):
        return {
            "$id": 0,
            "$type": self._type.string(),
            "active": self.active,
            "m_Mesh": self.mesh.string(),
            "m_Position": self.position.to_dict(),
            "m_Rotation": self.rotation.to_dict(),
            "m_RequireState": self.require_state,
        }
    
    def from_dict(self, data: dict):
        if contains(data, ("active", "m_Mesh", "m_Position", "m_Rotation", "m_RequireState")): 
            self.active = data["active"]
            self.mesh = GUID().from_string(data["m_Mesh"])
            self.position = Position().from_dict(data["m_Position"])
            self.rotation = Rotation().from_dict(data["m_Rotation"])
            self.require_state = data["m_RequireState"]
        return self