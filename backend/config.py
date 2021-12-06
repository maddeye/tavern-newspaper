import json
import os
import pathlib
import sys

from typing import Dict, Tuple, Union, List

SETTING_PATH = os.getenv("SETTINGS_PATH") or "./config.json"

DEFAULT_SETTINGS: Dict = {
    "done": [],
    "escalated": [],
    "city": 1
}


def ensure_config_path():
    """
    Esures that the config file is created and readable
    """
    path = pathlib.Path(SETTING_PATH)

    if not path.exists():
        try:
            with path.open("w", encoding="utf-8") as f:
                f.write(json.dumps(DEFAULT_SETTINGS, indent=2))
        except Exception:
            print(
                f"Fatal Error: Unable to create default configuration "
                f"at {SETTING_PATH}"
            )
            sys.exit(1)


def read_config() -> Dict:
    """
    Open and read the config file
    """
    with open(SETTING_PATH, "r") as f:
        return json.loads(f.read())


def write_config(config):
    """ 
    Open and write the config file
    """
    with open(SETTING_PATH, "w") as f:
        f.write(json.dumps(config, indent=2))


def get(key: str) -> Union[str, List[str], int]:
    """
    Read the config file and return value at given key
    """
    config: Dict = read_config()

    return config[key]


def get_escalation(quest_name: str) -> Tuple:
    """
    Get escalation object for given quest name
    """
    escalated = get("escalated")

    quest = [q for q in escalated if q["name"] and q["name"] == quest_name]

    if quest:
        return quest[0]

    return {}

def write(key: str, value):
    """
    Write the config file
    """
    config: Dict = read_config()

    config[key] = value
    
    write_config(config)

