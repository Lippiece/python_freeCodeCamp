base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"
is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3

extra_charges = 0
if show_time == "Evening" or is_weekend:
    extra_charges = 2
