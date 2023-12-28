from enum import Enum, IntEnum


# descriptions in overview (green and orange) can changer over dwarf lifetime
# sourced from df discord
class BodyAttributes(Enum):
    Strength = 1
    Agility = 2
    Toughness = 3
    Endurance = 4
    Recuperation = 5
    DiseaseResistance = 6

    def __repr__(self) -> str:
        return f"{self.name}"


class SoulAttributes(Enum):
    AnalyticalAbility = 1
    Creativity = 2
    Empathy = 3
    Focus = 4
    Intuition = 5
    Kinesthesic = 6
    Language = 7
    Memory = 8
    Music = 9
    Patience = 10
    SocialAwareness = 11
    SpatialSense = 12
    Willpower = 13

    def __repr__(self) -> str:
        return f"{self.name}"


class Beliefs(Enum):
    """
    - Under Personality-> Values
    - Memory can change beliefs and facets overtime.
    - Dictates needs and frequency of them.
    """

    LAW = 1
    LOYALTY = 2
    FAMILY = 3
    FRIENDSHIP = 4
    POWER = 5
    TRUTH = 6
    CUNNING = 7
    ELOQUENCE = 8
    FAIRNESS = 9
    DECORUM = 10
    TRADITION = 11
    ARTWORK = 12
    COOPERATION = 13
    INDEPENDENCE = 14
    STOICISM = 15
    INTROSPECTION = 16
    SELF_CONTROL = 17
    TRANQUILITY = 18
    HARMONY = 19
    MERRIMENT = 20
    CRAFTSMANSHIP = 21
    MARTIAL_PROWESS = 22
    SKILL = 23
    HARD_WORK = 24
    SACRIFICE = 25
    COMPETITION = 26
    PERSEVERANCE = 27
    LEISURE_TIME = 28
    COMMERCE = 29
    ROMANCE = 30
    NATURE = 31
    PEACE = 32
    KNOWLEDGE = 33


class Goals(Enum):
    START_A_FAMILY = 1
    RULE_THE_WORLD = 2
    CREATE_A_GREAT_WORK_OF_ART = 3
    CRAFT_A_MASTERWORK = 4
    BRING_PEACE_TO_THE_WORLD = 5
    BECOME_A_LEGENDARY_WARRIOR = 6
    MASTER_A_SKILL = 7
    FALL_IN_LOVE = 8
    SEE_THE_GREAT_NATURAL_SITES = 9
    IMMORTALITY = 10
    MAKE_A_GREAT_DISCOVERY = 11
    ATTAIN_RANK_IN_SOCIETY = 12
    BATHE_WORLD_IN_CHAOS = 13
    STAY_ALIVE = 14
    MAINTAIN_ENTITY_STATUS = 15


class Facets(Enum):
    """
    - Memory can change beliefs and facets overtime.
    - Conflicting facets currently gives unknown effect.
    - 2 dwarves with conflicting facets (i.e. 1 value helping, others hate helping),
    will have grudges with each other. Making grudges causes an unhappy thought. To
    ameliorate, have more meeting zones (so they meet each other less?)
    """

    LOVE_PROPENSITY = 1
    HATE_PROPENSITY = 2
    ENVY_PROPENSITY = 3
    # Cheer propensity is bad for most skills since very difficult to make the dwarf happy
    CHEER_PROPENSITY = 4
    DEPRESSION_PROPENSITY = 5
    ANGER_PROPENSITY = 6
    ANXIETY_PROPENSITY = 7
    LUST_PROPENSITY = 8
    STRESS_VULNERABILITY = 9
    GREED = 10
    IMMODERATION = 11
    VIOLENT = 12
    PERSEVERANCE = 13
    WASTEFULNESS = 14
    DISCORD = 15
    FRIENDLINESS = 16
    POLITENESS = 17
    DISDAIN_ADVICE = 18
    BRAVERY = 19
    CONFIDENCE = 20
    VANITY = 21
    AMBITION = 22
    GRATITUDE = 23
    IMMODESTY = 24
    HUMOR = 25
    VENGEFUL = 26
    PRIDE = 27
    CRUELTY = 28
    SINGLEMINDED = 29
    HOPEFUL = 30
    CURIOUS = 31
    BASHFUL = 32
    PRIVACY = 33
    PERFECTIONIST = 34
    CLOSEMINDED = 35
    TOLERANT = 36
    EMOTIONALLY_OBSESSIVE = 37
    SWAYED_BY_EMOTIONS = 38
    ALTRUISM = 39
    DUTIFULNESS = 40
    THOUGHTLESSNESS = 41
    ORDERLINESS = 42
    TRUST = 43
    GREGARIOUSNESS = 44
    ASSERTIVENESS = 45
    ACTIVITY_LEVEL = 46
    EXCITEMENT_SEEKING = 47
    IMAGINATION = 48
    ABSTRACT_INCLINED = 49
    ART_INCLINED = 50


class Scores(IntEnum):
    """
    Qualifier for skill attributes
    """

    A = 100
    B = 250
    C = 250


class Quality(IntEnum):
    """
    Qualifier for Beliefs and Facets
    """

    Highest = 3
    VeryHigh = 2
    High = 1
    Neutral = 0
    Low = -1
    VeryLow = -2
    Lowest = -3


class ThoughtType(IntEnum):
    HAPPY = 1
    NEUTRAL = 0
    UNHAPPY = -1


class AttributeType(IntEnum):
    """
    Qualifier for BodyAttributes and SoulAttributes
    """

    GOOD4 = 4
    GOOD3 = 3
    GOOD2 = 2
    GOOD1 = 1
    NEUTRAL = 0
    BAD1 = -1
    BAD2 = -2
    BAD3 = -3
    BAD4 = -4
