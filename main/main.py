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


if __name__ == "__main__":
    main()
