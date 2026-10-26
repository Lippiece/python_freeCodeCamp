from apply_discount import (
    apply_discount,
    discount_nan_error,
    discount_out_of_range_error,
    price_nan_error,
    price_too_low_error,
)


# If price is not a number (int or float),
# the function should return the string The price should be a number.
def test_price_nan() -> None:
    assert apply_discount("", 1) == price_nan_error


# If discount is not a number (int or float),
# the function should return the string The discount should be a number.
def test_discount_nan() -> None:
    assert apply_discount(1, "") == discount_nan_error


# If price is less than or equal to 0,
# the function should return the string The price should be greater than 0.
def test_too_low_price() -> None:
    cases = [
        (lambda: apply_discount(0, 1), price_too_low_error),
        (lambda: apply_discount(-1, 1), price_too_low_error),
        (lambda: apply_discount(-0.00001, 1), price_too_low_error),
    ]
    for check, error in cases:
        assert check() == error


# If discount is less than 0 or greater than 100,
# the function should return the string The discount should be between 0 and 100.
def test_price_out_of_range() -> None:
    cases = [
        (lambda: apply_discount(1, -1000001.1343134), discount_out_of_range_error),
        (lambda: apply_discount(1, -1), discount_out_of_range_error),
        (lambda: apply_discount(1, 101), discount_out_of_range_error),
    ]
    for check, error in cases:
        assert check() == error


# If both inputs are valid,
# the function should calculate the discount as a percentage of the price.
# The function should return the final price after applying the discount.
def test_valid_cases() -> None:
    cases = [
        (lambda: apply_discount(100, 25), 75),
        (lambda: apply_discount(1000, 10), 900),
        (lambda: apply_discount(10, 50), 5),
        (lambda: apply_discount(100, 99), 1),
    ]
    for check, error in cases:
        assert check() == error
