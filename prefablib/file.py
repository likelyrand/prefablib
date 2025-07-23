import os, re, json

from typing import TypeVar

from .prefab import Prefab, BuildingPrefab, BuildingExtensionPrefab

P = TypeVar("P", bound=Prefab)

indent = "    "


def check_file(fp: str) -> bool:

    if os.path.exists(fp) and os.path.isfile(fp) and fp.endswith(".Prefab"):
        return True
    return False


def get_cid(fp):
    if os.path.exists(fp+".cid"):
        with open(fp+".cid", "r") as cid:
            return cid.read()
        
def reads_dict(string: str) -> dict:
    fixed_string = re.sub(r'\$fstrref:"([^"]*)"', r'"$fstrref:\1"', string)

    data = json.loads(fixed_string)

    def process(item):

        if isinstance(item, dict):
            if "$type" in item and isinstance(item["$type"], str):
                item["$type"] = item["$type"][item["$type"].find("|")+1:]

            for child in item.values():
                process(child)

        elif isinstance(item, list):
            for child in item:
                process(child)

    process(data)

    return data

def from_dict(data: dict) -> P:
    
    if "$type" in data:

        if data["$type"] == "Game.Prefabs.BuildingPrefab, Game":

            return BuildingPrefab().from_dict(data)
        
        elif data["$type"] == "Game.Prefabs.BuildingExtensionPrefab, Game":
            
            return BuildingExtensionPrefab().from_dict(data)

def reads(string: str) -> P:

    data = reads_dict(string)

    return from_dict(data=data)


def read(fp: str) -> tuple[P, str]:

    if not check_file(fp):
        raise ValueError("filepath provided does not lead to a .Prefab file")

    with open(fp, "r") as f:
        string = f.read()

    return reads(string=string)


def encode(data, cur: int = 1):
    
    if isinstance(data, dict):

        items = []

        for key, value in data.items():

            item = f'"{key}": {encode(value, cur+1)}'
            items.append(indent*cur+item)

        inner = ",\n".join(items)
        return "{\n"+inner+"\n"+indent*(cur-1)+"}"
    

    elif isinstance(data, list):
        
        items = []

        for value in data:

            item = encode(value, cur+1)
            items.append(indent*cur+item)
        
        inner = ", \n".join(items)
        return "[\n"+inner+"\n"+indent*(cur-1)+"]"

    elif isinstance(data, str):

        if data.startswith("$fstrref:"):
            return f'$fstrref:"{data[9:]}"'
        
        else:
            return f'"{data}"'

    else:
        return json.dumps(data)
    

def assign_ids(data: dict):
    id = 0
    typeid = 0

    def process(item):
        nonlocal id, typeid

        if isinstance(item, dict):
            if "$id" in item:
                item["$id"] = id
                id += 1

            if "$type" in item:
                if isinstance(item["$type"], str):
                    item["$type"] = f"{str(typeid)}|{item['$type']}"
                elif isinstance(item["$type"], int):
                    item["$type"] = typeid
                typeid += 1

            for value in item.values():
                process(value)

        elif isinstance(item, (list, tuple)):
            for element in item:
                process(element)

    process(data)
    return data


def dumps(prefab: P) -> dict:

    data = prefab.to_dict()

    data = assign_ids(data)

    data = encode(data)
    
    return data


def dump(fp: str, prefab: P) -> None:

    data = prefab.to_dict()

    data = assign_ids(data)

    data = encode(data)

    with open(fp, "w") as f:
        f.write(data)