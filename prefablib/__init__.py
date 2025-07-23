"""
A library for modifying Cities Skylines 2 .Prefab files.
"""
__name__ = "prefablib"
__version__ = "1.0.0"

from .file import dump, dumps, read, reads, reads_dict, from_dict
from .prefab import BuildingPrefab, BuildingExtensionPrefab
from .component import UIObject, ServiceUpgrade
from .classes import GUID, CID, Mesh, Rotation, Position
