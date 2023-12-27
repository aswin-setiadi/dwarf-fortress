from abc import ABCMeta
from enum import Enum

from stats import BodyAttributes, Personalities, Scores, SoulAttributes


class Skill(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.attributes: dict[BodyAttributes | SoulAttributes, Scores] = {}

    def can_get_xp(self, personalities: set[Personalities]):
        return True


class AnimalTrainer(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Empathy: Scores.A,
            SoulAttributes.Patience: Scores.B,
            SoulAttributes.Intuition: Scores.C,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class Appraiser(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.AnalyticalAbility: Scores.A,
            SoulAttributes.Memory: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class ArmorUser(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.Willpower: Scores.B,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class BoneDoctor(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Focus: Scores.C,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Strength: Scores.B,
        }


class Brewer(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
        }


class Carpenter(Skill):
    """
    Produces wooden bed bin barrel, etc.
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
        }


class Comedian(Skill):
    """
    This skill raises agility
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.Creativity: Scores.B,
            SoulAttributes.Kinesthesic: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Concentration(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Focus: Scores.A,
            SoulAttributes.Patience: Scores.B,
            SoulAttributes.Willpower: Scores.C,
        }


class Consoler(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Empathy: Scores.A,
            SoulAttributes.Language: Scores.B,
            SoulAttributes.SocialAwareness: Scores.C,
        }


class Conversationalist(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }


class Cook(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.AnalyticalAbility: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Diagnoser(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.AnalyticalAbility: Scores.A,
            SoulAttributes.Memory: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class Discipline(Skill):
    """
    Military less likely to route
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Willpower: Scores.A,
            SoulAttributes.Focus: Scores.B,
        }


class Dodger(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Willpower: Scores.C,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.B,
        }


class Engraver(Skill):
    """
    Any constructed wall or floor or smoothed natural surface can be engraved;
    soil cannot be smoothed or engraved. Engraving increases the value of a wall
    or floor and gives it a quality level, which is dependent upon the engravers'
    skill. While experienced dwarves are more likely to engrave historical events
    than a novice, it is unclear if personality has any effect. Low-quality or
    unwanted engraved floor can be redone by carving a track over it and then
    smoothing the tile.

    Engraving gives the lowest amounts of XP per job of any skill (10 XP)
    meaning that it one of the most time consuming professions for your dwarves
    to skill up in. Since engraving is painfully slow at low skill levels,
    it may be a good idea to bring a proficient engraver in your embark to give
    you a head start. Even with a proficient engraver constantly doing engraving,
    it can take more than 5 in-game years to skill your dwarves up to legendary
    doing engravings the conventional way.

    Wiki: https://dwarffortresswiki.org/index.php/Engraver
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Fighter(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Willpower: Scores.C,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Strength: Scores.B,
            BodyAttributes.Toughness: Scores.C,
        }


class FishCleaner(Skill):
    """
    Process raw fish, skill only determined speed
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Endurance: Scores.B,
        }


class Fisherdwarf(Skill):
    """
    Fishing
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Focus: Scores.A,
            SoulAttributes.Patience: Scores.B,
            SoulAttributes.Kinesthesic: Scores.C,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Strength: Scores.B,
        }


class Flatterer(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }


class FurnaceOperator(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.AnalyticalAbility: Scores.B,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class GemCutter(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.AnalyticalAbility: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Herbalist(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.Memory: Scores.B,
            BodyAttributes.Agility: Scores.A,
        }


class Intimidator(Skill):
    """
    This skill raises agility
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.Kinesthesic: Scores.B,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
        }


class JudgeOfIntent(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Empathy: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class Leader(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Empathy: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Language: Scores.C,
        }


class Liar(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Creativity: Scores.C,
        }


class Mason(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class Miner(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Willpower: Scores.C,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class Negotiator(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }


class Observer(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.SpatialSense: Scores.A,
            SoulAttributes.Focus: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class Organizer(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.AnalyticalAbility: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Creativity: Scores.C,
        }


class Pacifier(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }


class Persuader(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }


class Planter(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class RecordKeeper(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.AnalyticalAbility: Scores.A,
            SoulAttributes.Memory: Scores.B,
            SoulAttributes.Focus: Scores.C,
        }


class Spinner(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Strength: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class StoneCarver(Skill):
    """
    Produces stone furniture(table chair door), slab for tomb
    not sure order correct or not cause missing in attributes wiki
    and in stone carver wiki it seems ordered from bottom up.
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Endurance: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Strength: Scores.C,
        }


class StoneCrafter(Skill):
    """
    Stone mug, crafts, instruments, toys, jugs, pots, etc
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class StoneCutter(Skill):
    """
    No entry in attributes wiki, status/ attributes unknown in Stonecutter wiki
    Smooth wall, create rock block, carve mine cart/ fortification
    """

    def __init__(self) -> None:
        self.attributes = {}


class Surgeon(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Focus: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Suturer(Skill):
    """
    Suturing and wound dressing are done by orderlies,
    but their quality is not impacted by any skills, so having all
    dwarves assigned to it has no negative effect.
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Focus: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Tactician(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.AnalyticalAbility: Scores.A,
            SoulAttributes.Creativity: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class Thresher(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Strength: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class WeaponSmith(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class Weaver(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class WoodBurner(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class WoodCrafter(Skill):
    """
    Wooden mug, crafts, instruments, toys, jugs, pots, etc
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class WoodCutter(Skill):
    """
    Due to a bug, the wood cutting labor conflicts with military uniforms.
    A military dwarf with wood cutting enabled will drop his uniform when
    transitioning to civilian duty. To avoid problems it is recommended you
    keep your military and wood cutters separate.
    """

    def __init__(self) -> None:
        # super().__init__()
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Willpower: Scores.C,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class WoundDresser(Skill):
    """
    Suturing and wound dressing are done by orderlies,
    but their quality is not impacted by any skills, so having all
    dwarves assigned to it has no negative effect.
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Empathy: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Skills(Enum):
    # Orderlies
    Brewer = Brewer()
    Fisherdwarf = Fisherdwarf()
    FishCleaner = FishCleaner()
    FurnaceOperator = FurnaceOperator()
    Herbalist = Herbalist()
    Planter = Planter()
    Spinner = Spinner()
    Thresher = Thresher()
    Weaver = Weaver()
    WoodBurner = WoodBurner()
    WoodCutter = WoodCutter()
    Suturer = Suturer()
    WoundDresser = WoundDresser()
    AnimalTrainer = AnimalTrainer()
    Miner = Miner()
    StoneCutter = StoneCutter()

    # Crafting
    Cook = Cook()
    WeaponSmith = WeaponSmith()
    GemCutter = GemCutter()
    Carpenter = Carpenter()
    StoneCarver = StoneCarver()
    StoneCrafter = StoneCrafter()
    WoodCrafter = WoodCrafter()
    Engraving = Engraver()
    Mason = Mason()

    # military
    Discipline = Discipline()
    ArmorUser = ArmorUser()
    Fighter = Fighter()
    Dodger = Dodger()
    # Army
    Tactician = Tactician()
    Leader = Leader()

    # Broker
    Appraiser = Appraiser()
    JudgeOfIntent = JudgeOfIntent()
    Negotiator = Negotiator()

    # Expedition Leader/ Mayor at 50 pop.
    Organizer = Organizer()
    Consoler = Consoler()
    Pacifier = Pacifier()
    # CMD-> do everything in beginning, depend on diagnose skill
    Diagnoser = Diagnoser()

    # Doctor
    BoneDoctor = BoneDoctor()
    Surgeon = Surgeon()

    # Book Keeper
    RecordKeeper = RecordKeeper()

    # Socializing
    Comedian = Comedian()
    Conversationalist = Conversationalist()
    Flatterer = Flatterer()
    Intimidator = Intimidator()
    Liar = Liar()
    Persuader = Persuader()

    # misc.
    Concentration = Concentration()
    Observer = Observer()

    def __call__(self):
        self.value


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


if __name__ == "__main__":
    print(Skills.WoodCutter)  # Skills.WoodCutter
    print(type(Skills.WoodCutter))  # <enum 'Skills'>
    a = Animal("cat")
    print(a)  # <__main__.Animal object at 0x000002462B053850>
    print(type(a))  # <class '__main__.Animal'>
