price_too_low_error = "The price should be greater than 0"
discount_out_of_range_error = "The discount should be between 0 and 100"
price_nan_error = "The price should be a number"
discount_nan_error = "The discount should be a number"


def apply_discount(price, discount):
    if not isinstance(price, (float, int)):
        return price_nan_error
    if not isinstance(discount, (float, int)):
        return discount_nan_error
    if price <= 0:
        return price_too_low_error
    if discount < 0 or discount > 100:
        return discount_out_of_range_error

    return price * (100 - discount) * 0.01
