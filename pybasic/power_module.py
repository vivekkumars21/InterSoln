
class NegativeExponentError(Exception):
    pass

def calculate_power(base, exponent):
    if exponent < 0:
        raise NegativeExponentError("Negative Exponent Not Allowed")
    return base ** exponent
