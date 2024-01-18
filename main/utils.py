from typing import Iterable

from char import Character
from skills import Skills


def print_skill_table(chars: list[Character], skills: Iterable[Skills] = []):
    names = [f"|{x.name.split()[0]:<10}" for x in chars]
    namestr = "".join(names)
    if not skills:
        skills = Skills
    for skill in skills:
        if skill.name == "Brewer":
            print("".ljust(50, "#"))
            print("Orderlies".ljust(20, " ") + namestr)
        elif skill.name == "Bowyer":
            print("".ljust(50, "#"))
            print("Crafting".ljust(20, " ") + namestr)
        elif skill.name == "Discipline":
            print("".ljust(50, "#"))
            print("Military".ljust(20, " ") + namestr)
        elif skill.name == "Appraiser":
            print("".ljust(50, "#"))
            print("Broker".ljust(20, " ") + namestr)
        elif skill.name == "Organizer":
            print("".ljust(50, "#"))
            print("Mngr/ExpLdr".ljust(20, " ") + namestr)
        elif skill.name == "Diagnoser":
            print("".ljust(50, "#"))
            print("CMD".ljust(20, " ") + namestr)
        elif skill.name == "BoneDoctor":
            print("".ljust(50, "#"))
            print("Doctor".ljust(20, " ") + namestr)
        elif skill.name == "RecordKeeper":
            print("".ljust(50, "#"))
            print("BookKeeper".ljust(20, " ") + namestr)
        elif skill.name == "Comedian":
            print("".ljust(50, "#"))
            print("SocialSkills".ljust(20, " ") + namestr)
        elif skill.name == "Concentration":
            print("".ljust(50, "#"))
            print("Misc.".ljust(20, " ") + namestr)
        l: list[str] = []
        for char in chars:
            if skill in char.skills.keys():
                t = char.skills[skill]
                if t[1]:
                    tmp = f"{t[0]} T {t[2]}"
                else:
                    tmp = f"{t[0]} F {t[2]}"
                tmp = f"|{tmp:<10}"
            else:
                none = "None"
                tmp = f"|{none:<10}"
            l.append(tmp)
        s = "".join(l)
        print(f"{skill.name:<20}{s}")
