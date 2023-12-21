from enum import Enum


# descriptions in overview (green and orange) can changer over dwarf lifetime
# sourced from df discord
class BodyAttributes(Enum):
    Agility = 2
    DiseaseResistance = 6
    Endurance = 4
    Recuperation = 5
    Strength = 1
    Toughness = 3
    Frail = 7


class SoulAttributes(Enum):
    AnalyticalAbility = 1
    Creativity = 4
    Empathy = 12
    Focus = 2
    Intuition = 5
    Kinesthesic = 11
    Language = 8
    Memory = 7
    Music = 10
    Patience = 6
    SocialAwareness = 13
    SpatialSense = 9
    Willpower = 3


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
    MasterCraft = 12
    Nature = 13
    OtherSlowSkillMastering = 14
    Peaceful = 15
    Perserverance = 16
    Romance = 17
    Sacrifice = 18
    SkillMastery = 19
    Stoicism = 20
    Tradition = 21
    Tranquility = 22
    WorkOfArt = 23


class Personality(Enum):
    SelfConscious = 1
    Reserved = 2
    StraightForward = 3
    Guarded = 4
