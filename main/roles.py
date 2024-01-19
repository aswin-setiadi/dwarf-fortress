from enum import Enum

from skills import BodyAttributes, Skills, SoulAttributes


class Roles(Enum):
    # do everything in beginning, depend on diagnose skill
    ChiefMedicalDoctor = {Skills.Diagnoser}
    Manager = {Skills.Organizer, Skills.Consoler, Skills.Pacifier}
    Broker = {Skills.JudgeOfIntent, Skills.Appraiser, Skills.Negotiator}
    BookKeeper = {Skills.RecordKeeper}
    # Expedition Leader/ Mayor at 50 pop.
    ExpeditionLeader = {
        Skills.Consoler,
        Skills.Pacifier,
    }
    MilitaryLeader = {
        Skills.ArmorUser,
        Skills.Dodger,
        Skills.Fighter,
        Skills.Leader,
        Skills.Tactician,
    }
    Crafter = {
        Skills.Bowyer,
        Skills.Carpenter,
        Skills.Cook,
        Skills.Engraver,
        Skills.GemCutter,
        Skills.Mason,
        Skills.StoneCarver,
        Skills.StoneCrafter,
        Skills.WeaponSmith,
        Skills.WoodCrafter,
    }
    Doctor = {Skills.BoneDoctor, Skills.Surgeon}

    @staticmethod
    def get_role_attributes(role: "Roles") -> set[BodyAttributes | SoulAttributes]:
        res: set[BodyAttributes | SoulAttributes] = set()
        for skill in role.value:
            _ = {x for x in skill.value.attributes.keys()}
            res = res.union(_)
        return res


if __name__ == "__main__":
    # print(Roles.Broker.value)  # will print tuple of Skills for Broker
    # print(list(Roles))
    res = Roles.get_role_attributes(Roles.MilitaryLeader)
    print(res)
