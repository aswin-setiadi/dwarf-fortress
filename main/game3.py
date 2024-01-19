import logging

from char import Character
import char_gen3 as cg
from roles import Roles
from skills import Skills

# from stats import (
#     Goals,
#     AttributeType as AT,
#     Quality as qty,
# )
from utils import print_skill_table

logging.basicConfig(
    filename="char.log",
    filemode="a",
    format="%(asctime)s %(module)s %(levelname)s %(message)s",
    level=logging.INFO,
)
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    chars: list[Character] = []
    chars.append(cg.char1())
    chars.append(cg.char2())
    chars.append(cg.char3())
    chars.append(cg.char4())
    chars.append(cg.char5())
    chars.append(cg.char6())
    chars.append(cg.char7())
    chars.append(cg.char8())
    chars.append(cg.char9())
    chars.append(cg.char10())
    chars.append(cg.char11())
    chars.append(cg.char12())
    chars.append(cg.char13())
    chars.append(cg.char14())
    chars.append(cg.char15())
    chars.append(cg.char16())
    chars.append(cg.char17())
    for char in chars:
        print(f"{char.name}={char.goals}")
        char.add_skills()
    # print_skill_table(chars, skills=[Skills.Appraiser, Skills.Organizer])
    print_skill_table(chars)
    armies = {
        "sword": ["Zulban", "LokumLet", "UrdimRith"],
        "hammer": [],
        "crossbow": [],
    }

    roles = {
        "Atis": [
            Skills.StoneCrafter,
            Skills.BoneDoctor,
            Skills.Surgeon,
        ],  # 4 3 3
        "Dakost": [
            Skills.Carpenter,
            Skills.Planter,
            Skills.Brewer,
            "animaltrainerrole",
        ],  # 4 3 3
        "Kogsak": [
            Skills.GemCutter,
            Skills.Cook,
            Skills.RecordKeeper,
        ],  # 5 3 2 herbalist
        "Shorast": [
            Skills.StoneCarver,
            Roles.Manager,
            Roles.ExpeditionLeader,
        ],  # 4 2 2 2
        "UristD": [
            Skills.Engraver,
            Skills.Suturer,
            Skills.WoundDresser,
        ],  # 5 2 3 fisherdwarf
        "UristE": [
            Skills.Diagnoser,
            Skills.StoneCutter,
            Roles.Broker,
            "TavernKeeper",
        ],  # 2 2 2 2 2
        "Zulban": ["soldier"],  # sword armor fighter dodger leader
        "LokumLet": [
            "Papermaker2",
            "Liar2",
            "Dancer2",
            "Musician2",
            "StringedInstrumentalist2",
            Skills.StoneCarver,
            "TemplePerformer",
        ],
        "UnibKeskal": [Skills.WeaponSmith, "Dancer2", Skills.StoneCutter],  # 10
        "UrdimRith": [
            "TavernPerformerLegendSpeakerAndPoet",
            Skills.WoodCutter,  # 2
            Skills.Spinner,  # 2
            "Teacher4",
            Skills.ArmorSmith,
        ],
        "KosothAva": [
            "gemset10",
            "miner5",
            "cheesemaker1",
            "siegeEng1",
            "papermaker1",
            "axe,shield,armor,discipline,observer,fighter,dodger=3",
        ],
        "likotIlral": [
            "engraver5",
            "mason5",
            "tanner5",
            "stonecutter5",
            "stonecarver5",
            "spear,shield,armor,discipline,observer,fighter,dodger3",
            "dancer3",
            "rider2",
            "climber3",
            "swimmer1",
        ],
        "mistemErith": [
            "surgeon1",
            "recordkeeper1",
            "persuader3",
            "musician3",
            "percussionist2",
        ],
        "monomTekkud": [
            "glassmaker6",
            "persuader,judgeofIntent,convers,comedian4",
            "negotiate,liar,intimidator,flatterer,consoler,pacifier3",
            "dancer3",
        ],
        "mosusSigun": [
            "clothier1",
            "appraiser,organizer,recordk1",
            "spear,shield,armor,discipline,observer,fighter,dodger1",
            "persuader,pacifier3",
            "liar,intimidator,converse,comedian,flatterer2",
            "negotiate,JoI,consoler1",
            "swimmer,climber,dancer1",
        ],
        "thikutIsha": [
            "bowyer6",
            "mason4",
            "weaver1",
            "flatterer3",
            "JoI,intimidate,converse,comedian,consoler,pacifier2",
            "persuader,negotiate,liar1",
            "dancer,musician,keyboardist2",
            "swimmer1",
        ],
        "tulonShol": ["miner1", "bonecarver1", "dancer2", "swimmer1"],
    }
    needs = {
        "AtisAth": ["fight", "craft", "martialtrain"],
        "Dakost": ["fight"],
        "Kogsak": ["fight"],
        "Shorast": ["fight", "martialtrain"],
        "uristD": ["craftobj!", "fight"],
        "uristE": ["fight"],
        "zulbanKubul": ["fight", "martialtrain"],
        "lokumLet": [],
        "unibKeskal": ["fight"],
        "urdimRith": ["praytomafi!", "learnsomething"],
        "kosothAva": [],
        "likotIlral": [],
        "mistemErith": [],
        "monomTekkud": [],
        "MosusSigun": ["craft object"],
        "thikutIsha": [],
        "tulonShol": [],
    }


if __name__ == "__main__":
    main()
