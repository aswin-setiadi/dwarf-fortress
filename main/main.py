import logging

from char import Character
from roles import Roles
from skills import Skills
from stats import (
    Goals,
    AttributeType as AT,
    Quality,
)

# logging.basicConfig(filename="char.log", filemode="a", level=logging.INFO)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def instantiate_char0() -> Character:
    char = Character(
        name="Kubuk(F) Fordportals", gender="female", goals={Goals.START_A_FAMILY}
    )
    char.set_toughness(AT.b1)
    char.set_willpower(AT.g3)
    char.set_kinesthesic_sense(AT.g2)
    char.set_creativity(AT.b2)
    char.set_intuition(AT.b2)
    # facets
    char.set_anxiety_propensity(Quality.Low)
    char.set_hate_propensity(Quality.Low)
    char.set_trust(Quality.High)
    char.set_cheer_propensity(Quality.Low)
    char.set_excitement_seeking(Quality.High)
    char.set_humor(Quality.High)
    char.set_thoughtlessness(Quality.High)
    char.set_emotionally_obsessive(Quality.High)
    char.set_love_propensity(Quality.High)
    char.set_stress_vulnerability(Quality.Low)
    char.set_confidence(Quality.Low)
    char.set_gratitude(Quality.High)
    char.set_immodesty(Quality.High)
    # beliefs
    char.set_craftsmanship(Quality.Highest)
    char.set_law(Quality.VeryHigh)
    char.set_loyalty(Quality.VeryHigh)
    char.set_family(Quality.VeryHigh)
    char.set_friendship(Quality.VeryHigh)
    char.set_artwork(Quality.VeryHigh)
    char.set_skill_belief(Quality.VeryHigh)
    char.set_hard_work(Quality.VeryHigh)
    char.set_fairness(Quality.High)
    char.set_cooperation(Quality.High)
    char.set_merriment(Quality.High)
    char.set_martial_prowess(Quality.High)
    char.set_leisure_time(Quality.High)
    char.set_commerce(Quality.High)
    char.set_knowledge(Quality.High)
    char.set_nature(Quality.Low)
    char.set_truth(Quality.Lowest)
    char.set_harmony(Quality.High)
    return char


def instantiate_char1() -> Character:
    char = Character(
        name="Rigoth Paddleblazes", gender="male", goals={Goals.CRAFT_A_MASTERWORK}
    )
    char.set_disease_resistance(AT.g3)
    char.set_recuperation(AT.g3)
    char.set_strength(AT.g2)
    char.set_endurance(AT.b1)
    char.set_toughness(AT.b2)

    char.set_focus(AT.g2)
    char.set_linguistic_ability(AT.b1)
    char.set_creativity(AT.b2)
    char.set_musical_ability(AT.b2)
    char.set_patience(AT.b2)
    # facets
    char.set_perfectionist(Quality.VeryLow)
    char.set_greed(Quality.VeryHigh)
    char.set_singleminded(Quality.VeryHigh)
    char.set_immodesty(Quality.VeryHigh)
    char.set_hate_propensity(Quality.Low)
    char.set_emotionally_obsessive(Quality.High)
    char.set_altruism(Quality.Low)
    char.set_thoughtlessness(Quality.Low)
    char.set_gregariousness(Quality.Low)
    char.set_activity_level(Quality.Low)
    char.set_perseverance(Quality.Low)
    char.set_ambition(Quality.Low)
    char.set_anxiety_propensity(Quality.Low)
    char.set_hate_propensity(Quality.Low)
    char.set_trust(Quality.High)
    char.set_cheer_propensity(Quality.Low)
    char.set_excitement_seeking(Quality.High)
    char.set_humor(Quality.High)
    char.set_vengeful(Quality.Low)
    char.set_envy_propensity(Quality.High)
    char.set_abstract_inclined(Quality.High)
    char.set_gratitude(Quality.High)

    # beliefs
    char.set_craftsmanship(Quality.Highest)
    char.set_law(Quality.VeryHigh)
    char.set_loyalty(Quality.VeryHigh)
    char.set_family(Quality.VeryHigh)
    char.set_friendship(Quality.VeryHigh)
    char.set_truth(Quality.VeryHigh)
    char.set_artwork(Quality.VeryHigh)
    char.set_skill_belief(Quality.VeryHigh)
    char.set_hard_work(Quality.VeryHigh)
    char.set_fairness(Quality.High)
    char.set_merriment(Quality.High)

    char.set_martial_prowess(Quality.High)
    char.set_leisure_time(Quality.High)

    char.set_commerce(Quality.High)
    char.set_nature(Quality.Low)
    char.set_cooperation(Quality.Neutral)
    char.set_knowledge(Quality.Neutral)
    return char


def instantiate_char2() -> Character:
    char = Character(
        name="Kosoth Rockchewed",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    char.set_disease_resistance(AT.g1)
    char.set_musical_ability(AT.b1)
    char.set_patience(AT.b2)
    char.set_analytical_ability(AT.b2)
    char.set_memory(AT.b2)
    # facets
    char.set_anxiety_propensity(Quality.VeryHigh)
    char.set_curious(Quality.High)
    char.set_dutifulness(Quality.High)
    char.set_bravery(Quality.Low)
    char.set_emotionally_obsessive(Quality.Low)
    char.set_gregariousness(Quality.Low)
    char.set_thoughtlessness(Quality.Low)
    char.set_disdain_advice(Quality.High)
    char.set_orderliness(Quality.High)
    char.set_greed(Quality.High)

    # beliefs
    char.set_craftsmanship(Quality.Highest)
    char.set_law(Quality.VeryHigh)
    char.set_loyalty(Quality.VeryHigh)
    char.set_family(Quality.VeryHigh)
    char.set_friendship(Quality.VeryHigh)
    char.set_truth(Quality.VeryHigh)
    char.set_artwork(Quality.VeryHigh)
    char.set_skill_belief(Quality.VeryHigh)
    char.set_fairness(Quality.High)
    char.set_cooperation(Quality.High)
    char.set_merriment(Quality.High)

    char.set_martial_prowess(Quality.High)
    char.set_leisure_time(Quality.High)
    char.set_commerce(Quality.High)
    char.set_knowledge(Quality.High)
    char.set_nature(Quality.Low)
    char.set_peace(Quality.VeryHigh)
    char.set_hard_work(Quality.High)

    return char


def instantiate_char3() -> Character:
    char = Character(
        name="Urist(S) Cryptfortress", gender="male", goals={Goals.MASTER_A_SKILL}
    )
    char.set_toughness(AT.b1)
    char.set_spatial_sense(AT.g4)
    char.set_intuition(AT.g2)
    char.set_social_awareness(AT.g1)
    char.set_creativity(AT.g1)
    char.set_focus(AT.b1)
    char.set_kinesthesic_sense(AT.b1)

    # facets
    char.set_anger_propensity(Quality.VeryLow)
    char.set_emotionally_obsessive(Quality.VeryLow)
    char.set_cheer_propensity(Quality.VeryHigh)
    char.set_dutifulness(Quality.High)
    char.set_imagination(Quality.Low)
    char.set_stress_vulnerability(Quality.High)
    char.set_hate_propensity(Quality.High)
    char.set_disdain_advice(Quality.High)
    char.set_trust(Quality.Low)
    char.set_excitement_seeking(Quality.Low)
    char.set_immoderation(Quality.High)
    char.set_discord(Quality.Low)

    # beliefs
    char.set_craftsmanship(Quality.Neutral)
    char.set_law(Quality.VeryHigh)
    char.set_loyalty(Quality.VeryHigh)
    char.set_family(Quality.VeryHigh)
    char.set_friendship(Quality.VeryHigh)
    char.set_truth(Quality.VeryHigh)
    char.set_artwork(Quality.VeryHigh)
    char.set_skill_belief(Quality.VeryHigh)
    char.set_hard_work(Quality.VeryHigh)
    char.set_fairness(Quality.High)
    char.set_cooperation(Quality.High)
    char.set_merriment(Quality.High)
    char.set_martial_prowess(Quality.High)
    char.set_leisure_time(Quality.High)

    char.set_commerce(Quality.High)
    char.set_knowledge(Quality.High)
    char.set_nature(Quality.Low)
    char.set_power(Quality.High)

    return char


def instantiate_char4() -> Character:
    char = Character(
        name="Cilob Lettertrails", gender="female", goals={Goals.CRAFT_A_MASTERWORK}
    )
    char.set_recuperation(AT.b1)
    char.set_linguistic_ability(AT.g3)
    char.set_willpower(AT.b1)
    char.set_focus(AT.b2)
    # facets
    char.set_vengeful(Quality.Lowest)
    char.set_politeness(Quality.VeryLow)
    char.set_violent(Quality.High)
    char.set_love_propensity(Quality.Low)
    char.set_humor(Quality.High)
    char.set_bashful(Quality.High)
    char.set_altruism(Quality.High)
    char.set_cheer_propensity(Quality.High)
    char.set_disdain_advice(Quality.High)
    char.set_cruelty(Quality.High)

    # beliefs
    char.set_craftsmanship(Quality.Highest)
    char.set_law(Quality.VeryHigh)
    char.set_loyalty(Quality.VeryHigh)
    char.set_family(Quality.VeryHigh)
    char.set_friendship(Quality.VeryHigh)
    char.set_truth(Quality.VeryHigh)
    char.set_artwork(Quality.VeryHigh)
    char.set_skill_belief(Quality.VeryHigh)
    char.set_hard_work(Quality.VeryHigh)
    char.set_fairness(Quality.High)
    char.set_cooperation(Quality.High)
    char.set_merriment(Quality.High)
    char.set_leisure_time(Quality.High)
    char.set_commerce(Quality.High)
    char.set_knowledge(Quality.High)
    char.set_nature(Quality.Low)
    char.set_martial_prowess(Quality.Neutral)
    return char


def instantiate_char5() -> Character:
    char = Character(
        name="Sazir Knightgranite",
        gender="male",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    char.set_spatial_sense(AT.g3)
    char.set_musical_ability(AT.g2)
    char.set_linguistic_ability(AT.b2)
    # facets
    char.set_closeminded(Quality.Lowest)
    char.set_humor(Quality.VeryHigh)
    char.set_assertiveness(Quality.High)
    char.set_altruism(Quality.Low)
    char.set_disdain_advice(Quality.Low)
    char.set_wastefulness(Quality.Low)
    char.set_depression_propensity(Quality.Low)
    char.set_thoughtlessness(Quality.High)
    char.set_greed(Quality.High)
    char.set_stress_vulnerability(Quality.Low)

    # beliefs
    char.set_craftsmanship(Quality.Highest)
    char.set_law(Quality.VeryHigh)
    char.set_loyalty(Quality.VeryHigh)
    char.set_family(Quality.VeryHigh)
    char.set_friendship(Quality.VeryHigh)
    char.set_truth(Quality.VeryHigh)
    char.set_artwork(Quality.VeryHigh)
    char.set_skill_belief(Quality.VeryHigh)
    char.set_hard_work(Quality.VeryHigh)
    char.set_fairness(Quality.High)
    char.set_cooperation(Quality.High)
    char.set_merriment(Quality.High)
    char.set_martial_prowess(Quality.High)
    char.set_leisure_time(Quality.High)
    char.set_commerce(Quality.High)
    char.set_knowledge(Quality.High)
    char.set_nature(Quality.Low)
    char.set_harmony(Quality.Low)
    return char


def instantiate_char6() -> Character:
    char = Character(
        name="Sigun Goldlesson", gender="male", goals={Goals.CRAFT_A_MASTERWORK}
    )
    char.set_toughness(AT.b1)
    char.set_analytical_ability(AT.g2)
    char.set_intuition(AT.g2)
    char.set_patience(AT.g1)
    char.set_willpower(AT.g1)
    char.set_memory(AT.g1)
    char.set_creativity(AT.g1)
    char.set_spatial_sense(AT.g1)
    char.set_kinesthesic_sense(AT.b1)
    char.set_social_awareness(AT.b1)

    # facets
    char.set_vanity(Quality.VeryLow)
    char.set_thoughtlessness(Quality.VeryLow)
    char.set_ambition(Quality.Low)
    char.set_lust_propensity(Quality.High)
    char.set_anger_propensity(Quality.Low)
    char.set_art_inclined(Quality.Low)
    char.set_perfectionist(Quality.High)
    char.set_envy_propensity(Quality.High)
    char.set_stress_vulnerability(Quality.Low)
    char.set_tolerant(Quality.High)
    char.set_confidence(Quality.High)

    # beliefs
    char.set_craftsmanship(Quality.Highest)
    char.set_law(Quality.VeryHigh)
    char.set_loyalty(Quality.Neutral)
    char.set_family(Quality.VeryHigh)
    char.set_friendship(Quality.VeryHigh)
    char.set_truth(Quality.VeryHigh)
    char.set_artwork(Quality.VeryHigh)
    char.set_skill_belief(Quality.Low)
    char.set_hard_work(Quality.VeryHigh)
    char.set_fairness(Quality.High)
    char.set_cooperation(Quality.High)
    char.set_merriment(Quality.High)
    char.set_martial_prowess(Quality.High)
    char.set_leisure_time(Quality.High)
    char.set_commerce(Quality.High)
    char.set_knowledge(Quality.High)
    char.set_nature(Quality.Low)
    char.set_stoicism(Quality.Lowest)

    return char


def instantiate_char7() -> Character:
    char = Character(
        name="Degel Coveredpapers", gender="male", goals={Goals.CRAFT_A_MASTERWORK}
    )
    char.set_disease_resistance(AT.g3)
    char.set_strength(AT.g3)
    char.set_endurance(AT.b1)

    char.set_willpower(AT.g3)
    char.set_kinesthesic_sense(AT.g1)
    char.set_social_awareness(AT.b1)
    char.set_empath(AT.b1)
    char.set_focus(AT.b2)

    char.set_bravery(Quality.Low)
    char.set_stress_vulnerability(Quality.High)

    char.set_martial_prowess(Quality.VeryHigh)
    char.set_tranquility(Quality.High)
    char.set_romance(Quality.Low)
    char.set_truth(Quality.High)
    return char


def instantiate_char8() -> Character:
    char = Character(
        name="Urdim Pillarwhims",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    char.set_endurance(AT.g2)
    char.set_recuperation(AT.g1)
    char.set_disease_resistance(AT.g1)

    char.set_patience(AT.g3)
    char.set_analytical_ability(AT.g1)
    char.set_kinesthesic_sense(AT.g1)
    char.set_creativity(AT.b1)
    char.set_intuition(AT.b2)
    char.set_linguistic_ability(AT.b2)
    char.set_willpower(AT.b2)
    char.set_privacy(Quality.VeryHigh)
    char.set_bravery(Quality.Low)

    char.set_craftsmanship(Quality.Low)
    char.set_stoicism(Quality.High)
    return char


def instantiate_char9() -> Character:
    char = Character(
        name="Kogan Channelequal",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    char.set_toughness(AT.g2)
    char.set_recuperation(AT.g1)
    char.set_agility(AT.b2)

    char.set_willpower(AT.g3)
    char.set_musical_ability(AT.g3)
    char.set_social_awareness(AT.g1)
    char.set_creativity(AT.b1)
    char.set_analytical_ability(AT.b1)
    char.set_memory(AT.b2)

    char.set_stress_vulnerability(Quality.Low)
    char.set_confidence(Quality.Low)

    char.set_introspection(Quality.High)
    char.set_truth(Quality.High)
    char.set_merriment(Quality.Low)
    char.set_family(Quality.Neutral)
    return char


def instantiate_char10() -> Character:
    char = Character(
        name="Degel Coveredpapers", gender="male", goals={Goals.CRAFT_A_MASTERWORK}
    )
    return char


def instantiate_char11() -> Character:
    char = Character(
        name="Degel Coveredpapers", gender="male", goals={Goals.CRAFT_A_MASTERWORK}
    )
    return char


def instantiate_char12() -> Character:
    char = Character(
        name="Degel Coveredpapers", gender="male", goals={Goals.CRAFT_A_MASTERWORK}
    )
    return char


def instantiate_chartemplate() -> Character:
    char = Character(name="", gender="", goals={})
    return char


def print_skill_table(chars: list[Character]):
    for char in chars:
        print(f"{char.name}={char.goals}")
        char.add_skills()
    names = [f"|{x.name.split()[0]:<11}".ljust(8) for x in chars]
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


def main():
    chars: list[Character] = []
    # chars.append(instantiate_char0())
    # chars.append(instantiate_char1())
    # chars.append(instantiate_char2())
    # chars.append(instantiate_char3())
    # chars.append(instantiate_char4())
    # chars.append(instantiate_char5())
    # chars.append(instantiate_char6())
    chars = [instantiate_char7(), instantiate_char8(), instantiate_char9()]
    print_skill_table(chars)

    # need engraver
    skill_assignment = {
        "Kubuk": {
            "skills": [
                (Skills.RecordKeeper, 2),
                (Skills.Fisherdwarf, 2),
                (Skills.WoodCutter, 2),
                (Skills.WoundDresser, 2),
                (Skills.Suturer, 2),
            ],
            "roles": [Roles.BookKeeper, "WoodCutter", "Fishing", "Performer"],
        },
        "Rigoth": {
            "skills": [
                (Skills.ArmorUser, 2),
                (Skills.Fighter, 2),
                (Skills.Dodger, 2),
                (Skills.Tactician, 1),
                (Skills.Leader, 1),
                (Skills.StoneCarver, 2),
            ],
            "roles": [Roles.MilitaryLeader, "Miner"],
        },
        "Kosoth": {
            "skills": [
                (Skills.Brewer, 2),
                (Skills.Thresher, 2),
                (Skills.Mason, 3),
                (Skills.Bowyer, 3),
            ],
            "roles": [],
        },
        "Urist": {
            "skills": [
                (Skills.Appraiser, 2),
                (Skills.JudgeOfIntent, 2),
                (Skills.Negotiator, 2),
                (Skills.Persuader, 2),
                (Skills.Weaver, 2),
            ],
            "roles": [Roles.Broker, "Hauler", "TavernKeeper"],
        },
        "Cilob": {
            "skills": [
                (Skills.Diagnoser, 3),
                (Skills.Planter, 3),
                (Skills.Cook, 2),
                (Skills.StoneCrafter, 2),
            ],
            "roles": [Roles.ChiefMedicalDoctor],
        },
        "Sazir": {
            "skills": [
                (Skills.FishCleaner, 2),
                (Skills.WeaponSmith, 2),
                (Skills.WoodBurner, 2),
                (Skills.BoneDoctor, 2),
                (Skills.Surgeon, 2),
            ],
            "roles": [],
        },
        "Sigun": {
            "skills": [
                (Skills.Organizer, 2),
                (Skills.Consoler, 2),
                (Skills.Pacifier, 2),
                (Skills.Carpenter, 2),
                (Skills.AnimalTrainer, 2),
            ],
            "roles": [Roles.Manager, Roles.ExpeditionLeader],
        },
        "Degel": {
            "skills": [(Skills.ArmorSmith, 2), (Skills.FurnaceOperator, 0)],
            "roles": [],
        },
        "Urdim": {"Skills": [(Skills.GemCutter, 3), "GemSetter,3"]},
        "Kogan": {"Skills": ["TemplePerformer (music g3)", "GemSetter,3"]},
    }


if __name__ == "__main__":
    main()
