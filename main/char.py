from enum import Enum
import logging

from roles import Roles
from skills import Skills
from stats import (
    AttributeType,
    Beliefs,
    BodyAttributes,
    Facets,
    Goals,
    Insanity,
    MentalBreakdowns,
    Quality,
    SoulAttributes,
    ThoughtType,
)

logger = logging.getLogger(__name__)


class Character:
    """
    How to use:
    - Instantiate obj
    - Call add_skills
    - Call get_conflicted_skills to check

    """

    crafting_related_values = {
        Beliefs.CRAFTSMANSHIP,
        Goals.CREATE_A_GREAT_WORK_OF_ART,
        Goals.CRAFT_A_MASTERWORK,
    }
    # trauma is depression_propensity?
    military_related_values = {
        Goals.BECOME_A_LEGENDARY_WARRIOR,
        Goals.BRING_PEACE_TO_THE_WORLD,
        Beliefs.MARTIAL_PROWESS,
        # Beliefs.STOICISM,
        Beliefs.PEACE,
        # Beliefs.FAMILY,
        # Beliefs.FRIENDSHIP,
        Facets.BRAVERY,
        Facets.STRESS_VULNERABILITY,
        Facets.DEPRESSION_PROPENSITY,
        Facets.ANXIETY_PROPENSITY,
    }
    atbs: list[BodyAttributes | SoulAttributes] = list(BodyAttributes) + list(
        SoulAttributes
    )

    def __init__(
        self,
        name: str,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
        attributes: dict[Enum, AttributeType],
    ) -> None:
        self.name = name
        self.beliefs: dict[Beliefs, Quality] = dict(
            (x, Quality.Neutral) for x in Beliefs
        )
        self.goals: set[Goals] = goals
        self.facets: dict[Facets, Quality] = dict((x, Quality.Neutral) for x in Facets)
        self.attributes: dict[Enum, AttributeType] = dict(
            (x, AttributeType.NEUTRAL) for x in Character.atbs
        )
        self.skills: set[tuple[Skills, int, bool, float]] = set()
        self._set_beliefs_facets_and_attributes(beliefs, facets, attributes)
        self._warn_bad_facets()

    def add_skills(self):
        for skill in Skills:
            if not skill.value.can_get_xp(self.beliefs, self.facets):
                continue
            if skill.value.get_thought_type(self.beliefs) == ThoughtType.UNHAPPY:
                continue

            # check beliefs+facets, if 1 clash, continue
            if skill.value.is_skill_clashes(self.beliefs, self.goals, self.facets):
                continue
            score, goal = skill.value.get_skill_score(
                self.beliefs, self.goals, self.facets
            )
            attribute_score = skill.value.get_skill_attribute_score(self.attributes)
            self.skills.add((skill, score, goal, attribute_score))

    def get_conflicted_skills(self) -> set[Skills]:
        conflicted_skills: set[Skills] = set()
        if {Skills.FishCleaner, Skills.Fisherdwarf}.issubset(self.skills):
            conflicted_skills.add(Skills.FishCleaner)
            conflicted_skills.add(Skills.Fisherdwarf)
            logger.warning(f"can't have fishing and fishcleaning in same dwarf...")
        return conflicted_skills

    def print_skills(self):
        for sk in self.skills:
            logger.info(
                f"{sk[0]}\tb+f={sk[1]}\tgoal aligned={sk[2]}\tatb score={sk[3]}"
            )

    def _set_beliefs_facets_and_attributes(
        self,
        beliefs: dict[Beliefs, Quality],
        facets: dict[Facets, Quality],
        attributes: dict[Enum, AttributeType],
    ):
        for k, v in beliefs.items():
            self.beliefs[k] = v
        for k, v in facets.items():
            self.facets[k] = v
        for k, v in attributes.items():
            self.attributes[k] = v

    def _warn_bad_facets(self):
        if self.facets[Facets.CHEER_PROPENSITY] < Quality.Neutral:
            logger.warning(
                f"{self.name} cheer propensity <0, can't generate + thought while drinking..."
            )
        if self.facets[Facets.CHEER_PROPENSITY] < Quality.Low:
            logger.warning(
                f"{self.name} cheer propensity <-1, can't generate + thought while working on preference... "
            )

        if self.facets[Facets.DEPRESSION_PROPENSITY] > Quality.Neutral:
            logger.warning(
                f"{self.name} depression propensity>0, easy to get {MentalBreakdowns.Depression} and get {Insanity.Melancholy}..."
            )

        if self.facets[Facets.ANGER_PROPENSITY] > Quality.Neutral:
            logger.warning(
                f"{self.name} anger propensity>0, easy to throw {MentalBreakdowns.Tantrum}/ {Insanity.Berserk}, unmet need and argument may trigger - thought 'frustation'"
            )

        if self.facets[Facets.ANXIETY_PROPENSITY] > Quality.Neutral:
            logger.warning(
                f"{self.name} anxiety propensity>0, easier to be {MentalBreakdowns.Oblivious}/ {Insanity.StarkRavingMad}"
            )

        if self.facets[Facets.STRESS_VULNERABILITY] == Quality.Highest:
            logger.warning(
                f"{self.name} stress vulnerability==3, 50% chance {Insanity.Catatonic}"
            )

        if self.facets[Facets.DISCORD] > Quality.Neutral:
            logger.info(f"{self.name} discord>0, arguments can trigger + thoughts")
        if self.facets[Facets.PRIDE] > Quality.Neutral:
            logger.warning(
                f"{self.name} pride>0, arguments may trigger - thought (subject to discord), teaching at guild hall + thought"
            )
        if self.facets[Facets.EMOTIONALLY_OBSESSIVE]:
            logger.warning(
                f"{self.name} emotionally_obsessive==-3, no feel when see death, still exp trauma/ fear based on other personality"
            )
        if self.facets[Facets.ALTRUISM] > Quality.Neutral:
            logger.warning(
                f"{self.name} altruism>0, get happy thought from recovering wounded"
            )
        elif self.facets[Facets.ALTRUISM] < Quality.Low:
            logger.warning(
                f"{self.name} altruism<-1, get unhappy thought from recovering wounded"
            )
        if self.facets[Facets.ORDERLINESS] > Quality.Neutral:
            logger.warning(f"{self.name} orderliness>0, will store cloth after change")
        elif self.facets[Facets.ORDERLINESS] < Quality.Neutral:
            logger.warning(
                f"{self.name} orderliness<0, will leave scattered cloth after change"
            )
