import logging

from char import Character
from stats import (
    BodyAttributes as BA,
    SoulAttributes as SA,
    Beliefs,
    Goals,
    Facets,
    AttributeType as AT,
    Quality,
)

logging.basicConfig(filename="char.log", filemode="a", level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_char1():
    """
    girl
    Strong (Strength?)
    Recovers Slowly (Recuperation?)
    facets grey: When she's thinking. she clicks her tongue repeatedly.
    """
    char1 = Character(
        name="Sigun Giltfeasts",
        beliefs={
            Beliefs.CRAFTSMANSHIP: Quality.Highest,
            Beliefs.LAW: Quality.VeryHigh,
            Beliefs.LOYALTY: Quality.VeryHigh,
            Beliefs.FAMILY: Quality.VeryHigh,
            Beliefs.FRIENDSHIP: Quality.VeryHigh,
            Beliefs.TRUTH: Quality.VeryHigh,
            Beliefs.ARTWORK: Quality.VeryHigh,
            Beliefs.SKILL: Quality.VeryHigh,
            Beliefs.FAIRNESS: Quality.High,
            Beliefs.COOPERATION: Quality.High,
            Beliefs.MARTIAL_PROWESS: Quality.Neutral,
            Beliefs.MERRIMENT: Quality.High,
            Beliefs.LEISURE_TIME: Quality.High,
            Beliefs.COMMERCE: Quality.High,
            Beliefs.KNOWLEDGE: Quality.High,
            Beliefs.NATURE: Quality.Low,
            Beliefs.HARMONY: Quality.VeryHigh,
            # Beliefs.COMPETITION: Quality.Low,
            # Beliefs.ROMANCE: Quality.Low,
            # Beliefs.HARD_WORK: Quality.Neutral,
        },
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
        facets={
            Facets.CHEER_PROPENSITY: Quality.High,
            Facets.EMOTIONALLY_OBSESSIVE: Quality.VeryHigh,
            Facets.HOPEFUL: Quality.Low,
            Facets.HUMOR: Quality.Low,
            Facets.SINGLEMINDED: Quality.Low,
            Facets.STRESS_VULNERABILITY: Quality.Low,
            Facets.VANITY: Quality.Low,
        },
        attributes={
            BA.Strength: AT.GOOD1,  # strong
            BA.Recuperation: AT.BAD1,
            SA.Empathy: AT.BAD1,
            SA.Intuition: AT.BAD2,
            SA.AnalyticalAbility: AT.BAD2,
            SA.Creativity: AT.BAD3,
        },
    )
    char1.add_skills()
    char1.print_skills(sort_by="bf")
    char1.print_skills(sort_by="atb")
    conflicted_skills1 = char1.get_conflicted_skills()
    roles = char1.get_suitable_roles()
    logger.info("char1 ends...")


def generate_char2():
    """
    girl
    kindred spirit with Ubbul
    Austere =  strict
    Temperate = self-control/ moderate
    facets grey: She always takes a deep breath whenever she is surprised.
    """
    char = Character(
        name="Avuz Tangleglaze",
        beliefs={
            Beliefs.CRAFTSMANSHIP: Quality.Highest,
            Beliefs.LAW: Quality.VeryHigh,
            Beliefs.LOYALTY: Quality.VeryHigh,
            Beliefs.FAMILY: Quality.VeryHigh,
            Beliefs.FRIENDSHIP: Quality.VeryHigh,
            Beliefs.TRUTH: Quality.VeryHigh,
            Beliefs.ARTWORK: Quality.VeryHigh,
            Beliefs.SKILL: Quality.VeryHigh,
            Beliefs.FAIRNESS: Quality.High,
            Beliefs.COOPERATION: Quality.High,
            Beliefs.MARTIAL_PROWESS: Quality.High,
            Beliefs.MERRIMENT: Quality.High,
            Beliefs.LEISURE_TIME: Quality.High,
            Beliefs.COMMERCE: Quality.Neutral,
            # Beliefs.KNOWLEDGE: Quality.High,
            Beliefs.NATURE: Quality.Low,
            # Beliefs.HARMONY: Quality.VeryHigh,
            Beliefs.COMPETITION: Quality.VeryLow,
            Beliefs.CUNNING: Quality.High,
            # Beliefs.ROMANCE: Quality.Low,
            Beliefs.HARD_WORK: Quality.Neutral,
            Beliefs.KNOWLEDGE: Quality.Neutral,
        },
        goals={Goals.START_A_FAMILY},
        facets={
            # Facets.CHEER_PROPENSITY: Quality.High,
            # Facets.EMOTIONALLY_OBSESSIVE: Quality.VeryHigh,
            # Facets.HOPEFUL: Quality.Low,
            # Facets.HUMOR: Quality.Low,
            # Facets.SINGLEMINDED: Quality.Low,
            # Facets.STRESS_VULNERABILITY: Quality.Low,
            # Facets.VANITY: Quality.Low,
            Facets.ABSTRACT_INCLINED: Quality.Highest,
            Facets.IMMODESTY: Quality.VeryLow,
            Facets.ALTRUISM: Quality.VeryHigh,
            Facets.IMMODERATION: Quality.VeryLow,
            Facets.HATE_PROPENSITY: Quality.VeryHigh,
            Facets.GREED: Quality.VeryLow,
            Facets.ASSERTIVENESS: Quality.Low,
            Facets.LOVE_PROPENSITY: Quality.High,
            Facets.EXCITEMENT_SEEKING: Quality.Low,
            Facets.ENVY_PROPENSITY: Quality.Low,
            Facets.DISDAIN_ADVICE: Quality.High,
            Facets.BRAVERY: Quality.Low,
            Facets.IMAGINATION: Quality.High,
        },
        attributes={
            SA.Empathy: AT.BAD1,
            # SA.Intuition: AT.BAD2,
            # SA.AnalyticalAbility: AT.BAD2,
            # SA.Creativity: AT.BAD3,
            SA.Music: AT.GOOD3,
            SA.SocialAwareness: AT.GOOD2,
            SA.Creativity: AT.BAD1,
            SA.Focus: AT.BAD2,
        },
    )
    char.add_skills()
    char.print_skills(sort_by="bf")
    char.print_skills(sort_by="atb")
    conflicted_skills1 = char.get_conflicted_skills()
    roles = char.get_suitable_roles()
    logger.info("char2 ends...")


def generate_char3():
    """
    girl
    facets grey: n.a.
    """
    char = Character(
        name="Reg Whirlroofs",
        beliefs={
            Beliefs.CRAFTSMANSHIP: Quality.Neutral,
            Beliefs.LAW: Quality.High,
            Beliefs.LOYALTY: Quality.Neutral,
            Beliefs.FAMILY: Quality.VeryHigh,
            Beliefs.FRIENDSHIP: Quality.VeryHigh,
            Beliefs.TRUTH: Quality.VeryHigh,
            Beliefs.ARTWORK: Quality.VeryHigh,
            Beliefs.SKILL: Quality.VeryHigh,
            Beliefs.FAIRNESS: Quality.High,
            Beliefs.COOPERATION: Quality.High,
            Beliefs.MARTIAL_PROWESS: Quality.High,
            Beliefs.MERRIMENT: Quality.High,
            Beliefs.LEISURE_TIME: Quality.High,
            Beliefs.COMMERCE: Quality.High,
            Beliefs.KNOWLEDGE: Quality.High,
            Beliefs.NATURE: Quality.Low,
            # # Beliefs.HARMONY: Quality.VeryHigh,
            # Beliefs.COMPETITION: Quality.VeryLow,
            # Beliefs.CUNNING: Quality.High,
            # # Beliefs.ROMANCE: Quality.Low,
            Beliefs.HARD_WORK: Quality.VeryHigh,
            # Beliefs.KNOWLEDGE: Quality.Neutral,
            Beliefs.SELF_CONTROL: Quality.High,
        },
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
        facets={
            Facets.CHEER_PROPENSITY: Quality.High,
            Facets.CURIOUS: Quality.Low,
            # Facets.EMOTIONALLY_OBSESSIVE: Quality.VeryHigh,
            # Facets.HOPEFUL: Quality.Low,
            # Facets.HUMOR: Quality.Low,
            # Facets.SINGLEMINDED: Quality.Low,
            # Facets.STRESS_VULNERABILITY: Quality.Low,
            # Facets.VANITY: Quality.Low,
            # Facets.ABSTRACT_INCLINED: Quality.Highest,
            # Facets.IMMODESTY: Quality.VeryLow,
            # Facets.ALTRUISM: Quality.VeryHigh,
            Facets.IMMODERATION: Quality.Low,
            # Facets.HATE_PROPENSITY: Quality.VeryHigh,
            # Facets.GREED: Quality.VeryLow,
            # Facets.ASSERTIVENESS: Quality.Low,
            # Facets.LOVE_PROPENSITY: Quality.High,
            # Facets.EXCITEMENT_SEEKING: Quality.Low,
            # Facets.ENVY_PROPENSITY: Quality.Low,
            # Facets.DISDAIN_ADVICE: Quality.High,
            # Facets.BRAVERY: Quality.Low,
            # Facets.IMAGINATION: Quality.High,
            Facets.CRUELTY: Quality.Low,
            Facets.CONFIDENCE: Quality.Low,
        },
        attributes={
            SA.Empathy: AT.GOOD3,
            SA.Memory: AT.GOOD3,
            # # SA.Intuition: AT.BAD2,
            SA.AnalyticalAbility: AT.BAD1,
            # # SA.Creativity: AT.BAD3,
            SA.Music: AT.BAD1,
            SA.SocialAwareness: AT.BAD2,
            # SA.Creativity: AT.BAD1,
            # SA.Focus: AT.BAD2,
            SA.Patience: AT.GOOD3,
            SA.Kinesthesic: AT.GOOD1,
        },
    )
    char.add_skills()
    char.print_skills(sort_by="bf")
    char.print_skills(sort_by="atb")
    conflicted_skills1 = char.get_conflicted_skills()
    roles = char.get_suitable_roles()
    logger.info("char3 ends...")


def generate_char4():
    """
    girl
    kindred spirit with Ineth Umarbomrek
    resilient (related to perserverance?)
    intemperate (lack of control/ immoderate)
    wasteful
    facets grey: She chews her lips when she's nervous. She rolls her eyes when she's annoyed.
    """
    char = Character(
        name="Kulet Bridgeardent",
        beliefs={
            Beliefs.CRAFTSMANSHIP: Quality.Highest,
            Beliefs.LAW: Quality.VeryHigh,
            Beliefs.LOYALTY: Quality.Low,
            Beliefs.FAMILY: Quality.VeryHigh,
            Beliefs.FRIENDSHIP: Quality.VeryHigh,
            Beliefs.TRUTH: Quality.VeryHigh,
            Beliefs.ARTWORK: Quality.VeryHigh,
            Beliefs.SKILL: Quality.VeryHigh,
            Beliefs.FAIRNESS: Quality.High,
            Beliefs.COOPERATION: Quality.High,
            Beliefs.MARTIAL_PROWESS: Quality.High,
            Beliefs.MERRIMENT: Quality.High,
            Beliefs.LEISURE_TIME: Quality.High,
            Beliefs.COMMERCE: Quality.High,
            Beliefs.KNOWLEDGE: Quality.High,
            Beliefs.NATURE: Quality.Low,
            # # Beliefs.HARMONY: Quality.VeryHigh,
            # Beliefs.COMPETITION: Quality.VeryLow,
            # Beliefs.CUNNING: Quality.High,
            # # Beliefs.ROMANCE: Quality.Low,
            Beliefs.HARD_WORK: Quality.VeryHigh,
            # Beliefs.KNOWLEDGE: Quality.Neutral,
            # Beliefs.SELF_CONTROL: Quality.High,
        },
        goals={Goals.CRAFT_A_MASTERWORK},
        facets={
            # Facets.CHEER_PROPENSITY: Quality.High,
            # Facets.CURIOUS: Quality.Low,
            # Facets.EMOTIONALLY_OBSESSIVE: Quality.VeryHigh,
            # Facets.HOPEFUL: Quality.Low,
            # Facets.HUMOR: Quality.Low,
            # Facets.SINGLEMINDED: Quality.Low,
            Facets.STRESS_VULNERABILITY: Quality.VeryLow,
            # Facets.VANITY: Quality.Low,
            # Facets.ABSTRACT_INCLINED: Quality.Highest,
            # Facets.IMMODESTY: Quality.VeryLow,
            # Facets.ALTRUISM: Quality.VeryHigh,
            Facets.IMMODERATION: Quality.VeryHigh,
            # Facets.HATE_PROPENSITY: Quality.VeryHigh,
            # Facets.GREED: Quality.VeryLow,
            Facets.ASSERTIVENESS: Quality.Low,
            # Facets.LOVE_PROPENSITY: Quality.High,
            # Facets.EXCITEMENT_SEEKING: Quality.Low,
            # Facets.ENVY_PROPENSITY: Quality.Low,
            Facets.DISDAIN_ADVICE: Quality.Low,
            # Facets.BRAVERY: Quality.Low,
            # Facets.IMAGINATION: Quality.High,
            # Facets.CRUELTY: Quality.Low,
            # Facets.CONFIDENCE: Quality.Low,
            Facets.WASTEFULNESS: Quality.High,
            Facets.GREGARIOUSNESS: Quality.High,
            Facets.BASHFUL: Quality.Low,
            Facets.VIOLENT: Quality.High,
            Facets.ANXIETY_PROPENSITY: Quality.High,
            Facets.SINGLEMINDED: Quality.High,
            Facets.PERSEVERANCE: Quality.High,
            Facets.SWAYED_BY_EMOTIONS: Quality.Low,
        },
        attributes={
            SA.Empathy: AT.GOOD3,
            # SA.Memory: AT.GOOD3,
            # # SA.Intuition: AT.BAD2,
            SA.AnalyticalAbility: AT.GOOD1,
            SA.Creativity: AT.GOOD1,
            # SA.Music: AT.BAD1,
            SA.SocialAwareness: AT.GOOD1,
            # SA.Creativity: AT.BAD1,
            # SA.Focus: AT.BAD2,
            # SA.Patience: AT.GOOD3,
            # SA.Kinesthesic: AT.GOOD1,
            SA.Willpower: AT.GOOD2,
            SA.SpatialSense: AT.BAD1,
        },
    )
    char.add_skills()
    char.print_skills(sort_by="bf")
    char.print_skills(sort_by="atb")
    conflicted_skills1 = char.get_conflicted_skills()
    roles = char.get_suitable_roles()
    logger.info("char4 ends...")


def generate_char5():
    """
    girl
    kindred spirit with tobul
    noy vain
    loner
    pusillanimous= lack of courage/ determination, timid
    facets grey: she winks during convo
    """
    char = Character(
        name="Ubbul Cleanroof",
        beliefs={
            Beliefs.ARTWORK: Quality.VeryHigh,
            Beliefs.COMMERCE: Quality.High,
            # Beliefs.COMPETITION: Quality.VeryLow,
            Beliefs.COOPERATION: Quality.High,
            Beliefs.CRAFTSMANSHIP: Quality.Neutral,
            # Beliefs.CUNNING: Quality.High,
            Beliefs.FAIRNESS: Quality.High,
            Beliefs.FAMILY: Quality.VeryHigh,
            Beliefs.FRIENDSHIP: Quality.VeryHigh,
            Beliefs.HARD_WORK: Quality.VeryHigh,
            # Beliefs.HARMONY: Quality.VeryHigh,
            Beliefs.KNOWLEDGE: Quality.High,
            # Beliefs.KNOWLEDGE: Quality.Neutral,
            Beliefs.LAW: Quality.VeryHigh,
            Beliefs.LEISURE_TIME: Quality.High,
            Beliefs.LOYALTY: Quality.VeryHigh,
            Beliefs.MARTIAL_PROWESS: Quality.High,
            Beliefs.MERRIMENT: Quality.High,
            Beliefs.NATURE: Quality.Low,
            Beliefs.PERSEVERANCE: Quality.High,
            Beliefs.ROMANCE: Quality.High,
            # Beliefs.SELF_CONTROL: Quality.High,
            Beliefs.SKILL: Quality.VeryHigh,
            Beliefs.TRUTH: Quality.VeryHigh,
        },
        goals={Goals.MASTER_A_SKILL},
        facets={
            Facets.ABSTRACT_INCLINED: Quality.High,
            # Facets.ALTRUISM: Quality.VeryHigh,
            # Facets.ANXIETY_PROPENSITY: Quality.High,
            # Facets.ASSERTIVENESS: Quality.Low,
            # Facets.BASHFUL: Quality.Low,
            # Facets.BRAVERY: Quality.Low,
            # Facets.CHEER_PROPENSITY: Quality.High,
            Facets.CONFIDENCE: Quality.VeryLow,
            # Facets.CRUELTY: Quality.Low,
            # Facets.CURIOUS: Quality.Low,
            # Facets.DISDAIN_ADVICE: Quality.Low,
            Facets.DEPRESSION_PROPENSITY: Quality.High,
            # Facets.EMOTIONALLY_OBSESSIVE: Quality.VeryHigh,
            Facets.ENVY_PROPENSITY: Quality.High,
            # Facets.EXCITEMENT_SEEKING: Quality.Low,
            # Facets.GREED: Quality.VeryLow,
            Facets.GREGARIOUSNESS: Quality.VeryLow,
            # Facets.HATE_PROPENSITY: Quality.VeryHigh,
            # Facets.HOPEFUL: Quality.Low,
            # Facets.HUMOR: Quality.Low,
            # Facets.IMAGINATION: Quality.High,
            Facets.IMMODERATION: Quality.High,
            # Facets.IMMODESTY: Quality.VeryLow,
            Facets.LOVE_PROPENSITY: Quality.High,
            # Facets.PERSEVERANCE: Quality.High,
            # Facets.SINGLEMINDED: Quality.High,
            # Facets.SINGLEMINDED: Quality.Low,
            # Facets.STRESS_VULNERABILITY: Quality.VeryLow,
            # Facets.SWAYED_BY_EMOTIONS: Quality.Low,
            Facets.TRUST: Quality.Low,
            Facets.VANITY: Quality.VeryLow,
            Facets.VIOLENT: Quality.Low,
            # Facets.WASTEFULNESS: Quality.High,
        },
        attributes={
            # SA.AnalyticalAbility: AT.GOOD1,
            # SA.Creativity: AT.BAD1,
            # SA.Creativity: AT.GOOD1,
            # SA.Empathy: AT.GOOD3,
            # SA.Focus: AT.BAD2,
            # SA.Intuition: AT.BAD2,
            # SA.Kinesthesic: AT.GOOD1,
            SA.Language: AT.GOOD1,
            SA.Memory: AT.BAD1,
            # SA.Music: AT.BAD1,
            SA.Patience: AT.BAD1,
            # SA.SocialAwareness: AT.GOOD1,
            # SA.Willpower: AT.GOOD2,
            SA.SpatialSense: AT.GOOD3,
        },
    )
    char.add_skills()
    char.print_skills(sort_by="bf")
    char.print_skills(sort_by="atb")
    conflicted_skills1 = char.get_conflicted_skills()
    roles = char.get_suitable_roles()
    logger.info("char5 ends...")


def generate_char6():
    """
    guy
    resists sickness
    facets grey: when he's annoyed, he starts to talk slowly
    """
    char = Character(
        name="Ineth Smoothwhipped",
        beliefs={
            # Beliefs.ARTWORK: Quality.Neutral,
            Beliefs.COMMERCE: Quality.High,
            # Beliefs.COMPETITION: Quality.VeryLow,
            Beliefs.COOPERATION: Quality.High,
            Beliefs.CRAFTSMANSHIP: Quality.Neutral,
            # Beliefs.CUNNING: Quality.High,
            Beliefs.FAIRNESS: Quality.High,
            Beliefs.FAMILY: Quality.VeryHigh,
            Beliefs.FRIENDSHIP: Quality.VeryHigh,
            Beliefs.HARD_WORK: Quality.VeryHigh,
            Beliefs.HARMONY: Quality.High,
            Beliefs.KNOWLEDGE: Quality.High,
            Beliefs.LAW: Quality.VeryHigh,
            Beliefs.LEISURE_TIME: Quality.High,
            Beliefs.LOYALTY: Quality.VeryHigh,
            Beliefs.MARTIAL_PROWESS: Quality.High,
            Beliefs.MERRIMENT: Quality.High,
            Beliefs.NATURE: Quality.Low,
            Beliefs.PEACE: Quality.Low,
            # Beliefs.PERSEVERANCE: Quality.High,
            # Beliefs.ROMANCE: Quality.High,
            # Beliefs.SELF_CONTROL: Quality.High,
            Beliefs.SKILL: Quality.VeryHigh,
            Beliefs.TRUTH: Quality.VeryHigh,
        },
        goals={Goals.MASTER_A_SKILL},
        facets={
            # Facets.ABSTRACT_INCLINED: Quality.High,
            # Facets.ALTRUISM: Quality.VeryHigh,
            Facets.ANXIETY_PROPENSITY: Quality.High,
            Facets.ASSERTIVENESS: Quality.Low,
            # Facets.BASHFUL: Quality.Low,
            # Facets.BRAVERY: Quality.Low,
            # Facets.CHEER_PROPENSITY: Quality.High,
            # Facets.CONFIDENCE: Quality.VeryLow,
            # Facets.CRUELTY: Quality.Low,
            # Facets.CURIOUS: Quality.Low,
            # Facets.DISDAIN_ADVICE: Quality.Low,
            # Facets.DEPRESSION_PROPENSITY: Quality.High,
            Facets.EMOTIONALLY_OBSESSIVE: Quality.High,
            # Facets.ENVY_PROPENSITY: Quality.High,
            # Facets.EXCITEMENT_SEEKING: Quality.Low,
            Facets.FRIENDLINESS: Quality.High,
            # Facets.GREED: Quality.VeryLow,
            # Facets.GREGARIOUSNESS: Quality.VeryLow,
            # Facets.HATE_PROPENSITY: Quality.VeryHigh,
            # Facets.HOPEFUL: Quality.Low,
            # Facets.HUMOR: Quality.Low,
            # Facets.IMAGINATION: Quality.High,
            # Facets.IMMODERATION: Quality.High,
            # Facets.IMMODESTY: Quality.VeryLow,
            # Facets.LOVE_PROPENSITY: Quality.High,
            # Facets.PERSEVERANCE: Quality.High,
            Facets.SINGLEMINDED: Quality.High,
            # Facets.STRESS_VULNERABILITY: Quality.VeryLow,
            # Facets.SWAYED_BY_EMOTIONS: Quality.Low,
            # Facets.TRUST: Quality.Low,
            Facets.VANITY: Quality.VeryHigh,
            Facets.VENGEFUL: Quality.Low,
            # Facets.VIOLENT: Quality.Low,
            # Facets.WASTEFULNESS: Quality.High,
        },
        attributes={
            BA.DiseaseResistance: AT.GOOD1,  # resist sickness
            SA.AnalyticalAbility: AT.BAD2,
            # SA.Creativity: AT.BAD1,
            # SA.Creativity: AT.GOOD1,
            SA.Empathy: AT.BAD1,
            SA.Focus: AT.GOOD2,
            # SA.Intuition: AT.BAD2,
            # SA.Kinesthesic: AT.GOOD1,
            SA.Language: AT.GOOD3,
            # SA.Memory: AT.BAD1,
            # SA.Music: AT.BAD1,
            # SA.Patience: AT.BAD1,
            # SA.SocialAwareness: AT.GOOD1,
            SA.Willpower: AT.GOOD1,  # no very good willpower, so put good1 according to master_list
            # SA.SpatialSense: AT.GOOD3,
        },
    )
    char.add_skills()
    char.print_skills(sort_by="bf")
    char.print_skills(sort_by="atb")
    conflicted_skills1 = char.get_conflicted_skills()
    roles = char.get_suitable_roles()
    logger.info("char6 ends...")


def generate_char7():
    """
    guy
    friend with sigun
    sickly (DiseaseResistance related?)

    facets grey: has a habit of stretching his body during pauses in convo
    """
    char = Character(
        name="Tobul Murdersyrup",
        beliefs={
            Beliefs.ARTWORK: Quality.VeryHigh,
            Beliefs.COMMERCE: Quality.High,
            # Beliefs.COMPETITION: Quality.VeryLow,
            Beliefs.COOPERATION: Quality.High,
            Beliefs.CRAFTSMANSHIP: Quality.Highest,
            # Beliefs.CUNNING: Quality.High,
            Beliefs.FAIRNESS: Quality.High,
            Beliefs.FAMILY: Quality.VeryHigh,
            Beliefs.FRIENDSHIP: Quality.VeryHigh,
            Beliefs.HARD_WORK: Quality.VeryHigh,
            # Beliefs.HARMONY: Quality.High,
            Beliefs.KNOWLEDGE: Quality.High,
            Beliefs.LAW: Quality.VeryHigh,
            Beliefs.LEISURE_TIME: Quality.High,
            Beliefs.LOYALTY: Quality.VeryHigh,
            Beliefs.MARTIAL_PROWESS: Quality.High,
            Beliefs.MERRIMENT: Quality.High,
            Beliefs.NATURE: Quality.Low,
            # Beliefs.PEACE: Quality.Low,
            Beliefs.PERSEVERANCE: Quality.High,
            # Beliefs.ROMANCE: Quality.High,
            # Beliefs.SELF_CONTROL: Quality.High,
            Beliefs.SKILL: Quality.VeryHigh,
            Beliefs.TRANQUILITY: Quality.Low,
            Beliefs.TRUTH: Quality.VeryHigh,
        },
        goals={Goals.MASTER_A_SKILL},
        facets={
            # Facets.ABSTRACT_INCLINED: Quality.High,
            # Facets.ALTRUISM: Quality.VeryHigh,
            # Facets.ANXIETY_PROPENSITY: Quality.High,
            # Facets.ASSERTIVENESS: Quality.Low,
            # Facets.BASHFUL: Quality.Low,
            # Facets.BRAVERY: Quality.Low,
            # Facets.CHEER_PROPENSITY: Quality.High,
            # Facets.CONFIDENCE: Quality.VeryLow,
            # Facets.CRUELTY: Quality.Low,
            # Facets.CURIOUS: Quality.Low,
            # Facets.DISDAIN_ADVICE: Quality.Low,
            # Facets.DEPRESSION_PROPENSITY: Quality.High,
            # Facets.EMOTIONALLY_OBSESSIVE: Quality.High,
            # Facets.ENVY_PROPENSITY: Quality.High,
            # Facets.EXCITEMENT_SEEKING: Quality.Low,
            Facets.FRIENDLINESS: Quality.Low,
            # Facets.GREED: Quality.VeryLow,
            # Facets.GREGARIOUSNESS: Quality.VeryLow,
            # Facets.HATE_PROPENSITY: Quality.VeryHigh,
            Facets.HOPEFUL: Quality.High,
            Facets.HUMOR: Quality.VeryHigh,
            Facets.IMAGINATION: Quality.Low,
            Facets.IMMODERATION: Quality.Low,
            Facets.IMMODESTY: Quality.VeryLow,
            # Facets.LOVE_PROPENSITY: Quality.High,
            Facets.PERSEVERANCE: Quality.High,
            Facets.PRIDE: Quality.High,
            # Facets.SINGLEMINDED: Quality.High,
            # Facets.STRESS_VULNERABILITY: Quality.VeryLow,
            # Facets.SWAYED_BY_EMOTIONS: Quality.Low,
            Facets.TOLERANT: Quality.Low,
            Facets.TRUST: Quality.VeryLow,
            Facets.VANITY: Quality.High,
            Facets.VENGEFUL: Quality.High,
            # Facets.VIOLENT: Quality.Low,
            # Facets.WASTEFULNESS: Quality.High,
        },
        attributes={
            BA.DiseaseResistance: AT.BAD1,  # sickly
            # SA.AnalyticalAbility: AT.BAD2,
            SA.Creativity: AT.BAD1,
            # SA.Creativity: AT.GOOD1,
            # SA.Empathy: AT.BAD1,
            # SA.Focus: AT.GOOD2,
            SA.Intuition: AT.GOOD2,
            # SA.Kinesthesic: AT.GOOD1,
            SA.Language: AT.BAD2,
            # SA.Memory: AT.BAD1,
            # SA.Music: AT.BAD1,
            SA.Patience: AT.BAD2,
            # SA.SocialAwareness: AT.GOOD1,
            # SA.Willpower: AT.GOOD1,
            # SA.SpatialSense: AT.GOOD3,
        },
    )
    char.add_skills()
    char.print_skills(sort_by="bf")
    char.print_skills(sort_by="atb")
    conflicted_skills1 = char.get_conflicted_skills()
    roles = char.get_suitable_roles()
    logger.info("char7 ends...")


if __name__ == "__main__":
    generate_char1()
    generate_char2()
    generate_char3()
    generate_char4()
    generate_char5()
    generate_char6()
    generate_char7()
