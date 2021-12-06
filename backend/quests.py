import json
import random

from os import listdir
from os.path import isfile, join
from typing import Dict

import config

QUEST_PATH = "./quests/"


def read_quest(quest_name: str) -> Dict:
    """
    Read quest file and return quest object based on escalation level and city level
    """
    escalated = config.get("escalated")
    esc = config.get_escalation(quest_name)

    rquest = {}

    with open(QUEST_PATH + quest_name + ".json", "r") as f:
        quest = json.loads(f.read())

    for q in quest:
        if not bool(esc):
            if q['escalation'] == 0 and config.get("city") >= q['city']:
                rquest = q
        elif esc["level"] >= q['escalation'] and config.get("city") >= q['city']:
            rquest = q


    if not bool(rquest):
        escalated = [e for e in escalated if e is not esc]
        config.write("escalated", escalated)

    if bool(rquest):
        rquest["name"] = quest_name

    return rquest


def get_quests(n: int):
    """
    Get n random quest from the quest folder
    """
    done = config.get("done")
    quests =  [f[:-5] for f in listdir(QUEST_PATH) if isfile(join(QUEST_PATH, f))]

    # File already done quests
    quests = [quest for quest in quests if quest not in done]

    if len(quests) <= 0:
        return []

    selected_quests = []

    for i in range(n + 1):
        if i > len(quests):
            break 

        rng = random.randrange(len(quests))
        selected_quests.append(quests[rng])

        del quests[rng]

    return selected_quests


def get_full_quests(n: int):
    """
    Get a list of random quests with full description
    """
    quests = get_quests(n)

    return [read_quest(q) for q in quests]


def mark_as_done(quest_name: str):
    """
    Save quest as done in the config file
    """
    done = config.get("done")
    esc = config.get_escalation(quest_name)

    if quest_name not in done:
        done.append(quest_name)
        config.write("done", done)

    if bool(esc):
        escalated = config.get("escalated")

        escalated = [e for e in escalated if e["name"] != quest_name]    
        config.write("escalated", escalated)


def escalate_quests():
    """
    Add escalation level to unselected quests
    """
    escalated = config.get("escalated")

    for q in escalated:
        q["level"] += 1

    config.write("escalated", escalated)

    calc_city_level()


def escalate_add(quest_name: str):
    """
    Add quest to list of unselected quests
    """
    escalaion = config.get("escalated")
    quest = config.get_escalation(quest_name)

    if quest not in escalaion:
        escalaion.append({"name": quest_name, "level": 0})
        
    config.write("escalated", escalaion)


def calc_city_level():
    """
    Calculate current city level
    """
    escalation = config.get("escalated")

    level = 0
    count = 0

    for esc in escalation:
        level += esc['level']
        count += 1

    if level == 0:
        config.write("city", 0)
        return 

    config.write("city", round(level / count))
