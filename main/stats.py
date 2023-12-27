from enum import Enum, IntEnum


# descriptions in overview (green and orange) can changer over dwarf lifetime
# sourced from df discord
class BodyAttributes(Enum):
    Agility = 1
    DiseaseResistance = 4
    Endurance = 6
    Frail = 8
    Recuperation = 15
    Strength = 18
    Toughness = 19

    def __repr__(self) -> str:
        return f"{self.name}"


class SoulAttributes(Enum):
    AnalyticalAbility = 2
    Creativity = 3
    Empathy = 5
    Focus = 7
    Intuition = 9
    Kinesthesic = 10
    Language = 11
    Memory = 12
    Music = 13
    Patience = 14
    SocialAwareness = 16
    SpatialSense = 17
    Willpower = 20

    def __repr__(self) -> str:
        return f"{self.name}"


class Values(Enum):
    ActiveLife = 1
    ArtWork = 2  # in discord say only affect during chatter
    ClimbSocietyRank = 3
    Commerce = 4
    Competition = 5
    Family = 6
    Friendship = 7
    Introspection = 8
    Knowledge = 9
    Law = 10
    Leisure = 11
    Martialprowess = 12
    MasterCraft = 13
    Nature = 14
    OtherSlowSkillMastering = 15
    Peaceful = 16
    Perserverance = 17
    Romance = 18
    Sacrifice = 19
    SkillMastery = 20
    Stoicism = 21
    Tradition = 22
    Tranquility = 23
    WorkOfArt = 24


class Personalities(Enum):
    SelfConscious = 1
    Reserved = 2
    StraightForward = 3
    Guarded = 4


class Scores(IntEnum):
    A = 100
    B = 250
    C = 250
