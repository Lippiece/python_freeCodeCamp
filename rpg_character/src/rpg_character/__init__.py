name_not_string_error = "The character name should be a string"
no_name_error = "The character should have a name"
too_long_name_error = "The character name is too long"
name_has_spaces_error = "The character name should not contain spaces"
stats_are_not_ints_error = "All stats should be integers"
stats_less_than_one_error = "All stats should be no less than 1"
stats_too_large_error = "All stats should be no more than 4"
stats_dont_sum_error = "The character should start with 7 points"


def create_character(character_name, strength, intelligence, charisma) -> str:
    if not isinstance(character_name, str):
        return name_not_string_error
    if character_name == "":
        return no_name_error
    if len(character_name) > 10:
        return too_long_name_error
    if " " in character_name:
        return name_has_spaces_error

    if (
        (not isinstance(strength, int) or isinstance(strength, bool))
        or (not isinstance(intelligence, int) or isinstance(intelligence, bool))
        or (not isinstance(charisma, int) or isinstance(charisma, bool))
    ):
        return stats_are_not_ints_error

    if strength < 1 or intelligence < 1 or charisma < 1:
        return stats_less_than_one_error

    if strength > 4 or intelligence > 4 or charisma > 4:
        return stats_too_large_error

    if strength + intelligence + charisma != 7:
        return stats_dont_sum_error

    return f"""{character_name}
STR {strength * "●"}{(10 - strength) * "○"}
INT {intelligence * "●"}{(10 - intelligence) * "○"}
CHA {charisma * "●"}{(10 - charisma) * "○"}"""
