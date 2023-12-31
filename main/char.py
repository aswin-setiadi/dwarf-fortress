from enum import Enum
import logging
from typing import Literal

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
    - Assign facets, beliefs, goals
    - Call add_skills
    - Call get_conflicted_skills to check
    - Call get_suitable roles to check roles

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
        # use Enum to represent both BodyAttributes and SoulAttributes
        self.attributes: dict[Enum, AttributeType] = dict(
            (x, AttributeType.NEUTRAL) for x in Character.atbs
        )
        self.skills: dict[Enum, tuple[int, bool, float]] = {}
        self._set_beliefs_facets_and_attributes(beliefs, facets, attributes)
        self._warn_bad_facets()

    def add_skills(self):
        for skill in Skills:
            if not skill.value.can_get_xp(self.beliefs, self.facets):
                continue
            if skill.value.get_thought_type(self.beliefs) == ThoughtType.UNHAPPY:
                continue

            # check beliefs+facets, if 1 clash, continue
            if skill.value.is_skill_clashes(
                self.beliefs, self.goals, self.facets, self.name
            ):
                continue
            score, goal = skill.value.get_skill_score(
                self.beliefs, self.goals, self.facets
            )
            attribute_score = skill.value.get_skill_attribute_score(self.attributes)
            self.skills[skill] = (score, goal, attribute_score)

    def get_conflicted_skills(self) -> set[str]:
        conflicted_skills: set[str] = set()
        if {Skills.FishCleaner, Skills.Fisherdwarf}.issubset(self.skills):
            conflicted_skills.add(Skills.FishCleaner.value.name())
            conflicted_skills.add(Skills.Fisherdwarf.value.name())
            logger.warning(f"can't have fishing and fishcleaning in same dwarf...")
        return conflicted_skills

    def get_suitable_roles(self) -> list[str]:
        roleslist: list[str] = []
        logger.info(f"printing suitable roles for {self.name}")
        for role in Roles:
            rolescore1 = 0
            rolescore2 = 0
            for skill in role.value:
                if skill in self.skills.keys():
                    rolescore1 += self.skills[skill][0]
                    rolescore2 += self.skills[skill][2]
                if role == Roles.Crafter:
                    break
            roleslist.append(role.name)
            logger.info(f"{role.name:<19}\tb+f={rolescore1}\tatb={rolescore2}")

        return roleslist

    def print_skills(self, sort_by: Literal["bf", "atb"]):
        logger.info(f"printing skills for {self.name} sorted by= {sort_by}")
        l = [(k, v) for k, v in self.skills.items()]
        if sort_by == "bf":
            l.sort(key=lambda x: x[1][0], reverse=True)
        else:
            l.sort(key=lambda x: x[1][2], reverse=True)
        for item in l:
            k = item[0]
            v = item[1]
            if v[1]:
                logger.info(f"{k:<19}\tb+f={v[0]}\tatb={v[2]} goal aligned")
            else:
                logger.info(f"{k:<19}\tb+f={v[0]}\tatb={v[2]}")

    def set_agility(self, v: AttributeType):
        """1000.GOOD4| amazingly agile\n
        750.GOOD3| extremely agile\n
        500.GOOD2| very agile\n
        250.GOOD1| agile\n
        0.NEUTRAL| (no description)\n
        -250.BAD1| clumsy\n
        -500.BAD2| quite clumsy\n
        -750.BAD3| totally clumsy\n
        -1000.BAD4| abysmally clumsy
        """
        self.attributes[BodyAttributes.Agility] = v

    def set_disease_resistance(self, v: AttributeType):
        """ "1000.GOOD4| virtually never sick",\n
        "750.GOOD3| almost never sick",\n
        "500.GOOD2| very rarely sick",\n
        "250.GOOD1| rarely sick",\n
        "0.NEUTRAL| (no description)",\n
        "-250.BAD1| susceptible to disease",\n
        "-500.BAD2| quite susceptible to disease",\n
        "-750.BAD3| really susceptible to disease",\n
        "-1000.BAD4| stunningly susceptible to disease"
        """
        self.attributes[BodyAttributes.DiseaseResistance] = v

    def set_recuperation(self, v: AttributeType):
        """
        1000.GOOD4| possessed of amazing recuperative powers\n
        750.GOOD3| incredibly quick to heal\n
        500.GOOD2| quite quick to heal\n
        250.GOOD1| quick to heal\n
        0.NEUTRAL| (no description)\n
        -250.BAD1| slow to heal\n
        -500.BAD2| very slow to heal\n
        -750.BAD3| really slow to heal\n
        -1000.BAD4| shockingly slow to heal\n
        """
        self.attributes[BodyAttributes.Recuperation] = v

    def set_endurance(self, v: AttributeType):
        """
        1000.GOOD4| absolutely inexhaustible\n
        750.GOOD3| indefatigable\n
        500.GOOD2| very slow to tire\n
        250.GOOD1| slow to tire\n
        0.NEUTRAL| (no description)\n
        -250.BAD1| quick to tire\n
        -500.BAD2| very quick to tire\n
        -750.BAD3| extremely quick to tire\n
        -1000.BAD4| truly quick to tire
        """
        self.attributes[BodyAttributes.Endurance] = v

    def set_strength(self, v: AttributeType):
        """
        1000.GOOD4| unbelievably strong\n
        750.GOOD3| mighty\n
        500.GOOD2| very strong\n
        250.GOOD1| strong\n
        0.NEUTRAL| (no description)\n
        -250.BAD1| weak\n
        -500.BAD2| very weak\n
        -750.BAD3| unquestionably weak\n
        -1000.BAD4| unfathomably weak\n
        """
        self.attributes[BodyAttributes.Strength] = v

    def set_toughness(self, v: AttributeType):
        """
        1000.GOOD4| basically unbreakable\n
        750.GOOD3| incredibly tough\n
        500.GOOD2| quite durable\n
        250.GOOD1| tough\n
        0.NEUTRAL| (no description)\n
        -250.BAD1| flimsy\n
        -500.BAD2| very flimsy\n
        -750.BAD3| remarkably flimsy\n
        -1000.BAD4| shockingly fragile\n
        """
        self.attributes[BodyAttributes.Toughness] = v

    def set_analytical_ability(self, v: AttributeType):
        """
        "1000.GOOD4| awesome intellectual powers",
        "750.GOOD3| great analytical abilities",
        "500.GOOD2| a sharp intellect",
        "250.GOOD1| a good intellect",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| poor analytical abilities",
        "-500.BAD2| very bad analytical abilities",
        "-750.BAD3| a lousy intellect",
        "-1000.BAD4| a stunning lack of analytical ability"
        """
        self.attributes[SoulAttributes.AnalyticalAbility] = v

    def set_creativity(self, v: AttributeType):
        """
        "1000.GOOD4| a boundless creative imagination",
        "750.GOOD3| great creativity",
        "500.GOOD2| very good creativity",
        "250.GOOD1| good creativity",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| meager creativity",
        "-500.BAD2| poor creativity",
        "-750.BAD3| lousy creativity",
        "-1000.BAD4| next to no creative talent"
        """
        self.attributes[SoulAttributes.Creativity] = v

    def set_empath(self, v: AttributeType):
        """
        "1000.GOOD4| an absolutely remarkable sense of others' emotions",
        "750.GOOD3| a great sense of empathy",
        "500.GOOD2| a very good sense of empathy",
        "250.GOOD1| an ability to read emotions fairly well",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| poor empathy",
        "-500.BAD2| a very bad sense of empathy",
        "-750.BAD3| next to no empathy",
        "-1000.BAD4| the utter inability to judge others' emotions"
        """
        self.attributes[SoulAttributes.Empathy] = v

    def set_focus(self, v: AttributeType):
        """
        "1000.GOOD4| unbreakable focus",
        "750.GOOD3| a great ability to focus",
        "500.GOOD2| very good focus",
        "250.GOOD1| the ability to focus",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| poor focus",
        "-500.BAD2| quite poor focus",
        "-750.BAD3| really poor focus",
        "-1000.BAD4| the absolute inability to focus"
        """
        self.attributes[SoulAttributes.Focus] = v

    def set_intuition(self, v: AttributeType):
        """
        "1000.GOOD4| uncanny intuition",
        "750.GOOD3| great intuition",
        "500.GOOD2| very good intuition",
        "250.GOOD1| good intuition",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| bad intuition",
        "-500.BAD2| very bad intuition",
        "-750.BAD3| lousy intuition",
        "-1000.BAD4| horrible intuition"
        """
        self.attributes[SoulAttributes.Intuition] = v

    def set_kinesthesic_sense(self, v: AttributeType):
        """
        "1000.GOOD4| an astounding feel for the position of [his/her] own body",
        "750.GOOD3| a great kinesthetic sense",
        "500.GOOD2| a very good sense of the position of [his/her] own body",
        "250.GOOD1| a good kinesthetic sense",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| a meager kinesthetic sense",
        "-500.BAD2| a poor kinesthetic sense",
        "-750.BAD3| a very clumsy kinesthetic sense",
        "-1000.BAD4| an unbelievably atrocious sense of the position of [his/her] own body"
        """
        self.attributes[SoulAttributes.Kinesthesic] = v

    def set_linguistic_ability(self, v: AttributeType):
        """
        "1000.GOOD4| an astonishing ability with languages and words",
        "750.GOOD3| a great affinity for language",
        "500.GOOD2| a natural inclination toward language",
        "250.GOOD1| a way with words",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| a little difficulty with words",
        "-500.BAD2| little linguistic ability",
        "-750.BAD3| very little linguistic ability",
        "-1000.BAD4| difficulty with words and language"
        """
        self.attributes[SoulAttributes.Language] = v

    def set_memory(self, v: AttributeType):
        """
        "1000.GOOD4| an astonishing memory",
        "750.GOOD3| an amazing memory",
        "500.GOOD2| a great memory",
        "250.GOOD1| a good memory",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| an iffy memory",
        "-500.BAD2| a poor memory",
        "-750.BAD3| a really bad memory",
        "-1000.BAD4| little memory to speak of"
        """
        self.attributes[SoulAttributes.Memory] = v

    def set_musical_ability(self, v: AttributeType):
        """
        "1000.GOOD4| an astonishing knack for music",
        "750.GOOD3| a great musical sense",
        "500.GOOD2| a natural ability with music",
        "250.GOOD1| a feel for music",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| an iffy sense for music",
        "-500.BAD2| little natural inclination toward music",
        "-750.BAD3| next to no natural musical ability",
        "-1000.BAD4| absolutely no feel for music at all"
        """
        self.attributes[SoulAttributes.Music] = v

    def set_patience(self, v: AttributeType):
        """
        "1000.GOOD4| absolutely boundless patience",
        "750.GOOD3| a deep well of patience",
        "500.GOOD2| a great deal of patience",
        "250.GOOD1| a sum of patience",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| a shortage of patience",
        "-500.BAD2| little patience",
        "-750.BAD3| very little patience",
        "-1000.BAD4| no patience at all"
        """
        self.attributes[SoulAttributes.Patience] = v

    def set_social_awareness(self, v: AttributeType):
        """
        "1000.GOOD4| a shockingly profound feel for social relationships",
        "750.GOOD3| a great feel for social relationships",
        "500.GOOD2| a very good feel for social relationships",
        "250.GOOD1| a good feel for social relationships",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| a meager ability with social relationships",
        "-500.BAD2| a poor ability to manage or understand social relationships",
        "-750.BAD3| a lack of understanding of social relationships",
        "-1000.BAD4| an absolute inability to understand social relationships"
        """
        self.attributes[SoulAttributes.SocialAwareness] = v

    def set_spatial_sense(self, v: AttributeType):
        """
        "1000.GOOD4| a stunning feel for spatial relationships",
        "750.GOOD3| an amazing spatial sense",
        "500.GOOD2| a great feel for the surrounding space",
        "250.GOOD1| a good spatial sense",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| a questionable spatial sense",
        "-500.BAD2| poor spatial senses",
        "-750.BAD3| an atrocious spatial sense",
        "-1000.BAD4| no sense for spatial relationships"
        """
        self.attributes[SoulAttributes.SpatialSense] = v

    def set_willpower(self, v: AttributeType):
        """
        "1000.GOOD4| an unbreakable will",
        "750.GOOD3| an iron will",
        "500.GOOD2| a lot of willpower",
        "250.GOOD1| willpower",
        "0.NEUTRAL| (no description)",
        "-250.BAD1| little willpower",
        "-500.BAD2| a large deficit of willpower",
        "-750.BAD3| next to no willpower",
        "-1000.BAD4| absolutely no willpower"
        """
        self.attributes[SoulAttributes.Willpower] = v

    # def set_(self, v: AttributeType):
    #     """

    #     """
    #     self.attributes[Beliefs.]=v
    # def set_(self, v: AttributeType):
    #     """

    #     """
    #     self.attributes[Beliefs.]=v

    # def set_(self, v: AttributeType):
    #     """

    #     """
    #     self.attributes[Beliefs.]=v

    # def set_(self, v: AttributeType):
    #     """

    #     """
    #     self.attributes[Beliefs.]=v

    # def set_(self, v: AttributeType):
    #     """

    #     """
    #     self.attributes[Beliefs.]=v

    # def set_(self, v: AttributeType):
    #     """

    #     """
    #     self.attributes[Beliefs.]=v

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
