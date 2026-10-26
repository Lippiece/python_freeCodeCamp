from travel_weather_planner import (
    can_ride,
    distance_mi,
    has_bike,
    has_car,
    has_ride_share_app,
    has_wheels,
    is_clear_with_bike,
    is_clear_without_bike,
    is_long,
    is_raining,
    is_raining_without_bike,
    is_short,
    is_very_short,
)


def test_distance_mi_variable() -> None:
    assert isinstance(distance_mi, (int, float))


def test_is_raining_variable() -> None:
    assert isinstance(is_raining, bool)


def test_has_bike_variable() -> None:
    assert isinstance(has_bike, bool)


def test_has_car_variable() -> None:
    assert isinstance(has_car, bool)


def test_has_ride_share_app_variable() -> None:
    assert isinstance(has_ride_share_app, bool)


def test_distance_falsy() -> None:
    assert distance_mi or can_ride == "False"


def test_short_and_raining_without_bike() -> None:
    assert not distance_mi or (
        not (is_short) or (not is_raining_without_bike or can_ride == "True")
    )


def test_short_and_raining_with_bike() -> None:
    assert not distance_mi or (
        not (is_short) or (not is_raining_without_bike or can_ride == "True")
    )


def test_very_short() -> None:
    assert not distance_mi or not is_very_short or (is_raining and can_ride == "False")


def test_short_and_clear_without_bike() -> None:
    assert not distance_mi or (
        not (is_short)
        or (not is_clear_without_bike or can_ride == "True")
        or can_ride == "False"
    )


def test_short_and_clear_with_bike() -> None:
    assert (
        not is_short
        or not is_clear_with_bike
        or (is_short and is_clear_with_bike and can_ride == "True")
    )


def test_long_and_has_car() -> None:
    assert (
        not is_long
        or not (has_car or has_ride_share_app or has_wheels)
        or (is_long and has_wheels and can_ride == "True")
    )
