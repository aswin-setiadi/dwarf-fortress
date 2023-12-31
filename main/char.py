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

    def set_craftsmanship(self, v: Quality):
        """3.Highest| holds crafts[man]ship to be of the highest ideals and celebrates talented artisans and their masterworks\n
        2.VeryHigh| has a great deal of respect for worthy crafts[man]ship\n
        1.High| values good crafts[man]ship\n
        0.Neutral| doesn't particularly care about crafts[man]ship\n
        -1.Low| considers crafts[man]ship to be relatively worthless\n
        -2.VeryLow| sees the pursuit of good crafts[man]ship as a total waste\n
        -3.Lowest| views crafts[man]ship with disgust and would desecrate a so-called masterwork or two if [he/she] could get away with it\n
        """
        self.beliefs[Beliefs.CRAFTSMANSHIP] = v

    def set_cunning(self, v: Quality):
        """3.Highest| holds well-laid plans and shrewd deceptions in the highest regard\n
        2.VeryHigh| greatly respects the shrewd and guileful\n
        1.High| values cunning\n
        0.Neutral| does not really value cunning and guile\n
        -1.Low| sees guile and cunning as indirect and somewhat worthless\n
        -2.VeryLow| holds shrewd and crafty individuals in the lowest esteem\n
        -3.Lowest| is utterly disgusted by guile and cunning\n"""
        self.beliefs[Beliefs.CUNNING] = v

    def set_decorum(self, v: Quality):
        """3.Highest| views decorum as a high ideal and is deeply offended by those that fail to maintain it\n
        2.VeryHigh| greatly respects those that observe decorum and maintain their dignity\n
        1.High| values decorum, dignity and proper behavior\n
        0.Neutral| doesn't care very much about decorum\n
        -1.Low| finds maintaining decorum a silly, fumbling waste of time\n
        -2.VeryLow| sees those that attempt to maintain dignified and proper behavior as vain and offensive\n
        -3.Lowest| is affronted by the whole notion of maintaining decorum and finds so-called dignified people disgusting\n
        """
        self.beliefs[Beliefs.DECORUM] = v

    def set_eloquence(self, v: Quality):
        """3.Highest| believes that artful speech and eloquent expression are some of the highest ideals\n
        2.VeryHigh| deeply respects eloquent speakers\n
        1.High| values eloquence\n
        0.Neutral| doesn't value eloquence so much\n
        -1.Low| finds eloquence and artful speech off-putting\n
        -2.VeryLow| finds [him/her]self somewhat disgusted with eloquent speakers\n
        -3.Lowest| sees artful speech and eloquence as a wasteful form of deliberate deception and treats it as such\n
        """
        self.beliefs[Beliefs.ELOQUENCE] = v

    def set_fairness(self, v: Quality):
        """3.Highest| holds fairness as one of the highest ideals and despises cheating of any kind\n
        2.VeryHigh| has great respect for fairness\n
        1.High| respects fair-dealing and fair-play\n
        0.Neutral| does not care about fairness\n
        -1.Low| sees life as unfair and doesn't mind it that way\n
        -2.VeryLow| finds the idea of fair-dealing foolish and cheats when [he/she] finds it profitable\n
        -3.Lowest| is disgusted by the idea of fairness and will freely cheat anybody at any time\n
        """
        self.beliefs[Beliefs.FAIRNESS] = v

    def set_family(self, v: Quality):
        """3.Highest| sees family as one of the most important things in life\n
        2.VeryHigh| values family greatly\n
        1.High| values family\n
        0.Neutral| does not care about family one way or the other\n
        -1.Low| is put off by family\n
        -2.VeryLow| lacks any respect for family\n
        -3.Lowest| finds the idea of family loathsome\n"""
        self.beliefs[Beliefs.FAMILY] = v

    def set_friendship(self, v: Quality):
        """3.Highest| believes friendship is a key to the ideal life\n
        2.VeryHigh| sees friendship as one of the finer things in life\n
        1.High| thinks friendship is important\n
        0.Neutral| does not care about friendship\n
        -1.Low| finds friendship burdensome\n
        -2.VeryLow| is completely put off by the idea of friends\n
        -3.Lowest| finds the whole idea of friendship disgusting\n"""
        self.beliefs[Beliefs.FRIENDSHIP] = v

    def set_hard_work(self, v: Quality):
        """3.Highest| believes that hard work is one of the highest ideals and a key to the good life\n
        2.VeryHigh| deeply respects those that work hard at their labors\n
        1.High| values hard work\n
        0.Neutral| doesn't really see the point of working hard\n
        -1.Low| sees working hard as a foolish waste of time\n
        -2.VeryLow| thinks working hard is an abject idiocy\n
        -3.Lowest| finds the proposition that one should work hard in life utterly abhorrent\n
        """
        self.beliefs[Beliefs.HARD_WORK] = v

    def set_harmony(self, v: Quality):
        """3.Highest| would have the world operate in complete harmony without the least bit of strife or disorder\n
        2.VeryHigh| strongly believes that a peaceful and ordered society without dissent is best\n
        1.High| values a harmonious existence\n
        0.Neutral| sees equal parts of harmony and discord as part of life\n
        -1.Low| doesn't respect a society that has settled into harmony without debate and strife\n
        -2.VeryLow| can't fathom why anyone would want to live in an orderly and harmonious society\n
        -3.Lowest| believes deeply that chaos and disorder are the truest expressions of life and would disrupt harmony wherever it is found\n
        """
        self.beliefs[Beliefs.HARMONY] = v

    def set_independence(self, v: Quality):
        """3.Highest| believes that freedom and independence are completely non-negotiable and would fight to defend them\n
        2.VeryHigh| treasures independence\n
        1.High| values independence\n
        0.Neutral| doesn't really value independence one way or another\n
        -1.Low| finds the ideas of independence and freedom somewhat foolish\n
        -2.VeryLow| sees freedom and independence as completely worthless\n
        -3.Lowest| hates freedom and would crush the independent spirit wherever it is found\n
        """
        self.beliefs[Beliefs.INDEPENDENCE] = v

    def set_introspection(self, v: Quality):
        """3.Highest| feels that introspection and all forms of self-examination are the keys to a good life and worthy of respect\n
        2.VeryHigh| deeply values introspection\n
        1.High| sees introspection as important\n
        0.Neutral| doesn't really see the value in self-examination\n
        -1.Low| finds introspection to be a waste of time\n
        -2.VeryLow| thinks that introspection is valueless and those that waste time in self-examination are deluded fools\n
        -3.Lowest| finds the whole idea of introspection completely offensive and contrary to the ideals of a life well-lived\n
        """
        self.beliefs[Beliefs.INTROSPECTION] = v

    def set_knowledge(self, v: Quality):
        """3.Highest| finds the quest for knowledge to be of the very highest value\n
        2.VeryHigh| views the pursuit of knowledge as deeply important\n
        1.High| values knowledge\n
        0.Neutral| doesn't see the attainment of knowledge as important\n
        -1.Low| finds the pursuit of knowledge to be a waste of effort\n
        -2.VeryLow| thinks the quest for knowledge is a delusional fantasy\n
        -3.Lowest| sees the attainment and preservation of knowledge as an offensive enterprise engaged in by arrogant fools\n
        """
        self.beliefs[Beliefs.KNOWLEDGE] = v

    def set_law(self, v: Quality):
        """3.Highest| is an absolute believer in the rule of law\n
        2.VeryHigh| has a great deal of respect for the law\n
        1.High| respects the law\n
        0.Neutral| doesn't feel strongly about the law\n
        -1.Low| does not respect the law\n
        -2.VeryLow| disdains the law\n
        -3.Lowest| finds the idea of laws abhorrent\n"""
        self.beliefs[Beliefs.LAW] = v

    def set_leisure_time(self, v: Quality):
        """3.Highest| believes that it would be a fine thing if all time were leisure time\n
        2.VeryHigh| treasures leisure time and thinks it is very important in life\n
        1.High| values leisure time\n
        0.Neutral| doesn't think one way or the other about leisure time\n
        -1.Low| finds leisure time wasteful\n
        -2.VeryLow| is offended by leisure time and leisurely living\n
        -3.Lowest| believes that those that take leisure time are evil and finds the whole idea disgusting\n
        """
        self.beliefs[Beliefs.LEISURE_TIME] = v

    def set_loyalty(self, v: Quality):
        """3.Highest| has the highest regard for loyalty\n
        2.VeryHigh| greatly prizes loyalty\n
        1.High| values loyalty\n
        0.Neutral| doesn't particularly value loyalty\n
        -1.Low| views loyalty unfavorably\n
        -2.VeryLow| disdains loyalty\n
        -3.Lowest| is disgusted by the idea of loyalty\n"""
        self.beliefs[Beliefs.LOYALTY] = v

    def set_martial_prowess(self, v: Quality):
        """3.Highest| believes that martial prowess defines the good character of an individual\n
        2.VeryHigh| deeply respects skill at arms\n
        1.High| values martial prowess\n
        0.Neutral| does not really value skills related to fighting\n
        -1.Low| finds those that develop skill with weapons and fighting distasteful\n
        -2.VeryLow| thinks that the pursuit of the skills of warfare and fighting is a low pursuit indeed\n
        -3.Lowest| abhors those that pursue the mastery of weapons and skill with fighting\n
        """
        self.beliefs[Beliefs.MARTIAL_PROWESS] = v

    def set_merriment(self, v: Quality):
        """3.Highest| believes that little is better in life than a good party\n
        2.VeryHigh| truly values merrymaking and parties\n
        1.High| finds merrymaking and partying worthwhile activities\n
        0.Neutral| doesn't really value merrymaking\n
        -1.Low| sees merrymaking as a waste\n
        -2.VeryLow| is disgusted by merrymakers\n
        -3.Lowest| is appalled by merrymaking, parties and other such worthless activities\n
        """
        self.beliefs[Beliefs.MERRIMENT] = v

    def set_nature(self, v: Quality):
        """3.Highest| holds nature to be of greater value than most aspects of civilization\n
        2.VeryHigh| has a deep respect for animals, plants and the natural world\n
        1.High| values nature\n
        0.Neutral| doesn't care about nature one way or another\n
        -1.Low| finds nature somewhat disturbing\n
        -2.VeryLow| has a deep dislike of the natural world\n
        -3.Lowest| would just as soon have nature and the great outdoors burned to ashes and converted into a great mining pit\n
        """
        self.beliefs[Beliefs.NATURE] = v

    def set_peace(self, v: Quality):
        """3.Highest| believes the idea of war is utterly repellent and would have peace at all costs\n
        2.VeryHigh| believes that peace is always preferable to war\n
        1.High| values peace over war\n
        0.Neutral| doesn't particularly care between war and peace\n
        -1.Low| sees war as a useful means to an end\n
        -2.VeryLow| believes war is preferable to peace in general\n
        -3.Lowest| thinks that the world should be engaged in perpetual warfare\n"""
        self.beliefs[Beliefs.PEACE] = v

    def set_perseverance(self, v: Quality):
        """3.Highest| believes that perseverance is one of the greatest qualities somebody can have\n
        2.VeryHigh| greatly respects individuals that persevere through their trials and labors\n
        1.High| respects perseverance\n
        0.Neutral| doesn't think much about the idea of perseverance\n
        -1.Low| sees perseverance in the face of adversity as bull-headed and foolish\n
        -2.VeryLow| thinks there is something deeply wrong with people that persevere through adversity\n
        -3.Lowest| finds the notion that one would persevere through adversity completely abhorrent\n
        """
        self.beliefs[Beliefs.PERSEVERANCE] = v

    def set_power(self, v: Quality):
        """3.Highest| believes that the acquisition of power over others is the ideal goal in life and worthy of the highest respect\n
        2.VeryHigh| sees power over others as something to strive for\n
        1.High| respects power\n
        0.Neutral| doesn't find power particularly praiseworthy\n
        -1.Low| has a negative view of those who exercise power over others\n
        -2.VeryLow| hates those who wield power over others\n
        -3.Lowest| finds the acquisition and use of power abhorrent and would have all masters toppled\n
        """
        self.beliefs[Beliefs.POWER] = v

    def set_romance(self, v: Quality):
        """3.Highest| sees romance as one of the highest ideals\n
        2.VeryHigh| thinks romance is very important in life\n
        1.High| values romance\n
        0.Neutral| doesn't care one way or the other about romance\n
        -1.Low| finds romance distasteful\n
        -2.VeryLow| is somewhat disgusted by romance\n
        -3.Lowest| finds even the abstract idea of romance repellent\n"""
        self.beliefs[Beliefs.ROMANCE] = v

    def set_sacrifice(self, v: Quality):
        """3.Highest| finds sacrifice to be one of the highest ideals\n
        2.VeryHigh| believes that those who sacrifice for others should be deeply respected\n
        1.High| values sacrifice\n
        0.Neutral| doesn't particularly respect sacrifice as a virtue\n
        -1.Low| sees sacrifice as wasteful and foolish\n
        -2.VeryLow| finds sacrifice to be the height of folly\n
        -3.Lowest| thinks that the entire concept of sacrifice for others is truly disgusting\n
        """
        self.beliefs[Beliefs.SACRIFICE] = v

    def set_self_control(self, v: Quality):
        """3.Highest| believes that self-mastery and the denial of impulses are some of the highest ideals\n
        2.VeryHigh| finds moderation and self-control to be very important\n
        1.High| values self-control\n
        0.Neutral| doesn't particularly value self-control\n
        -1.Low| finds those that deny their impulses somewhat stiff\n
        -2.VeryLow| sees the denial of impulses as a vain and foolish pursuit\n
        -3.Lowest| has abandoned any attempt at self-control and finds the whole concept deeply offensive\n
        """
        self.beliefs[Beliefs.SELF_CONTROL] = v

    def set_skill_belief(self, v: Quality):
        """3.Highest| believes that the mastery of a skill is one of the highest pursuits\n
        2.VeryHigh| really respects those that take the time to master a skill\n
        1.High| respects the development of skill\n
        0.Neutral| doesn't care if others take the time to master skills\n
        -1.Low| finds the pursuit of skill mastery off-putting\n
        -2.VeryLow| believes that the time taken to master a skill is a horrible waste\n
        -3.Lowest| sees the whole idea of taking time to master a skill as appalling\n
        """
        self.beliefs[Beliefs.SKILL] = v

    def set_stoicism(self, v: Quality):
        """3.Highest| views any show of emotion as offensive\n
        2.VeryHigh| thinks it is of the utmost importance to present a bold face and never grouse, complain or even show emotion\n
        1.High| believes it is important to conceal emotions and refrain from complaining\n
        0.Neutral| doesn't see much value in being stoic\n
        -1.Low| sees no value in holding back complaints and concealing emotions\n
        -2.VeryLow| feels that those who attempt to conceal their emotions are vain and foolish\n
        -3.Lowest| sees concealment of emotions as a betrayal and tries [his/her] best never to associate with such secretive fools\n
        """
        self.beliefs[Beliefs.STOICISM] = v

    def set_tradition(self, v: Quality):
        """3.Highest| holds the maintenance of tradition as one of the highest ideals\n
        2.VeryHigh| is a firm believer in the value of tradition\n
        1.High| values tradition\n
        0.Neutral| doesn't have any strong feelings about tradition\n
        -1.Low| disregards tradition\n
        -2.VeryLow| finds the following of tradition foolish and limiting\n
        -3.Lowest| is disgusted by tradition and would flout any [he/she] encounters if given a chance\n
        """
        self.beliefs[Beliefs.TRADITION] = v

    def set_tranquility(self, v: Quality):
        """3.Highest| views tranquility as one of the highest ideals\n
        2.VeryHigh| strongly values tranquility and quiet\n
        1.High| values tranquility and a peaceful day\n
        0.Neutral| doesn't have a preference between tranquility and tumult\n
        -1.Low| prefers a noisy, bustling life to boring days without activity\n
        -2.VeryLow| is greatly disturbed by quiet and a peaceful existence\n
        -3.Lowest| is disgusted by tranquility and would that the world would constantly churn with noise and activity\n
        """
        self.beliefs[Beliefs.TRANQUILITY] = v

    def set_truth(self, v: Quality):
        """3.Highest| believes the truth is inviolable regardless of the cost\n
        2.VeryHigh| believes that honesty is a high ideal\n
        1.High| values honesty\n
        0.Neutral| does not particularly value the truth\n
        -1.Low| finds blind honesty foolish\n
        -2.VeryLow| sees lying as an important means to an end\n
        -3.Lowest| is repelled by the idea of honesty and lies without compunction\n"""
        self.beliefs[Beliefs.TRUTH] = v

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
