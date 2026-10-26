distance_mi = 3
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = False


is_very_short = distance_mi <= 1
is_short = distance_mi > 1 and distance_mi <= 6
is_long = distance_mi > 6

is_raining_without_bike = is_raining and not has_bike
is_raining_with_bike = is_raining and has_bike
is_clear_without_bike = not is_raining and not has_bike
is_clear_with_bike = not is_raining and has_bike
has_wheels = has_car or has_ride_share_app


if not distance_mi or (
    (is_very_short and is_raining)
    or (
        is_short
        and (is_clear_without_bike or is_raining_without_bike or is_raining_with_bike)
    )
    or (is_long and not has_wheels)
):
    print("False")
    can_ride = "False"
elif (
    (is_very_short and not is_raining)
    or (is_short and is_clear_with_bike)
    or (is_long and has_wheels)
):
    print("True")
    can_ride = "True"
