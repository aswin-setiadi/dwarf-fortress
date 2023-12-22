from enum import Enum


# descriptions in overview (green and orange) can changer over dwarf lifetime
# sourced from df discord
class BodyAttributes(Enum):
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


class SoulAttributes(Enum):
    Agility = 1
    DiseaseResistance = 4
    Endurance = 6
    Frail = 8
    Recuperation = 15
    Strength = 18
    Toughness = 19


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


class Personalities(Enum):
    SelfConscious = 1
    Reserved = 2
    StraightForward = 3
    Guarded = 4
