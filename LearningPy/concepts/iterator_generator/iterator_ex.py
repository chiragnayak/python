from pprint import pprint as pp

iterable_list = [1, 2, 3, 4, 5]

iterator_obj = iter(iterable_list)

pp(next(iterator_obj))
pp(next(iterator_obj))
pp(next(iterator_obj))
pp(next(iterator_obj))
pp(next(iterator_obj))

# should throw StopIteration
# pp(next(iterator_obj))

# Iteration Protocol
def get_data(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterator is Empty!")

# gives first element of this list
pp(get_data([1,2]))

# gives first element of the set (random first)
pp(get_data({"Chirag", "Nayak"}))

# throws value error
get_data([])