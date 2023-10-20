from math import sqrt as square_root


def is_prime(num):
    if num <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, square_root(num)):
        if num % i == 0:
            return False;

    return True


def is_even(num):
    """
    Predicate Function
    :param num:
    :return:
    """
    if num % 2 == 0:
        return True
    else:
        return False