def normalize_list(obj: list, type):
    normalized_content = []

    if len(obj) > 0:

        for item in obj:
            if hasattr(item, 'to_dict') and callable(getattr(item, 'to_dict')):
                normalized_content.append(item.to_dict())
            elif hasattr(item, 'string') and callable(getattr(item, 'string')):
                normalized_content.append(item.string())
            else:
                normalized_content.append(item)
       
    return {
        "$id": 0,
        "$type": type.string(),
        "$rlength": len(obj),
        "$rcontent": normalized_content
    }

def id_from_type(type: str):
    return type[:type.find("|")]

def contains(d: dict, keys: tuple):
    return all(k in d for k in keys)

def is_int(string: str):
    try:
        int(string)
        return True
    except ValueError:
        return False