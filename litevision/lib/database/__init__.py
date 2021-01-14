from litevision.res.glob import *
import json


def read_json(path=APP_SETTINGS_PATH):
    with open(path) as file:
        read = json.load(file)
    return read


def write_to(obj, path=APP_SETTINGS_PATH):
    try:
        with open(path, "w+") as file:
            json.dump(obj, file, indent=4)
    except:
        print("İşlem başarısız...")
        return False
    return True


__all__ = ['read_json', 'write_to']