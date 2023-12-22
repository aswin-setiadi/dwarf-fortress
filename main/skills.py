from enum import Enum
from stats import BodyAttributes, Scores, SoulAttributes


class Skills(Enum):
    WoodCutter = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Willpower: Scores.C,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Agility: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    Miner = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Willpower: Scores.C,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Toughness: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    Carpenter = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Creativity: Scores.C,
    }
    StoneCutter = {
        # wiki n.a
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Creativity: Scores.C,
    }
    StoneCarver = {
        # wiki n.a
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Creativity: Scores.C,
    }
    StoneCrafter = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Creativity: Scores.C,
    }

    Cook = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.AnalyticalAbility: Scores.B,
        SoulAttributes.Creativity: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }

    Brewer = {
        SoulAttributes.Kinesthesic: Scores.A,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Agility: Scores.B,
    }

    Planter = {
        SoulAttributes.Kinesthesic: Scores.A,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Agility: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    Herbalist = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.Memory: Scores.B,
        BodyAttributes.Agility: Scores.A,
    }

    Spinner = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        BodyAttributes.Agility: Scores.A,
        BodyAttributes.Strength: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    Thresher = {
        SoulAttributes.Kinesthesic: Scores.A,
        BodyAttributes.Agility: Scores.A,
        BodyAttributes.Strength: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    Weaver = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Creativity: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }

    WoodBurner = {
        SoulAttributes.Kinesthesic: Scores.A,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Toughness: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    Fisherdwarf = {
        SoulAttributes.Focus: Scores.A,
        SoulAttributes.Patience: Scores.B,
        SoulAttributes.Kinesthesic: Scores.C,
        BodyAttributes.Agility: Scores.A,
        BodyAttributes.Strength: Scores.B,
    }

    FishCleaner = {
        SoulAttributes.Kinesthesic: Scores.A,
        BodyAttributes.Agility: Scores.A,
        BodyAttributes.Endurance: Scores.B,
    }

    FurnaceOperator = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.AnalyticalAbility: Scores.B,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Toughness: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    WeaponSmith = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Creativity: Scores.C,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Agility: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    GemCutter = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.AnalyticalAbility: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }

    WoodCrafter = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Creativity: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }

    Discipline = {SoulAttributes.Willpower: Scores.A, SoulAttributes.Focus: Scores.B}

    ArmorUser = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.Willpower: Scores.B,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Toughness: Scores.B,
        BodyAttributes.Endurance: Scores.C,
    }

    Fighter = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Willpower: Scores.C,
        BodyAttributes.Agility: Scores.A,
        BodyAttributes.Strength: Scores.B,
        BodyAttributes.Toughness: Scores.C,
    }

    Dodger = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Willpower: Scores.C,
        BodyAttributes.Agility: Scores.A,
        BodyAttributes.Toughness: Scores.B,
        BodyAttributes.Endurance: Scores.B,
    }

    Appraiser = {
        SoulAttributes.AnalyticalAbility: Scores.A,
        SoulAttributes.Memory: Scores.B,
        SoulAttributes.Intuition: Scores.C,
    }

    Organizer = {
        SoulAttributes.AnalyticalAbility: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Creativity: Scores.C,
    }
    RecordKeeper = {
        SoulAttributes.AnalyticalAbility: Scores.A,
        SoulAttributes.Memory: Scores.B,
        SoulAttributes.Focus: Scores.C,
    }

    Tactician = {
        SoulAttributes.AnalyticalAbility: Scores.A,
        SoulAttributes.Creativity: Scores.B,
        SoulAttributes.Intuition: Scores.C,
    }

    Comedian = {
        # this skill raises agility
        SoulAttributes.Language: Scores.A,
        SoulAttributes.Creativity: Scores.B,
        SoulAttributes.Kinesthesic: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }

    Conversationalist = {
        SoulAttributes.Language: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Empathy: Scores.C,
    }

    Flatterer = {
        SoulAttributes.Language: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Empathy: Scores.C,
    }

    Intimidator = {
        # this skill raises agility
        SoulAttributes.Language: Scores.A,
        SoulAttributes.Kinesthesic: Scores.B,
        BodyAttributes.Strength: Scores.A,
        BodyAttributes.Agility: Scores.B,
    }
    JudgeOfIntent = {
        SoulAttributes.Empathy: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Intuition: Scores.C,
    }

    Liar = {
        SoulAttributes.Language: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Creativity: Scores.C,
    }

    Negotiator = {
        SoulAttributes.Language: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Empathy: Scores.C,
    }

    Persuader = {
        SoulAttributes.Language: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Empathy: Scores.C,
    }
    Consoler = {
        SoulAttributes.Empathy: Scores.A,
        SoulAttributes.Language: Scores.B,
        SoulAttributes.SocialAwareness: Scores.C,
    }

    Pacifier = {
        SoulAttributes.Language: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Empathy: Scores.C,
    }

    Leader = {
        SoulAttributes.Empathy: Scores.A,
        SoulAttributes.SocialAwareness: Scores.B,
        SoulAttributes.Language: Scores.C,
    }

    Concentration = {
        SoulAttributes.Focus: Scores.A,
        SoulAttributes.Patience: Scores.B,
        SoulAttributes.Willpower: Scores.C,
    }

    Observer = {
        SoulAttributes.SpatialSense: Scores.A,
        SoulAttributes.Focus: Scores.B,
        SoulAttributes.Intuition: Scores.C,
    }

    Diagnoser = {
        SoulAttributes.AnalyticalAbility: Scores.A,
        SoulAttributes.Memory: Scores.B,
        SoulAttributes.Intuition: Scores.C,
    }

    BoneDoctor = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Focus: Scores.C,
        BodyAttributes.Agility: Scores.A,
        BodyAttributes.Strength: Scores.B,
    }
    Surgeon = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Focus: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }
    Suturer = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Focus: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }
    WoundDresser = {
        SoulAttributes.Kinesthesic: Scores.A,
        SoulAttributes.SpatialSense: Scores.B,
        SoulAttributes.Empathy: Scores.C,
        BodyAttributes.Agility: Scores.A,
    }


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


if __name__ == "__main__":
    print(Skills.WoodCutter)  # Skills.WoodCutter
    print(type(Skills.WoodCutter))  # <enum 'Skills'>
    a = Animal("cat")
    print(a)  # <__main__.Animal object at 0x000002462B053850>
    print(type(a))  # <class '__main__.Animal'>
