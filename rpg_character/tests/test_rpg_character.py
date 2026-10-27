from rpg_character import (
    create_character,
    name_has_spaces_error,
    name_not_string_error,
    no_name_error,
    stats_are_not_ints_error,
    stats_dont_sum_error,
    stats_less_than_one_error,
    stats_too_large_error,
    too_long_name_error,
)


def test_validate_string_name() -> None:
    assert create_character(2, 2, 2, 2) == name_not_string_error


def test_validate_non_empty_name() -> None:
    assert create_character("", 2, 2, 2) == no_name_error


def test_validate_too_long_name() -> None:
    assert create_character("123123123123", 2, 2, 2) == too_long_name_error


def test_validate_no_spaces_in_name() -> None:
    assert create_character("a a", 2, 2, 2) == name_has_spaces_error


def test_validate_stats_are_integers() -> None:
    for result in [
        create_character("a", True, 2, 2),
        create_character("a", 2, True, 2),
        create_character("a", 2, 2, True),
        create_character("a", True, True, True),
    ]:
        assert result == stats_are_not_ints_error


#     If one or more stats are less than 1, the function should return All stats should be no less than 1.
def test_validate_stats_are_more_than_one() -> None:
    for result in [
        create_character("a", 0, 2, 2),
        create_character("a", 2, 0, 2),
        create_character("a", 2, 2, 0),
        create_character("a", 1, 1, 0),
    ]:
        assert result == stats_less_than_one_error


#     If one or more stats are more than 4, the function should return All stats should be no more than 4.
def test_validate_stats_are_no_more_than_four() -> None:
    for result in [
        create_character("a", 5, 2, 2),
        create_character("a", 2, 5, 2),
        create_character("a", 2, 2, 5),
        create_character("a", 5, 5, 5),
    ]:
        assert result == stats_too_large_error


#     If the sum of all stats does not equal 7, the function should return The character should start with 7 points.
def test_validate_stats_sum_to_seven() -> None:
    assert create_character("a", 4, 2, 2) == stats_dont_sum_error


valid_case = create_character("a", 2, 3, 2)
#     The first line should contain the character name.
def test_has_name_first() -> None:
    assert valid_case.split("\n")[0] == "a"


#     Lines 2-4 should start with the stat abbreviation, STR, INT, or CHA (in this order)
def test_has_ordered_stats() -> None:
    _, strength, intelligence, charisma = valid_case.split("\n")
    assert strength
    assert intelligence
    assert charisma
    assert strength.split(" ")[0] == "STR"
    assert intelligence.split(" ")[0] == "INT"
    assert charisma.split(" ")[0] == "CHA"


# , then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3, there must be 3 full dots followed by 7 empty dots.
def test_has_correct_dots() -> None:
    _, strength, intelligence, charisma = valid_case.split("\n")
    assert strength == "STR ●●○○○○○○○○"
    assert intelligence == "INT ●●●○○○○○○○"
    assert charisma == "CHA ●●○○○○○○○○"
