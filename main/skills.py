from abc import ABCMeta
from enum import Enum
import logging

from stats import (
    AttributeType,
    Beliefs,
    BodyAttributes,
    Facets,
    Goals,
    Quality,
    Scores,
    SoulAttributes,
    ThoughtType,
)

logger = logging.getLogger(__name__)


class Skill(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.attributes: dict[BodyAttributes | SoulAttributes, Scores] = {}

    # https://stackoverflow.com/questions/11408148/how-to-get-derived-class-name-from-base-class
    def name(self):
        return self.__class__.__name__

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        """Check if beliefs/ facets cause skill unable to get xp"""
        return True

    def get_thought_type(self, beliefs: dict[Beliefs, Quality]) -> ThoughtType:
        """Check if beliefs/ facets cause skill to generate unhappy thoughts"""
        return ThoughtType.NEUTRAL

    def is_skill_clashes(
        self,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
        name: str,
    ) -> bool:
        """Check if skill clashes with any beliefs/ facets"""
        return False

    def get_skill_score(
        self,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
    ) -> tuple[int, bool]:
        """
        Get skill score based on beliefs, facets, and goals.
        Will return tuple of belief+face score (int) and if goal support or not (bool)
        """
        return (0, False)

    def get_skill_attribute_score(self, attributes: dict[Enum, AttributeType]) -> float:
        score = 0
        for atb, weight in self.attributes.items():
            score += attributes[atb] / weight
        return score


class BrokerSkill(Skill):
    def is_skill_clashes(
        self,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
        name: str,
    ) -> bool:
        if beliefs[Beliefs.COMMERCE] < Quality.Neutral:
            return True
        return False


class CraftSkill(Skill):
    def is_skill_clashes(
        self,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
        name: str,
    ) -> bool:
        if beliefs[Beliefs.CRAFTSMANSHIP] < Quality.Neutral:
            logger.warning(f"{name} {Beliefs.CRAFTSMANSHIP} < {Quality.Neutral}")
            return True
        else:
            return False

    def get_skill_score(
        self,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
    ) -> tuple[int, bool]:
        goal = (
            False
            if {Goals.CRAFT_A_MASTERWORK, Goals.CREATE_A_GREAT_WORK_OF_ART}.isdisjoint(
                goals
            )
            else True
        )
        score = 0
        if beliefs[Beliefs.CRAFTSMANSHIP] > Quality.Neutral:
            score += beliefs[Beliefs.CRAFTSMANSHIP]
        return (score, goal)


class MilitarySkill(Skill):
    def is_skill_clashes(
        self,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
        name: str,
    ) -> bool:
        if beliefs[Beliefs.MARTIAL_PROWESS] < Quality.Neutral:
            logger.warning(f"{name} {Beliefs.MARTIAL_PROWESS} > {Quality.Neutral}")
            return True
            # or beliefs[Beliefs.STOICISM] < Quality.Neutral
        if beliefs[Beliefs.PEACE] > Quality.Neutral:
            logger.warning(f"{name} {Beliefs.PEACE} > {Quality.Neutral}")
            return True
            # or beliefs[Beliefs.FAMILY] == Quality.Highest
            # or beliefs[Beliefs.FRIENDSHIP] == Quality.Highest
        if facets[Facets.BRAVERY] < Quality.Neutral:
            logger.warning(f"{name} {Facets.BRAVERY} < {Quality.Neutral}")
            return True
        if facets[Facets.STRESS_VULNERABILITY] > Quality.Neutral:
            logger.warning(f"{name} {Facets.STRESS_VULNERABILITY} > {Quality.Neutral}")
            return True
        if facets[Facets.DEPRESSION_PROPENSITY] > Quality.Neutral:
            logger.warning(f"{name} {Facets.DEPRESSION_PROPENSITY} > {Quality.Neutral}")
            return True
        if facets[Facets.ANXIETY_PROPENSITY] > Quality.Neutral:
            logger.warning(f"{name} {Facets.ANXIETY_PROPENSITY} > {Quality.Neutral}")
            return True
        if Goals.BRING_PEACE_TO_THE_WORLD in goals:
            logger.warning(f"{name}'s goal {Goals.BRING_PEACE_TO_THE_WORLD} conflicts.")
            return True

        return False

    def get_skill_score(
        self,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
    ) -> tuple[int, bool]:
        goal = True if Goals.BECOME_A_LEGENDARY_WARRIOR in goals else False
        score = 0
        score += beliefs[Beliefs.MARTIAL_PROWESS]
        score -= beliefs[Beliefs.PEACE]
        score += facets[Facets.BRAVERY]
        score -= facets[Facets.STRESS_VULNERABILITY]
        score -= facets[Facets.DEPRESSION_PROPENSITY]
        score -= facets[Facets.ANXIETY_PROPENSITY]
        return (score, goal)


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


class Appraiser(BrokerSkill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.AnalyticalAbility: Scores.A,
            SoulAttributes.Memory: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class Archer(MilitarySkill):
    def __init__(self) -> None:
        self.attributes = {
            BodyAttributes.Agility: Scores.A,
            SoulAttributes.SpatialSense: Scores.A,
            SoulAttributes.Kinesthesic: Scores.B,
            SoulAttributes.Focus: Scores.C,
        }


class ArmorSmith(CraftSkill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class ArmorUser(MilitarySkill):
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


class Bowyer(CraftSkill):
    """
    Produces wooden crossbows.
    Although crossbows can also be created from metal by a weaponsmith in a forge,
    the damage a crossbow deals when fired is determined by the weapon's quality
    and not their material. The material only affects damage when dwarves swing
    their crossbows as impromptu hammers during melee combat.
    This skill is not used to make bolts, which requires either wood crafting for
    wooden bolts, bone carving for bone bolts, or weaponsmithing for metal bolts.
    Wiki: https://dwarffortresswiki.org/index.php/Bowyer

    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Brewer(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
        }


class Butcher(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }

    def get_thought_type(self, beliefs: dict[Beliefs, Quality]) -> ThoughtType:
        if beliefs[Beliefs.NATURE] > Quality.High:
            return ThoughtType.UNHAPPY
        if beliefs[Beliefs.NATURE] < Quality.Neutral:
            return ThoughtType.HAPPY
        return ThoughtType.NEUTRAL


class Carpenter(CraftSkill):
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
    merriment
    3 to -1=can,subj to humor
    -2 to -3=cant, subj to humor
    humor
    3 to 2=can
    1 to -1=can,subj to merriment
    -2 to -3=cant
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.Creativity: Scores.B,
            SoulAttributes.Kinesthesic: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        if facets[Facets.HUMOR] < Quality.Low:
            return False
        if Quality.VeryLow < facets[Facets.HUMOR] < Quality.VeryHigh:
            if beliefs[Beliefs.MERRIMENT] < Quality.Low:
                return False
        return True


class Concentration(Skill):
    """absorb military demo"""

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Focus: Scores.A,
            SoulAttributes.Patience: Scores.B,
            SoulAttributes.Willpower: Scores.C,
        }


class Consoler(Skill):
    """empath, language, social awareness"""

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Empathy: Scores.A,
            SoulAttributes.Language: Scores.B,
            SoulAttributes.SocialAwareness: Scores.C,
        }

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        """
        stoic -3 to 1= can learn subject to sway, cruel, discord
        stoic 2 to 3=cant subject to sway,cruel, discord

        discord 3,2= cant
        discord 1,0,-1=can subject to stoic,cruelty,sway
        discord -2,-3=can subject to cruel,sway

        cruel 3,2=cant
        cruel 1,0,-1=can subject to stoic, discord, sway
        cruel -2,-3=can subject to discord, sway

        sway 3,2= can subj to cruel, discord
        sway 1,0,-1=can subject to stoic,cruel,discord
        sway -2,-3=cant
        """
        if (
            facets[Facets.DISCORD] > Quality.High
            or facets[Facets.CRUELTY] > Quality.High
            or facets[Facets.SWAYED_BY_EMOTIONS] < Quality.Low
        ):
            return False

        if (
            beliefs[Beliefs.STOICISM] > Quality.High
            and facets[Facets.DISCORD] > Quality.VeryLow
            and facets[Facets.CRUELTY] > Quality.VeryLow
            and facets[Facets.SWAYED_BY_EMOTIONS] < Quality.VeryHigh
        ):
            return False
        return True


class Conversationalist(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        """
        friendship
        3 to -1=maybe can, subj to leisure?, gregarious, bashful
        -2 to -3=maybe cant, subj to gregarious, bashful
        leisure
        3 to -1=maybe can, subj to friend?, gregarious, bashful
        -2 to -3= maybe cant, subj to gregarious, bashful
        bashful
        3 to 2=cant
        1 to -1= can, subj to beliefs, gregarious (I assume belief here is friend,leisure)
        -2 to -3= can, subj to gregarious
        gregarious
        3 to 2= can, subj to bashful
        1 to -1=can, subj to beliefs, bashful (same as above assumption)
        -2 to -3= cant
        """
        if (
            facets[Facets.BASHFUL] > Quality.High
            or facets[Facets.GREGARIOUSNESS] < Quality.Low
        ):
            return False
        if (
            Quality.Low <= facets[Facets.BASHFUL] <= Quality.High
            and Quality.Low <= facets[Facets.GREGARIOUSNESS] <= Quality.High
        ):
            if (
                beliefs[Beliefs.FRIENDSHIP] < Quality.Low
                or beliefs[Beliefs.LEISURE_TIME] < Quality.Low
            ):
                return False
        return True


class Cook(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.AnalyticalAbility: Scores.B,
            SoulAttributes.Creativity: Scores.C,
            BodyAttributes.Agility: Scores.A,
        }


class Crossbowman(MilitarySkill):
    def __init__(self) -> None:
        self.attributes = {
            BodyAttributes.Agility: Scores.A,
            SoulAttributes.SpatialSense: Scores.A,
            SoulAttributes.Kinesthesic: Scores.B,
            SoulAttributes.Focus: Scores.C,
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
    Military less likely to route.
    Medic keep away from panic when lose a patient when others waiting.
    Active military training raise discipline rather quickly.
    Exposed to dead body, rain, cancelling jobs due to "horrified" also raise it.
    Creature naturally high stress and horror tolerance hard to train discipline.
    """

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Willpower: Scores.A,
            SoulAttributes.Focus: Scores.B,
        }


class Dodger(MilitarySkill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.SpatialSense: Scores.B,
            SoulAttributes.Willpower: Scores.C,
            BodyAttributes.Agility: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.B,
        }


class Engraver(CraftSkill):
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


class Fighter(MilitarySkill):
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

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        """
        truth
        3 to 2=cant, unless friendliness
        1 to -3=can, subj to friendlines
        friendliness
        3 to 2=can
        1 to -1=can, subj to truth
        -2 to 3=cant
        """
        if facets[Facets.FRIENDLINESS] < Quality.Low:
            return False
        if Quality.VeryLow < facets[Facets.FRIENDLINESS] < Quality.VeryHigh:
            if beliefs[Beliefs.TRUTH] > Quality.High:
                return False
        return True


class FurnaceOperator(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.AnalyticalAbility: Scores.B,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Toughness: Scores.B,
            BodyAttributes.Endurance: Scores.C,
        }


class GemCutter(CraftSkill):
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

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        """
        belief power
        3 to -1=can, subj to harmony, tranquility, assertiveness,discord
        -2 to -3=cant, subj to assertiveness,discord
        belief tranquility
        3 to 2=cant, subj to assertiveness,discord
        1 to -3=can, subj to power, assertiveness,discord
        belief harmony
        3 to 2=cant, subj to assertiveness,discord
        1 to -3=can, subj to power, tranquility,assertiveness,discord
        facet discord
        3 to 2=can,subj to assertiveness
        1 to -1=can,subj to harmony,power,tranquility,assertiveness
        -2 to -3=cant
        facet assertiveness
        3 to 2=can,subj to discord
        1 to -1=can,subj to harmony,power,tranquility,discord
        -2 to -3=cant
        """
        if (
            facets[Facets.DISCORD] < Quality.Low
            or facets[Facets.ASSERTIVENESS] < Quality.Low
        ):
            return False
        if (
            Quality.VeryLow < facets[Facets.DISCORD] < Quality.VeryHigh
            and Quality.VeryLow < facets[Facets.ASSERTIVENESS] < Quality.VeryHigh
        ):
            if (
                beliefs[Beliefs.POWER] < Quality.Low
                or Quality.High < beliefs[Beliefs.TRANQUILITY]
                or Quality.High < beliefs[Beliefs.HARMONY]
            ):
                return False

        return True


class JudgeOfIntent(BrokerSkill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Empathy: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class Leader(MilitarySkill):
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

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        if beliefs[Beliefs.TRUTH] > Quality.Neutral:
            return False
        else:
            return True


class Mason(CraftSkill):
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


class Negotiator(BrokerSkill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }


class Observer(Skill):
    """Detect stealth, good for entrance guard/ marksdwarf on wall"""

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.SpatialSense: Scores.A,
            SoulAttributes.Focus: Scores.B,
            SoulAttributes.Intuition: Scores.C,
        }


class Organizer(Skill):
    """analytics, social awareness, creativity"""

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.AnalyticalAbility: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Creativity: Scores.C,
        }


class Pacifier(Skill):
    """language, social awareness, empathy"""

    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        """
        belief peace
        3 to -1= can, subj to discord
        -2 to -3= cant, subj to discord
        facet discord
        3 to 2=cant
        1 to -1=can,subj to peace
        -2 to -3=can
        """
        if facets[Facets.DISCORD] > Quality.High:
            return False
        if Quality.VeryLow < facets[Facets.DISCORD] < Quality.VeryHigh:
            if beliefs[Beliefs.PEACE] < Quality.Low:
                return False
        return True


class Persuader(Skill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Language: Scores.A,
            SoulAttributes.SocialAwareness: Scores.B,
            SoulAttributes.Empathy: Scores.C,
        }

    def can_get_xp(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ) -> bool:
        """
        belief eloquence
        3 to -1= can, subj to assertiveness
        -2 to -3= cant, subj to assertiveness
        facet assertiveness
        3 to 2=can
        1 to -1=can,subj to assertiveness
        -2 to -3=cant
        """
        if facets[Facets.ASSERTIVENESS] < Quality.Low:
            return False
        if Quality.VeryLow < facets[Facets.ASSERTIVENESS] < Quality.VeryHigh:
            if beliefs[Beliefs.ELOQUENCE] < Quality.Low:
                return False
        return True


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


class StoneCarver(CraftSkill):
    """
    Produces stone furniture(table chair door), slab for tomb, statue
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


class StoneCrafter(CraftSkill):
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


class Sword(MilitarySkill):
    def __init__(self) -> None:
        self.attributes = {
            SoulAttributes.Kinesthesic: Scores.A,
            SoulAttributes.Willpower: Scores.B,
            SoulAttributes.SpatialSense: Scores.C,
            BodyAttributes.Strength: Scores.A,
            BodyAttributes.Agility: Scores.B,
            BodyAttributes.Toughness: Scores.C,
        }


class Tactician(MilitarySkill):
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


class WeaponSmith(CraftSkill):
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


class WoodCrafter(CraftSkill):
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

    def get_thought_type(self, beliefs: dict[Beliefs, Quality]) -> ThoughtType:
        if beliefs[Beliefs.NATURE] > Quality.High:
            return ThoughtType.UNHAPPY
        if beliefs[Beliefs.NATURE] < Quality.Neutral:
            return ThoughtType.HAPPY
        return ThoughtType.NEUTRAL


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
    Butcher = Butcher()
    Fisherdwarf = Fisherdwarf()
    FishCleaner = FishCleaner()
    FurnaceOperator = FurnaceOperator()
    Herbalist = Herbalist()
    Planter = Planter()
    Spinner = Spinner()  # spin wool
    Thresher = Thresher()  # spin plant
    Weaver = Weaver()  # thread (including spider silk) to cloth
    WoodBurner = WoodBurner()
    WoodCutter = WoodCutter()
    Suturer = Suturer()
    WoundDresser = WoundDresser()
    AnimalTrainer = AnimalTrainer()
    Miner = Miner()
    StoneCutter = StoneCutter()
    # Successfully completing the 'capture a live land animal' task
    # fulfills a dwarf's 'do something exciting' need.
    # Trapper = Trapper()
    # Tanner = Tanner()

    # Crafting
    Cook = Cook()
    Bowyer = Bowyer()
    WeaponSmith = WeaponSmith()
    ArmorSmith = ArmorSmith()
    GemCutter = GemCutter()
    Carpenter = Carpenter()
    StoneCarver = StoneCarver()
    StoneCrafter = StoneCrafter()
    WoodCrafter = WoodCrafter()
    Engraver = Engraver()
    Mason = Mason()

    # military
    Discipline = Discipline()  # easy to increase w. basic mil. training.
    Sword = Sword()
    ArmorUser = ArmorUser()
    Fighter = Fighter()
    Dodger = Dodger()
    # Army
    Tactician = Tactician()
    Leader = Leader()
    # Hunter
    Archer = Archer()
    Crossbowman = Crossbowman()

    # Broker
    Appraiser = Appraiser()
    JudgeOfIntent = JudgeOfIntent()
    Negotiator = Negotiator()

    # Manager
    Organizer = Organizer()
    # Expedition Leader/ Mayor at 50 pop.
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

    @classmethod
    def list(cls) -> list[Skill]:
        """return list of Skill based obj"""
        # return list(map(lambda x: x.value, cls))
        return [x.value for x in cls]

    def __call__(self):
        self.value

    # no effect when print with f
    # def __repr__(self) -> str:
    #     return f"{self.name}"

    def __str__(self) -> str:
        return f"{self.name}"


if __name__ == "__main__":
    print(Skills.WoodCutter)  # Skills.WoodCutter
    print(type(Skills.WoodCutter))  # <enum 'Skills'>
    print(Skills.WoodBurner.name)
