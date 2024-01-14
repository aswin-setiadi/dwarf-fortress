from char import Character
from skills import Skills


def print_skill_table(chars: list[Character]):
    names = [f"|{x.name.split()[0]:<10}" for x in chars]
    namestr = "".join(names)
    for skill in Skills:
        if skill.name == "Brewer":
            print("Orderlies".ljust(19, "#") + namestr)
        elif skill.name == "Bowyer":
            print("Crafting".ljust(19, "#") + namestr)
        elif skill.name == "Discipline":
            print("Military".ljust(19, "#") + namestr)
        elif skill.name == "Appraiser":
            print("Broker".ljust(19, "#") + namestr)
        elif skill.name == "Organizer":
            print("Manager/ ExpeditionLeader".ljust(19, "#") + namestr)
        elif skill.name == "Diagnoser":
            print("CMD".ljust(19, "#") + namestr)
        elif skill.name == "BoneDoctor":
            print("Doctor".ljust(19, "#") + namestr)
        elif skill.name == "RecordKeeper":
            print("BookKeeper".ljust(19, "#") + namestr)
        elif skill.name == "Comedian":
            print("SocialSkills".ljust(19, "#") + namestr)
        elif skill.name == "Concentration":
            print("Misc.".ljust(19, "#") + namestr)
        l: list[str] = []
        for char in chars:
            if skill in char.skills.keys():
                t = char.skills[skill]
                if t[1]:
                    tmp = f"{t[0]} T {t[2]}"
                else:
                    tmp = f"{t[0]} F {t[2]}"
                tmp = f"{tmp:<10}"
            else:
                tmp = f"None".ljust(10)
            l.append(tmp)
        s = "|".join(l)
        print(f"{skill:<19}= {s}")
