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
        gender: Literal["male", "female"],
        goals: set[Goals],
    ) -> None:
        """
        Character class
        name= name of char
        attributes= dict, with BodyAttributes/ SoulAttributes as key and AttributeType as value
        beliefs= dict, with Beliefs class as key and Quality as value
        facets= dict, with Facets class as key and Quality as value
        goals= set of Goals
        skills= dict, with Skills as key and tuple(bf_score, is_goal_aligned, atb_score) as value
        """
        self.name = name
        self.gender: Literal["male", "female"] = gender
        self.beliefs: dict[Beliefs, Quality] = dict(
            (x, Quality.Neutral) for x in Beliefs
        )
        self.goals: set[Goals] = goals
        self.facets: dict[Facets, Quality] = dict((x, Quality.Neutral) for x in Facets)
        # use Enum to represent both BodyAttributes and SoulAttributes
        self.attributes: dict[Enum, AttributeType] = dict(
            (x, AttributeType.n) for x in Character.atbs
        )
        self.skills: dict[Enum, tuple[int, bool, float]] = {}

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
        """1000.GOOD4| virtually never sick\n
        750.GOOD3| almost never sick\n
        500.GOOD2| very rarely sick\n
        250.GOOD1| rarely sick\n
        0.NEUTRAL| (no description)\n
        -250.BAD1| susceptible to disease\n
        -500.BAD2| quite susceptible to disease\n
        -750.BAD3| really susceptible to disease\n
        -1000.BAD4| stunningly susceptible to disease
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
        """1000.GOOD4| awesome intellectual powers

        750.GOOD3| great analytical abilities

        500.GOOD2| a sharp intellect

        250.GOOD1| a good intellect

        0.NEUTRAL| (no description)

        -250.BAD1| poor analytical abilities

        -500.BAD2| very bad analytical abilities

        -750.BAD3| a lousy intellect

        -1000.BAD4| a stunning lack of analytical ability
        """
        self.attributes[SoulAttributes.AnalyticalAbility] = v

    def set_creativity(self, v: AttributeType):
        """
        1000.GOOD4| a boundless creative imagination

        750.GOOD3| great creativity

        500.GOOD2| very good creativity

        250.GOOD1| good creativity

        0.NEUTRAL| (no description)

        -250.BAD1| meager creativity

        -500.BAD2| poor creativity

        -750.BAD3| lousy creativity

        -1000.BAD4| next to no creative talent
        """
        self.attributes[SoulAttributes.Creativity] = v

    def set_empath(self, v: AttributeType):
        """
        1000.GOOD4| an absolutely remarkable sense of others' emotions

        750.GOOD3| a great sense of empathy

        500.GOOD2| a very good sense of empathy

        250.GOOD1| an ability to read emotions fairly well

        0.NEUTRAL| (no description)

        -250.BAD1| poor empathy

        -500.BAD2| a very bad sense of empathy

        -750.BAD3| next to no empathy

        -1000.BAD4| the utter inability to judge others' emotions
        """
        self.attributes[SoulAttributes.Empathy] = v

    def set_focus(self, v: AttributeType):
        """
        1000.GOOD4| unbreakable focus

        750.GOOD3| a great ability to focus

        500.GOOD2| very good focus

        250.GOOD1| the ability to focus

        0.NEUTRAL| (no description)

        -250.BAD1| poor focus

        -500.BAD2| quite poor focus

        -750.BAD3| really poor focus

        -1000.BAD4| the absolute inability to focus
        """
        self.attributes[SoulAttributes.Focus] = v

    def set_intuition(self, v: AttributeType):
        """
        1000.GOOD4| uncanny intuition

        750.GOOD3| great intuition

        500.GOOD2| very good intuition

        250.GOOD1| good intuition

        0.NEUTRAL| (no description)

        -250.BAD1| bad intuition

        -500.BAD2| very bad intuition

        -750.BAD3| lousy intuition

        -1000.BAD4| horrible intuition
        """
        self.attributes[SoulAttributes.Intuition] = v

    def set_kinesthesic_sense(self, v: AttributeType):
        """
        1000.GOOD4| an astounding feel for the position of [his/her] own body

        750.GOOD3| a great kinesthetic sense

        500.GOOD2| a very good sense of the position of [his/her] own body

        250.GOOD1| a good kinesthetic sense

        0.NEUTRAL| (no description)

        -250.BAD1| a meager kinesthetic sense

        -500.BAD2| a poor kinesthetic sense

        -750.BAD3| a very clumsy kinesthetic sense

        -1000.BAD4| an unbelievably atrocious sense of the position of [his/her] own body
        """
        self.attributes[SoulAttributes.Kinesthesic] = v

    def set_linguistic_ability(self, v: AttributeType):
        """
        1000.GOOD4| an astonishing ability with languages and words

        750.GOOD3| a great affinity for language

        500.GOOD2| a natural inclination toward language

        250.GOOD1| a way with words

        0.NEUTRAL| (no description)

        -250.BAD1| a little difficulty with words

        -500.BAD2| little linguistic ability

        -750.BAD3| very little linguistic ability

        -1000.BAD4| difficulty with words and language
        """
        self.attributes[SoulAttributes.Language] = v

    def set_memory(self, v: AttributeType):
        """
        1000.GOOD4| an astonishing memory

        750.GOOD3| an amazing memory

        500.GOOD2| a great memory

        250.GOOD1| a good memory

        0.NEUTRAL| (no description)

        -250.BAD1| an iffy memory

        -500.BAD2| a poor memory

        -750.BAD3| a really bad memory

        -1000.BAD4| little memory to speak of
        """
        self.attributes[SoulAttributes.Memory] = v

    def set_musical_ability(self, v: AttributeType):
        """
        1000.GOOD4| an astonishing knack for music

        750.GOOD3| a great musical sense

        500.GOOD2| a natural ability with music

        250.GOOD1| a feel for music

        0.NEUTRAL| (no description)

        -250.BAD1| an iffy sense for music

        -500.BAD2| little natural inclination toward music

        -750.BAD3| next to no natural musical ability

        -1000.BAD4| absolutely no feel for music at all
        """
        self.attributes[SoulAttributes.Music] = v

    def set_patience(self, v: AttributeType):
        """
        1000.GOOD4| absolutely boundless patience

        750.GOOD3| a deep well of patience

        500.GOOD2| a great deal of patience

        250.GOOD1| a sum of patience

        0.NEUTRAL| (no description)

        -250.BAD1| a shortage of patience

        -500.BAD2| little patience

        -750.BAD3| very little patience

        -1000.BAD4| no patience at all
        """
        self.attributes[SoulAttributes.Patience] = v

    def set_social_awareness(self, v: AttributeType):
        """
        1000.GOOD4| a shockingly profound feel for social relationships

        750.GOOD3| a great feel for social relationships

        500.GOOD2| a very good feel for social relationships

        250.GOOD1| a good feel for social relationships

        0.NEUTRAL| (no description)

        -250.BAD1| a meager ability with social relationships

        -500.BAD2| a poor ability to manage or understand social relationships

        -750.BAD3| a lack of understanding of social relationships

        -1000.BAD4| an absolute inability to understand social relationships
        """
        self.attributes[SoulAttributes.SocialAwareness] = v

    def set_spatial_sense(self, v: AttributeType):
        """
        1000.GOOD4| a stunning feel for spatial relationships

        750.GOOD3| an amazing spatial sense

        500.GOOD2| a great feel for the surrounding space

        250.GOOD1| a good spatial sense

        0.NEUTRAL| (no description)

        -250.BAD1| a questionable spatial sense

        -500.BAD2| poor spatial senses

        -750.BAD3| an atrocious spatial sense

        -1000.BAD4| no sense for spatial relationships
        """
        self.attributes[SoulAttributes.SpatialSense] = v

    def set_willpower(self, v: AttributeType):
        """
        1000.GOOD4| an unbreakable will

        750.GOOD3| an iron will

        500.GOOD2| a lot of willpower

        250.GOOD1| willpower

        0.NEUTRAL| (no description)

        -250.BAD1| little willpower

        -500.BAD2| a large deficit of willpower

        -750.BAD3| next to no willpower

        -1000.BAD4| absolutely no willpower
        """
        self.attributes[SoulAttributes.Willpower] = v

    def set_artwork(self, v: Quality):
        """3.Highest| believes that the creation and appreciation of artwork is one of the highest ideals

        2.VeryHigh| greatly respects artists and their works

        1.High| values artwork

        0.Neutral| doesn't care about art one way or another

        -1.Low| finds artwork boring

        -2.VeryLow| sees the whole pursuit of art as silly

        -3.Lowest| finds art offensive and would have it destroyed whenever possible"""
        self.beliefs[Beliefs.ARTWORK] = v

    def set_commerce(self, v: Quality):
        """3.Highest| sees engaging in commerce as a high ideal in life
        2.VeryHigh| really respects commerce and those that engage in trade

        1.High| respects commerce

        0.Neutral| doesn't particularly respect commerce

        -1.Low| is somewhat put off by trade and commerce

        -2.VeryLow| finds those that engage in trade and commerce to be fairly disgusting

        -3.Lowest| holds the view that commerce is a vile obscenity
        """
        self.beliefs[Beliefs.COMMERCE] = v

    def set_competition(self, v: Quality):
        """3.Highest| holds the idea of competition among the most important values and would encourage it wherever possible

        2.VeryHigh| views competition as a crucial driving force in the world

        1.High| sees competition as reasonably important

        0.Neutral| doesn't have strong views on competition

        -1.Low| sees competition as wasteful and silly

        -2.VeryLow| deeply dislikes competition

        -3.Lowest| finds the very idea of competition obscene
        """
        self.beliefs[Beliefs.COMPETITION] = v

    def set_cooperation(self, v:Quality):
        """3.Highest| places cooperation as one of the highest ideals

        2.VeryHigh| sees cooperation as very important in life

        1.High| values cooperation

        0.Neutral| doesn't see cooperation as valuable

        -1.Low| dislikes cooperation

        -2.VeryLow| views cooperation as a low ideal not worthy of any respect

        -3.Lowest| is thoroughly disgusted by cooperation"""
        self.beliefs[Beliefs.COOPERATION]=v

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

    def set_perseverance_belief(self, v: Quality):
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

    def set_anger_propensity(self, v: Quality):
        """
        3.Highest| is in a constant state of internal rage

        2.VeryHigh| is very quick to anger

        1.High| is quick to anger

        0.Neutral| (no description)

        -1.Low| is slow to anger

        -2.VeryLow| is very slow to anger

        -3.Lowest| never becomes angry

        """
        self.facets[Facets.ANGER_PROPENSITY] = v

    def set_anxiety_propensity(self, v: Quality):
        """
        3.Highest| is a nervous wreck

        2.VeryHigh| is always tense and jittery

        1.High| is often nervous

        0.Neutral| (no description)

        -1.Low| has a calm demeanor

        -2.VeryLow| has a very calm demeanor

        -3.Lowest| has an incredibly calm demeanor

        """
        self.facets[Facets.ANXIETY_PROPENSITY] = v

    def set_art_inclined(self, v: Quality):
        """
        3.Highest| can easily become absorbed in art and the beauty of the natural world

        2.VeryHigh| greatly moved by art and natural beauty

        1.High| is moved by art and natural beauty

        0.Neutral| (no description)

        -1.Low| does not have a great aesthetic sensitivity

        -2.VeryLow| is not readily moved by art or natural beauty

        -3.Lowest| is completely unmoved by art or the beauty of nature

        """
        self.facets[Facets.ART_INCLINED] = v

    def set_assertiveness(self, v: Quality):
        """
        3.Highest| is assertive to the point of aggression, unwilling to let others get a word in edgewise when [he/she] has something to say

        2.VeryHigh| has an overbearing personality

        1.High| is assertive

        0.Neutral| (no description)

        -1.Low| tends to be passive in discussions

        -2.VeryLow| only rarely tries to assert [him/her]self in conversation

        -3.Lowest| would never under any circumstances speak up or otherwise put forth [his/her] point of view in a discussion

        """
        self.facets[Facets.ASSERTIVENESS] = v

    def set_bashful(self, v: Quality):
        """
        3.Highest| is gripped by a crippling shyness

        2.VeryHigh| is bashful

        1.High| tends to consider what others think of [him/her]

        0.Neutral| (no description)

        -1.Low| is not particularly interested in what others think of [him/her]

        -2.VeryLow| is generally unhindered by the thoughts of others concerning [his/her] actions

        -3.Lowest| is shameless, absolutely unfazed by the thoughts of others

        """
        self.facets[Facets.BASHFUL] = v

    def set_bravery(self, v: Quality):
        """
        3.Highest| is utterly fearless when confronted with danger, to the point of lacking common sense

        2.VeryHigh| is incredibly brave in the face of looming danger, perhaps a bit foolhardy

        1.High| is brave in the face of imminent danger

        0.Neutral| (no description)

        -1.Low| is somewhat fearful in the face of imminent danger

        -2.VeryLow| has great trouble mastering fear when confronted by danger

        -3.Lowest| is a coward, completely overwhelmed by fear when confronted with danger

        """
        self.facets[Facets.BRAVERY] = v

    def set_cheer_propensity(self, v: Quality):
        """
        3.Highest| often feels filled with joy

        2.VeryHigh| can be very happy and optimistic

        1.High| is often cheerful

        0.Neutral| (no description)

        -1.Low| is rarely happy or enthusiastic

        -2.VeryLow| is dour as a rule

        -3.Lowest| is never the slightest bit cheerful about anything

        """
        self.facets[Facets.CHEER_PROPENSITY] = v

    def set_closeminded(self, v: Quality):
        """
        3.Highest| is completely closed-minded and never changes [his/her] mind after forming an initial idea

        2.VeryHigh| is intellectually stubborn, rarely changing [his/her] mind during a debate regardless of the merits

        1.High| tends to be a bit stubborn in changing [his/her] mind about things

        0.Neutral| (no description)

        -1.Low| doesn't cling tightly to ideas and is open to changing [his/her] mind

        -2.VeryLow| often finds [him/her]self changing [his/her] mind to agree with somebody else

        -3.Lowest| easily changes [his/her] mind and will generally go with the prevailing view on anything

        """
        self.facets[Facets.CLOSEMINDED] = v

    def set_confidence(self, v: Quality):
        """
        3.Highest| presupposes success in any venture requiring [his/her] skills with what could be called blind overconfidence

        2.VeryHigh| is extremely confident of [him/her]self in situations requiring [his/her] skills

        1.High| is generally quite confident of [his/her] abilities when undertaking specific ventures

        0.Neutral| (no description)

        -1.Low| sometimes acts with little determination and confidence

        -2.VeryLow| lacks confidence in [his/her] abilities

        -3.Lowest| has no confidence at all in [his/her] talent and abilities

        """
        self.facets[Facets.CONFIDENCE] = v

    def set_cruelty(self, v: Quality):
        """
        3.Highest| is deliberately cruel to those unfortunate enough to be subject to [his/her] sadism

        2.VeryHigh| is sometimes cruel

        1.High| generally acts impartially and is rarely moved to mercy

        0.Neutral| (no description)

        -1.Low| often acts with compassion

        -2.VeryLow| is easily moved to mercy

        -3.Lowest| always acts with mercy and compassion at the forefront of [his/her] considerations

        """
        self.facets[Facets.CRUELTY] = v

    def set_curious(self, v: Quality):
        """
        3.Highest| is implacably curious, without any respect for propriety or privacy

        2.VeryHigh| is very curious, sometimes to [his/her] detriment

        1.High| is curious and eager to learn

        0.Neutral| (no description)

        -1.Low| isn't particularly curious about the world

        -2.VeryLow| is very rarely moved by curiosity

        -3.Lowest| is incurious and never seeks out knowledge or information to satisfy [him/her]self

        """
        self.facets[Facets.CURIOUS] = v

    def set_depression_propensity(self, v: Quality):
        """
        3.Highest| is frequently depressed

        2.VeryHigh| is often sad and dejected

        1.High| often feels discouraged

        0.Neutral| (no description)

        -1.Low| rarely feels discouraged

        -2.VeryLow| almost never feels discouraged

        -3.Lowest| never feels discouraged

        """
        self.facets[Facets.DEPRESSION_PROPENSITY] = v

    def set_discord(self, v: Quality):
        """
        3.Highest| revels in chaos and discord, and [he/she] encourages it whenever possible

        2.VeryHigh| finds a chaotic mess preferable to the boredom of harmonious living

        1.High| doesn't mind a little tumult and discord in day-to-day living

        0.Neutral| (no description)

        -1.Low| prefers that everyone live as harmoniously as possible

        -2.VeryLow| feels best when everyone gets along without any strife or contention

        -3.Lowest| would be deeply satisfied if everyone could live as one in complete harmony

        """
        self.facets[Facets.DISCORD] = v

    def set_disdain_advice(self, v: Quality):
        """
        3.Highest| disdains even the best advice of associates and family, relying strictly on [his/her] own counsel

        2.VeryHigh| dislikes receiving advice, preferring to keep [his/her] own counsel

        1.High| has a tendency to go it alone, without considering the advice of others

        0.Neutral| (no description)

        -1.Low| tends to ask others for help with difficult decisions

        -2.VeryLow| relies on the advice of others during decision making

        -3.Lowest| is unable to make decisions without a great deal of input from others

        """
        self.facets[Facets.DISDAIN_ADVICE] = v

    def set_dutifulness(self, v: Quality):
        """
        3.Highest| has a profound sense of duty and obligation

        2.VeryHigh| has a strong sense of duty

        1.High| has a sense of duty

        0.Neutral| (no description)

        -1.Low| finds obligations confining

        -2.VeryLow| dislikes obligations and will try to avoid being bound by them

        -3.Lowest| hates vows, obligations, promises and other binding elements that could restrict [him/her]

        """
        self.facets[Facets.DUTIFULNESS] = v

    def set_emotionally_obsessive(self, v: Quality):
        """
        3.Highest| is emotionally obsessive, forming life-long attachments even if they aren't reciprocated

        2.VeryHigh| forms strong emotional bonds with others, at times to [his/her] detriment

        1.High| has a tendency toward forming deep emotional bonds with others

        0.Neutral| (no description)

        -1.Low| tends to form only tenuous emotional bonds with others

        -2.VeryLow| forms only fleeting and rare emotional bonds with others

        -3.Lowest| does not have feelings of emotional attachment and has never felt even a moment's connection with another being

        """
        self.facets[Facets.EMOTIONALLY_OBSESSIVE] = v

    def set_envy_propensity(self, v: Quality):
        """
        3.Highest| is consumed by overpowering feelings of jealousy

        2.VeryHigh| is prone to strong feelings of jealousy

        1.High| often feels envious of others

        0.Neutral| (no description)

        -1.Low| doesn't often feel envious of others

        -2.VeryLow| is rarely jealous

        -3.Lowest| never envies others their status, situation or possessions

        """
        self.facets[Facets.ENVY_PROPENSITY] = v

    def set_excitement_seeking(self, v: Quality):
        """
        3.Highest| never fails to seek out the most stressful and even dangerous situations

        2.VeryHigh| seeks out exciting and adventurous situations

        1.High| likes a little excitement now and then

        0.Neutral| (no description)

        -1.Low| doesn't seek out excitement

        -2.VeryLow| actively avoids exciting or stressful situations

        -3.Lowest| does everything in [his/her] power to avoid excitement and stress

        """
        self.facets[Facets.EXCITEMENT_SEEKING] = v

    def set_friendliness(self, v: Quality):
        """
        3.Highest| is quite a bold flatterer, extremely friendly but just a little insufferable

        2.VeryHigh| is very friendly and always tries to say nice things to others

        1.High| is a friendly individual

        0.Neutral| (no description)

        -1.Low| is somewhat quarrelsome

        -2.VeryLow| is unfriendly and disagreeable

        -3.Lowest| is a dyed-in-the-wool quarreler, never missing a chance to lash out in verbal hostility

        """
        self.facets[Facets.FRIENDLINESS] = v

    def set_gratitude(self, v: Quality):
        """
        3.Highest| unerringly returns favors and has a profound sense of gratitude for the kind actions of others

        2.VeryHigh| feels a strong need to reciprocate any favor done for [him/her]

        1.High| is grateful when others help [him/her] out and tries to return favors

        0.Neutral| (no description)

        -1.Low| takes offered help and gifts without feeling particularly grateful

        -2.VeryLow| accepts favors without developing a sense of obligation, preferring to act as the current situation demands

        -3.Lowest| does not feel the slightest need to reciprocate favors that others do for [him/her], no matter how major the help or how much [he/she] needed it

        """
        self.facets[Facets.GRATITUDE] = v

    def set_greed(self, v: Quality):
        """
        3.Highest| is as avaricious as they come, obsessed with acquiring wealth

        2.VeryHigh| is very greedy

        1.High| has a greedy streak

        0.Neutral| (no description)

        -1.Low| doesn't focus on material goods

        -2.VeryLow| desires little for [him/her]self in the way of possessions

        -3.Lowest| often neglects [his/her] own wellbeing, having no interest in material goods

        """
        self.facets[Facets.GREED] = v

    def set_gregariousness(self, v: Quality):
        """
        3.Highest| truly treasures the company of others

        2.VeryHigh| enjoys being in crowds

        1.High| enjoys the company of others

        0.Neutral| (no description)

        -1.Low| tends to avoid crowds

        -2.VeryLow| prefers to be alone

        -3.Lowest| considers spending time alone much more important than associating with others

        """
        self.facets[Facets.GREGARIOUSNESS] = v

    def set_hate_propensity(self, v: Quality):
        """
        3.Highest| is often inflamed by hatred and easily develops hatred toward things

        2.VeryHigh| is prone to hatreds and often develops negative feelings

        1.High| is quick to form negative views about things

        0.Neutral| (no description)

        -1.Low| does not easily hate or develop negative feelings

        -2.VeryLow| very rarely develops negative feelings toward things

        -3.Lowest| never feels hatred toward anyone or anything

        """
        self.facets[Facets.HATE_PROPENSITY] = v

    def set_hopeful(self, v: Quality):
        """
        3.Highest| has such a developed sense of optimism that [he/she] always assumes the best outcome will eventually occur, no matter what

        2.VeryHigh| is an optimist

        1.High| generally finds [him/her]self quite hopeful about the future

        0.Neutral| (no description)

        -1.Low| tends to assume the worst of two outcomes will be the one that comes to pass

        -2.VeryLow| is a pessimist

        -3.Lowest| despairs of anything positive happening in the future and lives without feelings of hope

        """
        self.facets[Facets.HOPEFUL] = v

    def set_humor(self, v: Quality):
        """
        3.Highest| finds something humorous in everything, no matter how serious or inappropriate

        2.VeryHigh| finds the humor in most situations

        1.High| has an active sense of humor

        0.Neutral| (no description)

        -1.Low| has little interest in joking around

        -2.VeryLow| does not find most jokes humorous

        -3.Lowest| is utterly humorless

        """
        self.facets[Facets.HUMOR] = v

    def set_imagination(self, v: Quality):
        """
        3.Highest| is bored by reality and would rather disappear utterly and forever into a world of made-up fantasy

        2.VeryHigh| is given to flights of fancy to the point of distraction

        1.High| has an active imagination

        0.Neutral| (no description)

        -1.Low| isn't given to flights of fancy

        -2.VeryLow| is grounded in reality

        -3.Lowest| is interested only in facts and the real world

        """
        self.facets[Facets.IMAGINATION] = v

    def set_immoderation(self, v: Quality):
        """
        3.Highest| is ruled by irresistible cravings and urges

        2.VeryHigh| feels strong urges and seeks short-term rewards

        1.High| occasionally overindulges

        0.Neutral| (no description)

        -1.Low| doesn't often experience strong cravings or urges

        -2.VeryLow| only rarely feels strong cravings or urges

        -3.Lowest| never feels tempted to overindulge in anything

        """
        self.facets[Facets.IMMODERATION] = v

    def set_immodesty(self, v: Quality):
        """
        3.Highest| always presents [him/her]self as extravagantly as possible, displaying a magnificent image to the world

        2.VeryHigh| likes to present [him/her]self boldly, even if it would offend an average sense of modesty

        1.High| doesn't mind wearing something special now and again

        0.Neutral| (no description)

        -1.Low| prefers to present [him/her]self modestly

        -2.VeryLow| presents [him/her]self modestly and frowns on any flashy accoutrements

        -3.Lowest| cleaves to an austere lifestyle, disdaining even minor immodesties in appearance

        """
        self.facets[Facets.IMMODESTY] = v

    def set_love_propensity(self, v: Quality):
        """
        3.Highest| is always in love with somebody and easily develops positive feelings

        2.VeryHigh| very easily falls into love and develops positive feelings

        1.High| can easily fall in love or develop positive sentiments

        0.Neutral| (no description)

        -1.Low| does not easily fall in love and rarely develops positive sentiments

        -2.VeryLow| is not the type to fall in love or even develop positive feelings

        -3.Lowest| never falls in love or develops positive feelings toward anything

        """
        self.facets[Facets.LOVE_PROPENSITY] = v

    def set_lust_propensity(self, v: Quality):
        """
        3.Highest| is constantly ablaze with feelings of lust

        2.VeryHigh| is prone to strong feelings of lust

        1.High| often feels lustful

        0.Neutral| (no description)

        -1.Low| does not often feel lustful

        -2.VeryLow| rarely looks on others with lust

        -3.Lowest| never feels lustful passions

        """
        self.facets[Facets.LUST_PROPENSITY] = v

    def set_orderliness(self, v: Quality):
        """
        3.Highest| is obsessed with order and structure in [his/her] own life, with everything kept in its proper place

        2.VeryHigh| lives an orderly life, organized and neat

        1.High| tries to keep [his/her] things orderly

        0.Neutral| (no description)

        -1.Low| tends to make a small mess with [his/her] own possessions

        -2.VeryLow| is sloppy with [his/her] living space

        -3.Lowest| is completely oblivious to any conception of neatness and will just leave things strewn about without a care

        """
        self.facets[Facets.ORDERLINESS] = v

    def set_perfectionist(self, v: Quality):
        """
        3.Highest| is obsessed with details and will often take a great deal of extra time to make sure things are done the right way

        2.VeryHigh| is a perfectionist

        1.High| tries to do things correctly each time

        0.Neutral| (no description)

        -1.Low| doesn't try to get things done perfectly

        -2.VeryLow| is inattentive to detail in [his/her] own work

        -3.Lowest| is frustratingly sloppy and careless with every task [he/she] sets to carry out

        """
        self.facets[Facets.PERFECTIONIST] = v

    def set_perseverance(self, v: Quality):
        """
        3.Highest| is unbelievably stubborn, and will stick with even the most futile action once [his/her] mind is made up

        2.VeryHigh| is very stubborn

        1.High| is stubborn

        0.Neutral| (no description)

        -1.Low| has a noticeable lack of perseverance

        -2.VeryLow| doesn't stick with things if even minor difficulties arise

        -3.Lowest| drops any activity at the slightest hint of difficulty or even the suggestion of effort being required

        """
        self.facets[Facets.PERSEVERANCE] = v

    def set_politeness(self, v: Quality):
        """
        3.Highest| exhibits a refined politeness and is determined to keep the guiding rules of etiquette and decorum as if life itself depended on it

        2.VeryHigh| is very polite and observes appropriate rules of decorum when possible

        1.High| is quite polite

        0.Neutral| (no description)

        -1.Low| could be considered rude

        -2.VeryLow| is very impolite and inconsiderate of propriety

        -3.Lowest| is a vulgar being who does not care a lick for even the most basic rules of civilized living

        """
        self.facets[Facets.POLITENESS] = v

    def set_pride(self, v: Quality):
        """
        3.Highest| is absorbed in delusions of self-importance

        2.VeryHigh| has an overinflated sense of self-worth

        1.High| thinks [he/she] is fairly important in the grand scheme of things

        0.Neutral| (no description)

        -1.Low| is very humble

        -2.VeryLow| has a low sense of self-esteem

        -3.Lowest| is completely convinced of [his/her] own worthlessness

        """
        self.facets[Facets.PRIDE] = v

    def set_privacy(self, v: Quality):
        """
        3.Highest| is private to the point of paranoia, unwilling to reveal even basic information about [him/her]self

        2.VeryHigh| has a strong tendency toward privacy

        1.High| tends not to reveal personal information

        0.Neutral| (no description)

        -1.Low| tends to share [his/her] own experiences and thoughts with others

        -2.VeryLow| is not a private person and freely shares details of [his/her] life

        -3.Lowest| shares intimate details of life without sparing a thought to repercussions or propriety

        """
        self.facets[Facets.PRIVACY] = v

    def set_singleminded(self, v: Quality):
        """
        3.Highest| pursues matters with a single-minded focus, often overlooking other matters

        2.VeryHigh| can be very single-minded

        1.High| generally acts with a narrow focus on the current activity

        0.Neutral| (no description)

        -1.Low| can occasionally lose focus on the matter at hand

        -2.VeryLow| is somewhat scatterbrained

        -3.Lowest| is a complete scatterbrain, unable to focus on a single matter for more than a passing moment

        """
        self.facets[Facets.SINGLEMINDED] = v

    def set_stress_vulnerability(self, v: Quality):
        """
        3.Highest| becomes completely helpless in stressful situations

        2.VeryHigh| cracks easily under pressure

        1.High| doesn't handle stress well

        0.Neutral| (no description)

        -1.Low| can handle stress

        -2.VeryLow| is confident under pressure

        -3.Lowest| is impervious to the effects of stress

        """
        self.facets[Facets.STRESS_VULNERABILITY] = v

    def set_swayed_by_emotions(self, v: Quality):
        """
        3.Highest| is buffeted by others' emotions and can't help but to respond to them

        2.VeryHigh| is swayed by emotional appeals

        1.High| tends to be swayed by the emotions of others

        0.Neutral| (no description)

        -1.Low| tends not to be swayed by emotional appeals

        -2.VeryLow| does not generally respond to emotional appeals

        -3.Lowest| is never moved by the emotions of others

        """
        self.facets[Facets.SWAYED_BY_EMOTIONS] = v

    def set_thoughtlessness(self, v: Quality):
        """
        3.Highest| never deliberates before acting, to the point of being considered thoughtless

        2.VeryHigh| doesn't generally think before acting

        1.High| can sometimes act without deliberation

        0.Neutral| (no description)

        -1.Low| tends to think before acting

        -2.VeryLow| can get caught up in internal deliberations when action is necessary

        -3.Lowest| never acts without prolonged deliberation, even to [his/her] own detriment and the harm of those around [him/her]

        """
        self.facets[Facets.THOUGHTLESSNESS] = v

    def set_tolerant(self, v: Quality):
        """
        3.Highest| is not bothered in the slightest by deviations from the norm or even extreme differences in lifestyle or appearance

        2.VeryHigh| is very comfortable around others that are different from [him/her]

        1.High| is quite comfortable with others that have a different appearance or culture

        0.Neutral| (no description)

        -1.Low| is somewhat uncomfortable around those that appear unusual or live differently from [him/her]

        -2.VeryLow| is made deeply uncomfortable by differences in culture or appearance

        -3.Lowest| cannot tolerate differences in culture, lifestyle or appearance

        """
        self.facets[Facets.TOLERANT] = v

    def set_trust(self, v: Quality):
        """
        3.Highest| is naturally trustful of everybody

        2.VeryHigh| is very trusting

        1.High| is trusting

        0.Neutral| (no description)

        -1.Low| is slow to trust others

        -2.VeryLow| does not trust others

        -3.Lowest| sees others as selfish and conniving

        """
        self.facets[Facets.TRUST] = v

    def set_vanity(self, v: Quality):
        """
        3.Highest| is completely wrapped up in [his/her] own appearance, abilities and other personal matters

        2.VeryHigh| is greatly pleased by [his/her] own looks and accomplishments

        1.High| is pleased by [his/her] own appearance and talents

        0.Neutral| (no description)

        -1.Low| is not inherently proud of [his/her] talents and accomplishments

        -2.VeryLow| takes no pleasure in [his/her] talents and appearance

        -3.Lowest| could not care less about [his/her] appearance, talents or other personal vanities

        """
        self.facets[Facets.VANITY] = v

    def set_vengeful(self, v: Quality):
        """
        3.Highest| is vengeful and never forgets or forgives past grievances

        2.VeryHigh| has little time for forgiveness and will generally seek retribution

        1.High| tends to hang on to grievances

        0.Neutral| (no description)

        -1.Low| doesn't tend to hold on to grievances

        -2.VeryLow| does not generally seek retribution for past wrongs

        -3.Lowest| has no sense of vengeance or retribution

        """
        self.facets[Facets.VENGEFUL] = v

    def set_violent(self, v: Quality):
        """
        3.Highest| is given to rough-and-tumble brawling, even to the point of starting fights for no reason

        2.VeryHigh| would never pass up a chance for a good fistfight

        1.High| likes to brawl

        0.Neutral| (no description)

        -1.Low| tends to avoid any physical confrontations

        -2.VeryLow| does not enjoy participating in physical confrontations

        -3.Lowest| would flee even the most necessary battle to avoid any form of physical confrontation

        """
        self.facets[Facets.VIOLENT] = v

    def set_wastefulness(self, v: Quality):
        """
        3.Highest| is completely careless with resources when completing projects, and invariably wastes a lot of time and effort

        2.VeryHigh| is not careful with resources when working on projects and often spends unnecessary effort

        1.High| tends to be a little wasteful when working on projects

        0.Neutral| (no description)

        -1.Low| tends to be a little tight with resources when working on projects

        -2.VeryLow| is stingy with resources on projects and refuses to expend any extra effort

        -3.Lowest| cuts any corners possible when working on a project, regardless of the consequences, rather than wasting effort or resources

        """
        self.facets[Facets.WASTEFULNESS] = v

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
