'''
itertools.islice()
perfrom lazy slicing of any iterator
'''

from itertools import islice, count

one_million_numbers = (x for x in range(1, 1000000))

first_ten = islice(one_million_numbers, 10)

for x in first_ten:
    print(x)


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


# first thousand evens isslice and count
first_thousand_even = islice((x for x in count() if is_even(x)), 1000)
print(first_thousand_even)

list_it = list(first_thousand_even)[-10:]
print(list_it)

for x in first_thousand_even:
    print(x)