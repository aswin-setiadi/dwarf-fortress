from enum import Enum

from main.skills import BodyAttributes, Skills, SoulAttributes


class Roles(Enum):
    ChiefMedicalDoctor = {Skills.Diagnoser}
    Manager = {Skills.Organizer, Skills.Consoler, Skills.Pacifier}
    Broker = {Skills.JudgeOfIntent, Skills.Appraiser, Skills.Negotiator}
    BookKeeper = {Skills.RecordKeeper}
    ExpeditionLeader = {Skills.Consoler, Skills.Pacifier}
    MillitaryLeader = {
        Skills.Leader,
        Skills.Tactician,
        Skills.ArmorUser,
        Skills.Fighter,
        Skills.Dodger,
    }
    Crafter = {
        Skills.Cook,
        Skills.Bowyer,
        Skills.WeaponSmith,
        Skills.GemCutter,
        Skills.Carpenter,
        Skills.StoneCarver,
        Skills.StoneCrafter,
        Skills.WoodCrafter,
        Skills.Engraver,
        Skills.Mason,
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
    res = Roles.get_role_attributes(Roles.MillitaryLeader)
    print(res)
