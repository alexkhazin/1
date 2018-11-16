25. """Given a non-negative integer, return a list of the individual digits in
order."""

def make_list(number):
    result = []
    while number:
        result.append(number%10)
        number //= 10
    return result[::-1]