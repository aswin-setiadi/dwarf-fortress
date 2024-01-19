from char import Character
from stats import AttributeType as AT, Goals, Quality as qty


def char() -> Character:
    c = Character(name="", gender="", goals={})
    return c


def char1() -> Character:
    char = Character(name="Atis Atheludist", gender="male", goals={})
    char.set_spatial_sense(AT.g1)
    char.set_creativity(AT.g1)
    char.set_empath(AT.b1)
    char.set_analytical_ability(AT.b2)
    char.set_patience(AT.b2)

    char.set_imagination(qty.VeryLow)
    char.set_vengeful(qty.VeryHigh)
    char.set_tolerant(qty.Low)
    char.set_immoderation(qty.High)
    char.set_immodesty(qty.High)
    char.set_swayed_by_emotions(qty.High)
    char.set_hate_propensity(qty.High)
    char.set_excitement_seeking(qty.Low)
    char.set_greed(qty.Low)
    char.set_cheer_propensity(qty.Low)
    char.set_privacy(qty.High)

    char.set_tradition(qty.Low)
    char.set_family(qty.Low)
    char.set_merriment(qty.Neutral)
    return char


def char2() -> Character:
    c = Character(
        name="Dakost Vosutkogan", gender="female", goals={Goals.CRAFT_A_MASTERWORK}
    )
    c.set_patience(AT.g3)
    c.set_creativity(AT.g2)
    c.set_musical_ability(AT.g1)
    c.set_memory(AT.b3)

    c.set_privacy(qty.VeryHigh)
    c.set_vanity(qty.VeryLow)
    c.set_activity_level(qty.VeryLow)
    c.set_envy_propensity(qty.High)
    c.set_gratitude(qty.Low)
    c.set_tolerant(qty.High)
    c.set_thoughtlessness(qty.Low)
    c.set_perfectionist(qty.High)
    c.set_greed(qty.High)

    c.set_tranquility(qty.High)
    return c


def char3() -> Character:
    c = Character(
        name="Kogsak Nokimthad", gender="female", goals={Goals.START_A_FAMILY}
    )
    c.set_analytical_ability(AT.g2)
    c.set_kinesthesic_sense(AT.g1)
    c.set_focus(AT.g1)
    c.set_spatial_sense(AT.b2)
    c.set_linguistic_ability(AT.b2)

    c.set_discord(qty.VeryLow)
    c.set_cruelty(qty.VeryLow)
    c.set_wastefulness(qty.High)
    c.set_perfectionist(qty.Low)
    c.set_immoderation(qty.High)
    c.set_vanity(qty.Low)
    c.set_tolerant(qty.Low)
    c.set_thoughtlessness(qty.Low)
    c.set_stress_vulnerability(qty.Low)
    c.set_confidence(qty.Low)

    c.set_knowledge(qty.Low)
    c.set_introspection(qty.High)
    c.set_artwork(qty.High)
    return c


def char4() -> Character:
    c = Character(
        name="Shorast Stakudmesir", gender="female", goals={Goals.CRAFT_A_MASTERWORK}
    )
    c.set_endurance(AT.g1)

    c.set_intuition(AT.g3)
    c.set_creativity(AT.g3)
    c.set_linguistic_ability(AT.g1)
    c.set_analytical_ability(AT.g1)
    c.set_willpower(AT.b1)
    c.set_memory(AT.b2)

    c.set_thoughtlessness(qty.Low)
    c.set_assertiveness(qty.High)
    c.set_lust_propensity(qty.High)
    c.set_excitement_seeking(qty.Low)
    c.set_politeness(qty.High)
    c.set_immodesty(qty.Low)
    c.set_abstract_inclined(qty.High)
    c.set_activity_level(qty.Low)
    c.set_love_propensity(qty.High)
    c.set_discord(qty.High)
    c.set_privacy(qty.Low)

    c.set_sacrifice(qty.Low)
    c.set_friendship(qty.High)
    return c


def char5() -> Character:
    c = Character(name="Urist Ducimtost", gender="female", goals={})
    c.set_focus(AT.g3)
    c.set_spatial_sense(AT.g3)
    c.set_memory(AT.g1)
    c.set_intuition(AT.g1)
    c.set_creativity(AT.g1)
    c.set_musical_ability(AT.b1)

    c.set_imagination(qty.VeryLow)
    c.set_swayed_by_emotions(qty.VeryLow)
    c.set_greed(qty.VeryLow)
    c.set_ambition(qty.High)
    c.set_friendliness(qty.High)
    c.set_privacy(qty.Low)
    c.set_bravery(qty.High)
    c.set_envy_propensity(qty.High)
    c.set_vanity(qty.High)
    c.set_bashful(qty.High)
    c.set_closeminded(qty.Low)
    c.set_stress_vulnerability(qty.High)

    c.set_martial_prowess(qty.Low)
    c.set_law(qty.Neutral)
    return c


def char6() -> Character:
    c = Character(name="Urist Egulezum", gender="male", goals={Goals.MASTER_A_SKILL})
    c.set_recuperation(AT.g1)
    c.set_strength(AT.g1)

    c.set_creativity(AT.b1)
    c.set_kinesthesic_sense(AT.b3)

    c.set_bashful(qty.VeryLow)
    c.set_envy_propensity(qty.High)
    c.set_perseverance(qty.Low)
    c.set_emotionally_obsessive(qty.High)
    c.set_imagination(qty.High)

    c.set_stoicism(qty.High)
    c.set_leisure_time(qty.Neutral)
    return c


def char7() -> Character:
    c = Character(name="Zulban Kubukkurel", gender="male", goals={Goals.MASTER_A_SKILL})
    c.set_endurance(AT.g3)
    c.set_toughness(AT.g2)
    c.set_disease_resistance(AT.g1)
    c.set_recuperation(AT.g1)
    c.set_agility(AT.g1)

    c.set_creativity(AT.g1)
    c.set_empath(AT.b1)
    c.set_social_awareness(AT.b1)
    c.set_memory(AT.b1)
    c.set_linguistic_ability(AT.b2)
    c.set_analytical_ability(AT.b2)

    c.set_discord(qty.VeryLow)
    c.set_lust_propensity(qty.VeryHigh)
    c.set_abstract_inclined(qty.Low)
    c.set_immodesty(qty.Low)
    c.set_humor(qty.Low)
    c.set_swayed_by_emotions(qty.High)
    c.set_immoderation(qty.High)
    c.set_singleminded(qty.High)
    c.set_bashful(qty.High)

    c.set_leisure_time(qty.Low)
    c.set_craftsmanship(qty.Neutral)
    c.set_hard_work(qty.Neutral)
    c.set_family(qty.Neutral)
    c.set_fairness(qty.Neutral)
    return c


def char8() -> Character:
    c = Character(name="Lokum Letmosigath", gender="male", goals={Goals.MASTER_A_SKILL})
    c.set_endurance(AT.b1)
    c.set_kinesthesic_sense(AT.g3)
    c.set_creativity(AT.g1)
    c.set_spatial_sense(AT.b1)
    c.set_analytical_ability(AT.b2)
    c.set_social_awareness(AT.b2)

    c.set_curious(qty.Lowest)
    c.set_hate_propensity(qty.VeryLow)
    c.set_emotionally_obsessive(qty.VeryHigh)
    c.set_immodesty(qty.Low)
    c.set_hopeful(qty.High)
    c.set_perseverance(qty.High)
    c.set_wastefulness(qty.Low)
    c.set_bravery(qty.High)
    c.set_anxiety_propensity(qty.Low)
    c.set_humor(qty.Low)
    c.set_imagination(qty.High)
    c.set_immoderation(qty.High)
    c.set_violent(qty.Low)

    c.set_fairness(qty.Lowest)
    c.set_nature(qty.Neutral)
    return c


def char9() -> Character:
    c = Character(name="Unib Keskalmusar", gender="male", goals={Goals.START_A_FAMILY})
    c.set_endurance(AT.g2)
    c.set_toughness(AT.b1)
    c.set_strength(AT.b1)
    c.set_agility(AT.b2)

    c.set_analytical_ability(AT.g3)
    c.set_patience(AT.g2)
    c.set_memory(AT.g1)
    c.set_empath(AT.g1)
    c.set_kinesthesic_sense(AT.b1)

    c.set_orderliness(qty.Lowest)
    c.set_humor(qty.VeryLow)
    c.set_closeminded(qty.High)
    c.set_altruism(qty.High)
    c.set_tolerant(qty.High)
    c.set_activity_level(qty.High)
    c.set_cruelty(qty.High)
    c.set_singleminded(qty.High)
    c.set_violent(qty.High)
    c.set_assertiveness(qty.High)
    c.set_hate_propensity(qty.High)
    c.set_trust(qty.High)
    c.set_cheer_propensity(qty.Low)
    c.set_gratitude(qty.High)

    c.set_stoicism(qty.High)
    c.set_decorum(qty.High)
    c.set_cooperation(qty.Low)
    return c


def char10() -> Character:
    c = Character(
        name="Urdim Rithlutstakud", gender="male", goals={Goals.MASTER_A_SKILL}
    )
    c.set_strength(AT.g3)
    c.set_toughness(AT.g3)
    c.set_disease_resistance(AT.g1)
    c.set_recuperation(AT.g1)

    c.set_spatial_sense(AT.g3)
    c.set_intuition(AT.g3)
    c.set_focus(AT.g3)
    c.set_patience(AT.g2)
    c.set_memory(AT.g1)
    c.set_kinesthesic_sense(AT.g1)
    c.set_musical_ability(AT.g1)
    c.set_creativity(AT.g1)
    c.set_linguistic_ability(AT.b1)

    c.set_anxiety_propensity(qty.Lowest)
    c.set_violent(qty.VeryLow)
    c.set_immodesty(qty.VeryHigh)
    c.set_greed(qty.High)
    c.set_stress_vulnerability(qty.High)
    c.set_vengeful(qty.High)
    c.set_gregariousness(qty.Low)
    c.set_friendliness(qty.Low)

    c.set_craftsmanship(qty.VeryHigh)
    c.set_family(qty.High)
    c.set_competition(qty.Low)
    c.set_truth(qty.Neutral)
    return c


def char11() -> Character:
    c = Character(name="Kosoth Avalavuz", gender="male", goals={Goals.MASTER_A_SKILL})
    c.set_endurance(AT.g1)
    c.set_disease_resistance(AT.b2)
    c.set_recuperation(AT.b2)

    c.set_analytical_ability(AT.g3)
    c.set_linguistic_ability(AT.g1)
    c.set_focus(AT.b1)

    c.set_discord(qty.Highest)
    c.set_orderliness(qty.VeryHigh)
    c.set_love_propensity(qty.Low)
    c.set_trust(qty.Low)
    c.set_gregariousness(qty.High)
    c.set_altruism(qty.Low)
    c.set_stress_vulnerability(qty.High)
    c.set_envy_propensity(qty.Low)
    c.set_anxiety_propensity(qty.High)
    c.set_singleminded(qty.High)

    c.set_stoicism(qty.VeryHigh)
    c.set_tradition(qty.High)
    c.set_friendship(qty.Neutral)
    c.set_knowledge(qty.Neutral)
    return c


def char12() -> Character:
    c = Character(
        name="Likot Ilrallimar", gender="female", goals={Goals.START_A_FAMILY}
    )
    c.set_endurance(AT.b1)
    c.set_disease_resistance(AT.b2)

    c.set_spatial_sense(AT.g2)
    c.set_patience(AT.g2)
    c.set_intuition(AT.g1)
    c.set_willpower(AT.g1)
    c.set_creativity(AT.g1)
    c.set_musical_ability(AT.b1)
    c.set_kinesthesic_sense(AT.b2)
    c.set_social_awareness(AT.b2)
    c.set_analytical_ability(AT.b3)

    c.set_anger_propensity(qty.VeryLow)
    c.set_perfectionist(qty.VeryLow)
    c.set_excitement_seeking(qty.VeryHigh)
    c.set_politeness(qty.Low)
    c.set_orderliness(qty.High)
    c.set_art_inclined(qty.High)
    c.set_cheer_propensity(qty.High)
    c.set_altruism(qty.Low)
    c.set_bashful(qty.Low)

    c.set_perseverance_belief(qty.VeryLow)
    c.set_loyalty(qty.Neutral)
    return c


def char13() -> Character:
    c = Character(
        name="Mistem Erithducim", gender="female", goals={Goals.MASTER_A_SKILL}
    )
    c.set_endurance(AT.g3)
    c.set_disease_resistance(AT.g1)
    c.set_toughness(AT.g1)
    c.set_agility(AT.b1)
    c.set_recuperation(AT.b2)

    c.set_willpower(AT.g2)
    c.set_spatial_sense(AT.b1)
    c.set_analytical_ability(AT.b2)
    c.set_intuition(AT.b2)
    c.set_patience(AT.b2)

    c.set_anger_propensity(qty.VeryLow)
    c.set_closeminded(qty.Low)
    c.set_cheer_propensity(qty.High)
    c.set_singleminded(qty.Low)

    c.set_independence(qty.VeryHigh)
    c.set_martial_prowess(qty.Neutral)
    return c


def char14() -> Character:
    c = Character(
        name="Monom Tekkudrimtar", gender="male", goals={Goals.START_A_FAMILY}
    )
    # no bodyattribute explicit values
    c.set_willpower(AT.g3)
    c.set_musical_ability(AT.g3)
    c.set_intuition(AT.g2)
    c.set_patience(AT.b1)

    c.set_disdain_advice(qty.VeryLow)
    c.set_privacy(qty.Low)
    c.set_perfectionist(qty.High)
    c.set_love_propensity(qty.Low)
    c.set_dutifulness(qty.Low)
    c.set_perseverance(qty.High)
    c.set_assertiveness(qty.Low)
    c.set_ambition(qty.Low)
    c.set_pride(qty.High)
    c.set_emotionally_obsessive(qty.Low)
    c.set_trust(qty.Low)

    c.set_friendship(qty.Neutral)
    c.set_artwork(qty.Neutral)
    return c


def char15() -> Character:
    c = Character(
        name="Mosus Sigunbomrek",
        gender="female",
        goals={Goals.CREATE_A_GREAT_WORK_OF_ART},
    )
    c.set_recuperation(AT.g3)
    c.set_strength(AT.g3)
    c.set_agility(AT.g2)
    c.set_disease_resistance(AT.g1)

    c.set_linguistic_ability(AT.g2)
    c.set_creativity(AT.g2)
    c.set_patience(AT.g1)
    c.set_willpower(AT.b1)
    c.set_spatial_sense(AT.b2)
    c.set_confidence(qty.Highest)
    c.set_bravery(qty.VeryLow)
    c.set_ambition(qty.VeryHigh)
    c.set_friendliness(qty.Low)
    c.set_hate_propensity(qty.Low)
    c.set_privacy(qty.Low)
    c.set_imagination(qty.Low)
    c.set_tolerant(qty.Low)
    c.set_closeminded(qty.High)
    c.set_art_inclined(qty.High)
    c.set_immoderation(qty.High)
    c.set_activity_level(qty.Low)
    c.set_stress_vulnerability(qty.Low)
    c.set_emotionally_obsessive(qty.High)

    c.set_independence(qty.Low)
    c.set_knowledge(qty.Low)
    c.set_sacrifice(qty.High)
    c.set_cunning(qty.Low)
    c.set_truth(qty.Neutral)
    return c


def char16() -> Character:
    c = Character(
        name="Thikut Ishashonul", gender="female", goals={Goals.CRAFT_A_MASTERWORK}
    )
    c.set_agility(AT.b1)
    c.set_strength(AT.b2)

    c.set_empath(AT.g3)
    c.set_musical_ability(AT.g2)
    c.set_willpower(AT.g1)
    c.set_analytical_ability(AT.g1)
    c.set_linguistic_ability(AT.b2)
    c.set_spatial_sense(AT.b2)

    c.set_humor(qty.Lowest)
    c.set_gratitude(qty.VeryHigh)
    c.set_anger_propensity(qty.VeryLow)
    c.set_depression_propensity(qty.High)
    c.set_tolerant(qty.Low)
    c.set_stress_vulnerability(qty.Low)
    c.set_vengeful(qty.Low)
    c.set_ambition(qty.High)
    c.set_greed(qty.High)
    c.set_immoderation(qty.High)
    c.set_pride(qty.High)

    c.set_sacrifice(qty.Low)
    c.set_law(qty.High)
    c.set_loyalty(qty.Low)
    return c


def char17() -> Character:
    c = Character(name="Tulon Sholidoslan", gender="male", goals={Goals.MASTER_A_SKILL})
    c.set_toughness(AT.g3)
    c.set_strength(AT.g1)
    c.set_recuperation(AT.b2)

    c.set_social_awareness(AT.g3)
    c.set_focus(AT.g3)
    c.set_linguistic_ability(AT.g1)
    c.set_memory(AT.b1)

    c.set_pride(qty.VeryLow)
    c.set_vengeful(qty.VeryLow)
    c.set_thoughtlessness(qty.VeryLow)
    c.set_imagination(qty.VeryHigh)
    c.set_lust_propensity(qty.High)
    c.set_anger_propensity(qty.Low)
    c.set_disdain_advice(qty.Low)
    c.set_art_inclined(qty.High)
    c.set_hopeful(qty.Low)
    c.set_orderliness(qty.High)
    c.set_wastefulness(qty.Low)
    c.set_emotionally_obsessive(qty.Low)
    c.set_cheer_propensity(qty.Low)
    c.set_curious(qty.Low)
    c.set_greed(qty.High)
    c.set_stress_vulnerability(qty.Low)

    c.set_law(qty.Low)
    c.set_nature(qty.Neutral)
    return c
