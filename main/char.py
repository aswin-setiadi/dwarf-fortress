import logging
from typing import TypeVar

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
T = TypeVar("T", BodyAttributes, SoulAttributes)


class Character:
    crafting_related_values = {
        Beliefs.CRAFTSMANSHIP,
        Goals.CREATE_A_GREAT_WORK_OF_ART,
        Goals.CRAFT_A_MASTERWORK,
    }
    # trauma is depression_propensity?
    military_related_values = {
        Beliefs.MARTIAL_PROWESS,
        Beliefs.STOICISM,
        Beliefs.PEACE,
        Beliefs.FAMILY,
        Beliefs.FRIENDSHIP,
        Facets.BRAVERY,
        Facets.STRESS_VULNERABILITY,
        Facets.DEPRESSION_PROPENSITY,
        Facets.ANXIETY_PROPENSITY,
    }

    def __init__(
        self,
        name: str,
        beliefs: dict[Beliefs, Quality],
        goals: set[Goals],
        facets: dict[Facets, Quality],
        attributes: dict[BodyAttributes | SoulAttributes, AttributeType],
    ) -> None:
        self.name = name
        self.beliefs: dict[Beliefs, Quality] = dict(
            (x, Quality.Neutral) for x in Beliefs
        )
        self.goals: set[Goals] = goals
        self.facets: dict[Facets, Quality] = dict((x, Quality.Neutral) for x in Facets)
        self.attributes: dict[
            BodyAttributes | SoulAttributes, AttributeType
        ] = attributes
        self.skills: set[tuple[Skills, int]] = set()
        self.set_beliefs_and_facets(beliefs, facets)
        self.warn_bad_facets()

    def get_conflicted_skills(self) -> set[Skills]:
        conflicted_skills: set[Skills] = set()
        if {Skills.FishCleaner, Skills.Fisherdwarf}.issubset(self.skills):
            conflicted_skills.add(Skills.FishCleaner)
            conflicted_skills.add(Skills.Fisherdwarf)
            logger.warning(f"can't have fishing and fishcleaning in same dwarf...")
        return conflicted_skills

    def set_beliefs_and_facets(
        self, beliefs: dict[Beliefs, Quality], facets: dict[Facets, Quality]
    ):
        for k, v in beliefs.items():
            self.beliefs[k] = v
        for k, v in facets.items():
            self.facets[k] = v

    def warn_bad_facets(self):
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
                f"{self.name} anxiety propensity>0, easier to be {MentalBreakdowns.Oblivious}/{Insanity.StarkRavingMad}"
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

    def calculate_skills(self):
        for skill in Skills:
            # if cant get xp (clashing personality) continue
            if not skill.value.can_get_xp(self.beliefs, self.facets):
                continue
            if skill.value.get_thought_type(self.beliefs) == ThoughtType.UNHAPPY:
                continue
            self.skills.add(skill)
            # TODO
            # check beliefs+facets, if 1 clash, continue
            # score skill based on supporting beliefs/ facets
            # score skill based on supporting attributes

    # def evaluate_skill_score(self, skill: Skills) -> int:
    #     val: int = 0
    #     # 1 skill in 2 roles, the last 1 (military in this case) will hide the first
    #     # need to evaluate attributes first then values?
    #     # crafting
    #     if skill in Roles.Crafter.value:
    #         crafting_clashed_disdains = [
    #             x for x in self.disdains if x in Character.crafting_values
    #         ]
    #         if crafting_clashed_disdains:
    #             print(
    #                 f"{self.name} disdains {crafting_clashed_disdains} clash with {skill}"
    #             )
    #             val = -1
    #     # broker
    #     if skill in Roles.Broker.value:
    #         if Values.Commerce in self.disdains:
    #             print(f"{self.name} disdains {Values.Commerce} clash with {skill}")
    #             return -1
    #     # military
    #     if skill in Roles.MillitaryLeader.value:
    #         military_clashed_disdains = [
    #             x for x in self.disdains if x in Character.military_values
    #         ]
    #         if military_clashed_disdains:
    #             return True

    #         military_clashed_values = [
    #             x for x in self.values if x in Character.military_disdains
    #         ]
    #         if military_clashed_values:
    #             return True
    #     return False

    # def does_values_clash_with_skill(self, skill: Skills) -> bool:
    #     # crafting
    #     if skill in Roles.Crafter.value:
    #         crafting_clashed_disdains = [
    #             x for x in self.disdains if x in Character.crafting_values
    #         ]
    #         if crafting_clashed_disdains:
    #             print(
    #                 f"{self.name} disdains {crafting_clashed_disdains} clash with {skill}"
    #             )
    #             return True
    #     # broker
    #     if skill in Roles.Broker.value:
    #         if Values.Commerce in self.disdains:
    #             print(f"{self.name} disdains {Values.Commerce} clash with {skill}")
    #             return True
    #     # military
    #     if skill in Roles.MillitaryLeader.value:
    #         military_clashed_disdains = [
    #             x for x in self.disdains if x in Character.military_values
    #         ]
    #         if military_clashed_disdains:
    #             return True

    #         military_clashed_values = [
    #             x for x in self.values if x in Character.military_disdains
    #         ]
    #         if military_clashed_values:
    #             return True
    #     return False

    # def does_value_support_skill(self, skill: Skills) -> bool:
    #     # crafting
    #     if skill in Roles.Crafter.value:
    #         crafting_supported_values = [
    #             x for x in self.values if x in Character.crafting_values
    #         ]
    #         if crafting_supported_values:
    #             print(
    #                 f"{self.name} disdains {crafting_supported_values}  support {skill}"
    #             )
    #             return True
    #     # broker
    #     if skill in Roles.Broker.value:
    #         if Values.Commerce in self.values:
    #             print(f"{self.name} disdains {Values.Commerce} clash with {skill}")
    #             return True
    #     # military
    #     if skill in Roles.MillitaryLeader.value:
    #         military_clashed_disdains = [
    #             x for x in self.disdains if x in Character.military_values
    #         ]
    #         if military_clashed_disdains:
    #             return True

    #         military_clashed_values = [
    #             x for x in self.values if x in Character.military_disdains
    #         ]
    #         if military_clashed_values:
    #             return True
    #     return False
