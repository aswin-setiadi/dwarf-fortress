import logging

from char import Character
from roles import Roles
from skills import Skills
from stats import (
    Goals,
    AttributeType as AT,
    Quality,
)
from utils import print_skill_table

logging.basicConfig(
    filename="char.log",
    filemode="a",
    format="%(asctime)s %(module)s %(levelname)s %(message)s",
    level=logging.INFO,
)
# logging.basicConfig(level=logging.INFO)
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
        name="Kadol Bladerags", gender="male", goals={Goals.MASTER_A_SKILL}
    )
    char.set_toughness(AT.g2)

    char.set_intuition(AT.g1)
    char.set_patience(AT.b2)

    char.set_altruism(Quality.Low)
    char.set_anger_propensity(Quality.Low)
    char.set_friendliness(Quality.High)
    char.set_hate_propensity(Quality.High)
    char.set_imagination(Quality.Low)
    char.set_activity_level(Quality.High)
    char.set_gratitude(Quality.Low)

    return char


def instantiate_char11() -> Character:
    char = Character(
        name="Meng SystemHatchets", gender="female", goals={Goals.CRAFT_A_MASTERWORK}
    )
    char.set_toughness(AT.g1)
    char.set_endurance(AT.b1)
    char.set_recuperation(AT.b3)

    char.set_linguistic_ability(AT.g2)
    char.set_focus(AT.g1)
    char.set_analytical_ability(AT.g1)
    char.set_musical_ability(AT.b1)
    char.set_patience(AT.b2)

    char.set_humor(Quality.High)
    char.set_anxiety_propensity(Quality.High)
    char.set_friendliness(Quality.High)
    char.set_thoughtlessness(Quality.High)

    char.set_sacrifice(Quality.VeryLow)
    char.set_tranquility(Quality.Low)

    return char


def instantiate_char12() -> Character:
    char = Character(
        name="Rith Blamelesschamber",
        gender="male",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    char.set_endurance(AT.g3)
    char.set_recuperation(AT.b1)
    char.set_toughness(AT.b1)

    char.set_creativity(AT.g3)
    char.set_spatial_sense(AT.g3)
    char.set_focus(AT.g2)
    char.set_analytical_ability(AT.b1)
    char.set_willpower(AT.b2)
    char.set_empath(AT.b3)

    char.set_immoderation(Quality.VeryHigh)
    char.set_stress_vulnerability(Quality.Low)

    char.set_family(Quality.Lowest)
    return char


def instantiate_char13() -> Character:
    char = Character(
        name="Avuz Roadboarded", gender="female", goals={Goals.START_A_FAMILY}
    )
    char.set_agility(AT.g1)
    char.set_endurance(AT.b2)

    char.set_kinesthesic_sense(AT.g1)
    char.set_linguistic_ability(AT.g1)
    char.set_creativity(AT.b1)
    char.set_empath(AT.b2)
    char.set_memory(AT.b2)

    char.set_stress_vulnerability(Quality.Low)

    return char


def instantiate_char14() -> Character:
    char = Character(
        name="Edzul Salvestokes", gender="female", goals={Goals.MASTER_A_SKILL}
    )
    char.set_recuperation(AT.b1)

    char.set_creativity(AT.g2)
    char.set_spatial_sense(AT.b1)
    char.set_linguistic_ability(AT.b2)

    char.set_stress_vulnerability(Quality.High)

    return char


def instantiate_char15() -> Character:
    char = Character(
        name="Fath Swordpracticed",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    char.set_strength(AT.g1)

    char.set_kinesthesic_sense(AT.g1)
    char.set_memory(AT.g1)
    char.set_willpower(AT.b1)

    char.set_cheer_propensity(Quality.Low)
    char.set_excitement_seeking(Quality.Low)
    char.set_anxiety_propensity(Quality.High)
    char.set_stress_vulnerability(Quality.Low)
    char.set_immoderation(Quality.High)
    char.set_bravery(Quality.High)

    char.set_cunning(Quality.Low)
    char.set_craftsmanship(Quality.Low)
    return char


def instantiate_char16() -> Character:
    char = Character(
        name="Shorast Enjoyarmors", gender="female", goals={Goals.MASTER_A_SKILL}
    )
    char.set_intuition(AT.g3)
    char.set_musical_ability(AT.g1)
    char.set_willpower(AT.g1)
    char.set_anger_propensity(Quality.High)
    char.set_violent(Quality.High)

    char.set_perseverance_belief(Quality.High)
    char.set_tradition(Quality.Low)
    return char


def instantiate_char17() -> Character:
    char = Character(
        name="Zulban Kindnesscrafts",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    char.set_endurance(AT.g1)
    char.set_creativity(AT.g2)
    char.set_spatial_sense(AT.b1)
    char.set_patience(AT.b1)

    char.set_humor(Quality.Highest)
    char.set_stress_vulnerability(Quality.Low)
    char.set_anxiety_propensity(Quality.Low)

    char.set_perseverance_belief(Quality.VeryLow)
    char.set_family(Quality.VeryLow)
    char.set_fairness(Quality.Neutral)

    return char


def instantiate_char18() -> Character:
    char = Character(
        name="Zon Fanciedhelms", gender="female", goals={Goals.START_A_FAMILY}
    )
    char.set_strength(AT.g1)
    char.set_agility(AT.b1)

    char.set_linguistic_ability(AT.g2)
    char.set_musical_ability(AT.g2)
    char.set_willpower(AT.g1)
    char.set_patience(AT.b2)
    char.set_analytical_ability(AT.b2)

    char.set_stress_vulnerability(Quality.High)
    char.set_cheer_propensity(Quality.High)
    char.set_cruelty(Quality.Low)

    char.set_eloquence(Quality.Highest)
    char.set_martial_prowess(Quality.Low)
    char.set_tranquility(Quality.High)
    return char


def instantiate_char19() -> Character:
    char = Character(
        name="Meng Websaves", gender="female", goals={Goals.START_A_FAMILY}
    )
    char.set_agility(AT.g2)
    char.set_endurance(AT.g2)

    char.set_memory(AT.g1)
    char.set_kinesthesic_sense(AT.g1)
    char.set_patience(AT.g1)
    char.set_spatial_sense(AT.b2)
    char.set_analytical_ability(AT.b2)

    char.set_cruelty(Quality.VeryLow)
    char.set_excitement_seeking(Quality.VeryHigh)
    char.set_stress_vulnerability(Quality.Low)
    char.set_politeness(Quality.Low)
    char.set_bravery(Quality.Low)

    char.set_merriment(Quality.VeryHigh)
    return char


def instantiate_chartemplate() -> Character:
    char = Character(name="", gender="", goals={})
    return char


def main():
    chars: list[Character] = []
    # chars.append(instantiate_char0())
    # chars.append(instantiate_char1())
    # chars.append(instantiate_char2())
    # chars.append(instantiate_char3())
    # chars.append(instantiate_char4())
    # chars.append(instantiate_char5())
    # chars.append(instantiate_char6())
    # chars.append(instantiate_char7())
    # chars.append(instantiate_char8())
    # chars.append(instantiate_char9())
    # chars.append(instantiate_char10())
    # chars.append(instantiate_char11())
    # chars.append(instantiate_char12())
    # chars.append(instantiate_char13())
    # chars.append(instantiate_char14())
    # chars.append(instantiate_char15())
    chars.append(instantiate_char16())
    chars.append(instantiate_char17())
    chars.append(instantiate_char18())
    chars.append(instantiate_char19())
    # chars = [instantiate_char7(), instantiate_char8(), instantiate_char9()]
    for char in chars:
        print(f"{char.name}={char.goals}")
        char.add_skills()
    print_skill_table(chars, skills=[Skills.Appraiser, Skills.Organizer])
    # print_skill_table(chars)

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
            "roles": [
                Roles.BookKeeper,
                "WoodCutter",
                "Fishing",
            ],
            "goal": "family",
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
            "roles": [Roles.MilitaryLeader, "Miner1"],
        },
        "Kosoth": {
            "skills": [
                (Skills.Brewer, 2),
                (Skills.Thresher, 2),
                (Skills.Mason, 3),
                (Skills.Bowyer, 3),
            ],
            "roles": ["stonecutter"],
        },
        "Urist": {
            "skills": [
                (Skills.Appraiser, 2),
                (Skills.JudgeOfIntent, 2),
                (Skills.Negotiator, 2),
                (Skills.Persuader, 2),
                (Skills.Weaver, 2),
            ],
            "roles": [Roles.Broker, "Hauler1", "TavernKeeper"],
            "goal": "skill",
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
            "roles": ["Archer1"],
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
        "Urdim": {
            "skills": [(Skills.GemCutter, 3), "GemSetter,3"],
            "roles": ["Miner", "Militia"],
        },
        "Kogan": {
            "skills": ["Poet (music atb g3)"],
            "roles": ["hauler4", "TavernPerfomer"],
        },
        "Kadol": {
            "skills": [(Skills.StoneCrafter, 6), "Shearer 5"],
            "roles": ["Militia", "Miner3"],
            "goal": "skill",
        },
        "Meng": {"skills": ["Musician 12"], "roles": ["TemplePerformer", "Hauler5"]},
        "Rith": {
            "skills": ["Musician 12"],
            "roles": ["TavernPerformer", "Militia", "Miner4"],
        },
        "Avuz": {
            "skills": [
                (Skills.WeaponSmith, 13),
                (Skills.GemCutter, 7),
                ("armoruser,discipline,observer,fighter,biter,dodger", 4),
            ],
            "roles": [
                "Militia",
                "Miner5",
                "CompotentPoet-> xPerformer",
                "GemCutter",
                "WeaponSmith",
            ],
        },
        "Edzul": {
            "skills": [("Trapper", 13), ("Dyer", 5), ("Gelder", 3), ("Dancer", 3)],
            "roles": ["Dancer-> xPerformer", "hauler6", "Stonecutter"],
        },
        "Fath": {
            "skills": [],
            "roles": ["Militia", "miner8"],  # TODO
        },
        "Shorast": {
            "skills": [("Trapper", 6)],
            "roles": ["Miner2", "Militia"],
        },
        "Zulban": {
            "skills": [(Skills.GemCutter, 3), ("LyeMaker", 3)],
            "roles": ["Militia", "Miner7"],
        },
        "Zon": {
            "skills": [("Trapper", 10), ("Milker", 5)],
            "roles": ["nganggur", "miner"],
        },
        "MengOrs": {
            "skills": [],
            "roles": ["nganggur"],
        },
        "template": {
            "skills": [],
            "roles": [],
        },
    }

    armies = {
        "spear": ["Rigoth", "Kadol", "Shorast", "Urdim"],
        "Sword": ["Avuz", "Rith", "Zulban"],
        "crossbow": ["Sazir"],
    }
    miners = ["Fath", "Degel", "Meng", "Kogan"]


def game2():
    chars: list[Character] = []
    c0 = Character(
        name="Dodok Lolokshalig",
        gender="male",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    # body and soul attributes
    c0.set_creativity(AT.g3)
    c0.set_kinesthesic_sense(AT.g3)
    c0.set_willpower(AT.g1)
    c0.set_analytical_ability(AT.b1)
    c0.set_patience(AT.b2)
    # facets
    c0.set_bashful(Quality.VeryLow)
    c0.set_bravery(Quality.VeryLow)
    c0.set_depression_propensity(Quality.VeryHigh)
    c0.set_greed(Quality.Low)
    c0.set_wastefulness(Quality.Low)
    c0.set_politeness(Quality.Low)
    c0.set_immodesty(Quality.Low)
    c0.set_privacy(Quality.High)
    c0.set_discord(Quality.Low)
    c0.set_altruism(Quality.Low)
    c0.set_vengeful(Quality.Low)
    c0.set_confidence(Quality.High)
    c0.set_lust_propensity(Quality.High)

    # beliefs
    c0.set_hard_work(Quality.Lowest)
    c0.set_commerce(Quality.Low)
    c0.set_introspection(Quality.Low)
    chars.append(c0)

    c1 = Character(
        name="Eshtan Thuneninod",
        gender="male",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    c1.set_spatial_sense(AT.g2)
    c1.set_social_awareness(AT.g2)
    c1.set_intuition(AT.b1)

    c1.set_trust(Quality.VeryHigh)
    c1.set_humor(Quality.VeryLow)
    c1.set_ambition(Quality.VeryLow)
    c1.set_singleminded(Quality.High)
    c1.set_imagination(Quality.Low)
    c1.set_hopeful(Quality.High)
    c1.set_tolerant(Quality.Low)
    c1.set_activity_level(Quality.High)
    c1.set_privacy(Quality.Low)
    c1.set_perfectionist(Quality.Low)

    c1.set_knowledge(Quality.Low)
    c1.set_power(Quality.Low)

    chars.append(c1)

    c2 = Character(name="Momuz Othmorul", gender="male", goals={Goals.MASTER_A_SKILL})
    c2.set_strength(AT.g1)
    c2.set_toughness(AT.b1)
    c2.set_intuition(AT.g3)
    c2.set_focus(AT.g1)
    c2.set_linguistic_ability(AT.g1)
    c2.set_kinesthesic_sense(AT.b1)
    c2.set_patience(AT.b2)

    c2.set_gratitude(Quality.VeryHigh)
    c2.set_closeminded(Quality.VeryLow)
    c2.set_greed(Quality.Low)
    c2.set_orderliness(Quality.Low)
    c2.set_vanity(Quality.High)
    c2.set_singleminded(Quality.High)
    c2.set_imagination(Quality.High)
    c2.set_vengeful(Quality.Low)
    c2.set_immoderation(Quality.High)

    c2.set_harmony(Quality.Low)
    c2.set_competition(Quality.High)

    chars.append(c2)

    c3 = Character(
        name="Tobul Edosrigoth",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )

    c3.set_creativity(AT.g3)
    c3.set_willpower(AT.g2)
    c3.set_social_awareness(AT.b2)

    c3.set_humor(Quality.High)
    c3.set_altruism(Quality.VeryHigh)
    c3.set_cruelty(Quality.VeryHigh)
    c3.set_excitement_seeking(Quality.High)
    c3.set_anger_propensity(Quality.High)
    c3.set_gregariousness(Quality.Low)
    c3.set_activity_level(Quality.Low)
    c3.set_thoughtlessness(Quality.High)
    c3.set_cheer_propensity(Quality.Low)
    c3.set_gratitude(Quality.High)
    c3.set_greed(Quality.High)
    c3.set_lust_propensity(Quality.Low)
    c3.set_dutifulness(Quality.High)

    c3.set_commerce(Quality.Low)
    c3.set_stoicism(Quality.Low)
    c3.set_perseverance_belief(Quality.Low)
    c3.set_sacrifice(Quality.High)
    c3.set_power(Quality.Low)

    chars.append(c3)

    c4 = Character(
        name="Vucar Asteshkosoth", gender="female", goals={Goals.START_A_FAMILY}
    )
    c4.set_recuperation(AT.b1)
    c4.set_intuition(AT.g2)
    c4.set_kinesthesic_sense(AT.g2)
    c4.set_memory(AT.g1)
    c4.set_willpower(AT.g1)
    c4.set_focus(AT.b2)

    c4.set_politeness(Quality.VeryHigh)
    c4.set_singleminded(Quality.VeryHigh)
    c4.set_love_propensity(Quality.VeryHigh)
    c4.set_disdain_advice(Quality.Low)
    c4.set_assertiveness(Quality.High)
    c4.set_discord(Quality.Low)
    c4.set_ambition(Quality.High)
    c4.set_altruism(Quality.Low)
    c4.set_gregariousness(Quality.High)
    c4.set_lust_propensity(Quality.High)
    c4.set_imagination(Quality.Low)
    c4.set_curious(Quality.High)

    c4.set_cooperation(Quality.Low)
    chars.append(c4)

    c5 = Character(
        name="Dodok Okirbesmar", gender="female", goals={Goals.START_A_FAMILY}
    )
    c5.set_disease_resistance(AT.g1)
    c5.set_recuperation(AT.b1)

    c5.set_linguistic_ability(AT.g1)
    c5.set_musical_ability(AT.b2)
    c5.set_kinesthesic_sense(AT.b3)

    c5.set_hopeful(Quality.VeryHigh)
    c5.set_assertiveness(Quality.VeryLow)
    c5.set_emotionally_obsessive(Quality.High)
    c5.set_privacy(Quality.Low)
    c5.set_cheer_propensity(Quality.High)
    c5.set_pride(Quality.Low)
    c5.set_wastefulness(Quality.High)
    c5.set_perfectionist(Quality.Low)
    c5.set_dutifulness(Quality.High)
    c5.set_swayed_by_emotions(Quality.Low)
    c5.set_perseverance(Quality.High)
    c5.set_immodesty(Quality.High)
    c5.set_greed(Quality.High)
    c5.set_trust(Quality.High)

    c5.set_martial_prowess(Quality.VeryLow)
    c5.set_hard_work(Quality.Neutral)
    chars.append(c5)

    c6 = Character(
        name="Udib Keskalvathez", gender="female", goals={Goals.START_A_FAMILY}
    )
    c6.set_strength(AT.b1)
    c6.set_agility(AT.b1)
    c6.set_linguistic_ability(AT.g2)
    c6.set_kinesthesic_sense(AT.g1)
    c6.set_memory(AT.g1)
    c6.set_focus(AT.g1)
    c6.set_spatial_sense(AT.b1)
    c6.set_creativity(AT.b1)

    c6.set_lust_propensity(Quality.Highest)
    c6.set_disdain_advice(Quality.Highest)
    c6.set_stress_vulnerability(Quality.VeryLow)
    c6.set_anxiety_propensity(Quality.High)
    c6.set_greed(Quality.High)
    c6.set_ambition(Quality.High)
    c6.set_discord(Quality.High)
    c6.set_emotionally_obsessive(Quality.Low)
    c6.set_depression_propensity(Quality.Low)
    c6.set_hopeful(Quality.High)
    c6.set_anger_propensity(Quality.Low)
    c6.set_bravery(Quality.Low)
    c6.set_singleminded(Quality.Low)

    c6.set_nature(Quality.Neutral)
    chars.append(c6)

    c7 = Character(
        name="Athel Bomrekdesor", gender="female", goals={Goals.MASTER_A_SKILL}
    )
    c7.set_recuperation(AT.g1)
    c7.set_strength(AT.b2)
    c7.set_memory(AT.g2)
    c7.set_creativity(AT.b1)
    c7.set_spatial_sense(AT.b1)

    c7.set_cheer_propensity(Quality.VeryLow)
    c7.set_anxiety_propensity(Quality.Low)
    c7.set_perseverance(Quality.Low)
    c7.set_art_inclined(Quality.High)
    c7.set_singleminded(Quality.Low)
    c7.set_swayed_by_emotions(Quality.High)
    c7.set_love_propensity(Quality.Low)
    c7.set_imagination(Quality.Low)
    c7.set_depression_propensity(Quality.High)
    c7.set_trust(Quality.Low)
    c7.set_hate_propensity(Quality.High)
    c7.set_discord(Quality.High)
    c7.set_cruelty(Quality.Low)
    c7.set_greed(Quality.High)
    c7.set_immoderation(Quality.High)
    c7.set_humor(Quality.High)

    c7.set_sacrifice(Quality.High)
    c7.set_peace(Quality.High)

    chars.append(c7)

    c8 = Character(
        name="Logem Ducimtorad", gender="female", goals={Goals.START_A_FAMILY}
    )
    c8.set_recuperation(AT.g1)
    c8.set_disease_resistance(AT.b2)
    c8.set_creativity(AT.g3)
    c8.set_social_awareness(AT.g2)
    c8.set_musical_ability(AT.g1)
    c8.set_analytical_ability(AT.g1)
    c8.set_linguistic_ability(AT.g1)
    c8.set_kinesthesic_sense(AT.b1)
    c8.set_intuition(AT.b2)

    c8.set_trust(Quality.High)
    c8.set_swayed_by_emotions(Quality.High)
    c8.set_cruelty(Quality.Low)
    c8.set_envy_propensity(Quality.Low)
    c8.set_curious(Quality.High)
    c8.set_abstract_inclined(Quality.High)
    c8.set_disdain_advice(Quality.High)
    c8.set_altruism(Quality.Low)
    c8.set_vanity(Quality.Low)
    c8.set_ambition(Quality.Low)
    c8.set_politeness(Quality.Low)

    c8.set_loyalty(Quality.Neutral)
    c8.set_law(Quality.Neutral)
    c8.set_truth(Quality.Neutral)

    chars.append(c8)

    c9 = Character(name="Onul Megidnil", gender="male", goals={Goals.START_A_FAMILY})
    c9.set_agility(AT.g1)
    c9.set_disease_resistance(AT.b1)

    c9.set_creativity(AT.g3)
    c9.set_spatial_sense(AT.g3)
    c9.set_empath(AT.g2)
    c9.set_patience(AT.g1)
    c9.set_kinesthesic_sense(AT.b1)
    c9.set_willpower(AT.b1)
    c9.set_linguistic_ability(AT.b1)
    c9.set_memory(AT.b2)
    c9.set_focus(AT.b2)

    c9.set_orderliness(Quality.Highest)
    c9.set_lust_propensity(Quality.VeryLow)
    c9.set_altruism(Quality.Low)
    c9.set_anxiety_propensity(Quality.High)
    c9.set_vengeful(Quality.Low)
    c9.set_assertiveness(Quality.Low)
    c9.set_vanity(Quality.High)
    c9.set_discord(Quality.Low)
    c9.set_immodesty(Quality.Low)
    c9.set_cruelty(Quality.Low)

    c9.set_decorum(Quality.High)
    chars.append(c9)

    c10 = Character(
        name="Tekkud Igathlikot", gender="male", goals={Goals.MASTER_A_SKILL}
    )
    c10.set_agility(AT.b1)
    c10.set_recuperation(AT.b1)
    c10.set_linguistic_ability(AT.g3)
    c10.set_intuition(AT.g1)
    c10.set_social_awareness(AT.g1)
    c10.set_creativity(AT.b1)
    c10.set_kinesthesic_sense(AT.b2)

    c10.set_excitement_seeking(Quality.VeryHigh)
    c10.set_hate_propensity(Quality.VeryLow)
    c10.set_ambition(Quality.VeryLow)
    c10.set_discord(Quality.Low)
    c10.set_activity_level(Quality.High)
    c10.set_orderliness(Quality.High)
    c10.set_envy_propensity(Quality.Low)
    c10.set_confidence(Quality.High)
    c10.set_immoderation(Quality.High)
    c10.set_friendliness(Quality.Low)
    c10.set_imagination(Quality.High)
    c10.set_bravery(Quality.High)
    c10.set_gratitude(Quality.High)

    c10.set_tranquility(Quality.VeryHigh)
    c10.set_romance(Quality.VeryHigh)
    c10.set_craftsmanship(Quality.High)
    c10.set_truth(Quality.Neutral)
    chars.append(c10)
    c11 = Character(
        name="Datan Rerrasfikod",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    c11.set_disease_resistance(AT.g1)
    c11.set_recuperation(AT.b1)
    c11.set_analytical_ability(AT.g3)
    c11.set_patience(AT.b1)
    c11.set_empath(AT.b2)
    c11.set_intuition(AT.b3)

    c11.set_violent(Quality.VeryLow)
    c11.set_stress_vulnerability(Quality.VeryLow)
    c11.set_discord(Quality.VeryLow)

    c11.set_introspection(Quality.Low)
    c11.set_cooperation(Quality.Low)
    c11.set_harmony(Quality.High)
    c11.set_craftsmanship(Quality.Neutral)
    chars.append(c11)
    c12 = Character(name="Dumat Idenidek", gender="male", goals={Goals.START_A_FAMILY})
    chars.append(c12)

    # c= Character(name="",gender="male",goals={Goals.})
    # chars.append(c)

    armies = {
        "sword": [],
        "hammer": [],
        "crossbow": [],
    }

    for char in chars:
        print(f"{char.name}={char.goals}")
        char.add_skills()
    skills_to_check = [
        Skills.FurnaceOperator,
        Skills.Brewer,
        Skills.Planter,
        Skills.Thresher,
        Skills.Weaver,
        Skills.WoodBurner,
        Skills.Suturer,
        Skills.WoundDresser,
        Skills.Miner,
        Skills.StoneCutter,
        Skills.Cook,
        Skills.Bowyer,
        Skills.WeaponSmith,
        Skills.ArmorSmith,
        Skills.GemCutter,
        Skills.Carpenter,
        Skills.StoneCarver,
        Skills.StoneCrafter,
        Skills.Engraver,
        Skills.Mason,
        Skills.ArmorUser,
        Skills.Fighter,
        Skills.Dodger,
        Skills.Tactician,
        Skills.Leader,
        Skills.Appraiser,
        Skills.JudgeOfIntent,
        Skills.Negotiator,
        Skills.Organizer,
        Skills.Consoler,
        Skills.Pacifier,
        Skills.Diagnoser,
        Skills.BoneDoctor,
        Skills.Surgeon,
        Skills.RecordKeeper,
        Skills.Comedian,
        Skills.Conversationalist,
        Skills.Flatterer,
        Skills.Intimidator,
        Skills.Liar,
        Skills.Persuader,
    ]
    # print_skill_table(chars, skills=skills_to_check)
    print_skill_table([c7, c8, c9, c10, c11, c12])
    # woodcrafter,mason
    # stonecutter smooth wall
    # engraver

    roles = {
        "DodokLolok": ["StoneCarver5", "BoneDoctor2", "Surgeon2", "WoodCutter1"],
        "Eshtan": [Roles.ExpeditionLeader, "Carpenter4", "TavernKeeper"],
        "Momuz": [Roles.MilitaryLeader],
        "Tobul": ["StoneCrafter4", "Planter3", "Brewer3", "TavernPerformer"],
        "Vucar": ["Cook5", "GemCutter5", "TempMiner"],
        "DodokOkir": [Roles.Broker, Roles.BookKeeper, "StoneCutter2"],
        "Udib": [Roles.ChiefMedicalDoctor, "Engraver5", "Miner2"],
        "AthelBom": ["Bowyer2", "Miner", "Herbalist"],
        "LogemDucim": ["Miner", "Woodcutter2", Roles.Manager],
        "OnulMeg": ["weaponsmith2", "Miner", "AnimalTrainer"],
        "TekkudIgath": [],
        "DatanRerrasfikod": [],
        "DumatIdenidek": [],
    }


if __name__ == "__main__":
    game2()
