from pprint import pprint as pp

text = "Kindle the light of knowledge and love"
data = text.split(" ")

# list comprehension : [expr(x) for x in iterable]
# iterable can be any object that is iterable like : list, tuple.
# resulting object is list
word_len = [len(x) for x in data]
print(word_len)

# set comprehension : {expr(x) for x in iterable}
# iterable can be any object that is iterable like : list, tuple.
# result is set (i.e. duplicates removed)
word_len = {len(x) for x in data}
print(word_len)

# dictionary comprehension :
# {
#     key_expr(item) : value_expr(item)
#     for item in iterable
# }
# result is a dictionary
# Ex usage : to invert a dictionary to perform reverse lookups.
# basically to make values from previous dict as keys in new dict.
country_to_capital = {"India": "New Delhi",
                      "China": "Beijing",
                      "USA": "Washington D.C.",
                      "Nepal": "Kathmandu"}
pp(country_to_capital)

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)


# Filtering comprehensions
# First, you need a predicate functions

def is_even(num):
    if num != 0 and num % 2 == 0:
        return True
    return False


nums = range(0, 50)
# ex 1
evens = [x for x in nums if is_even(x)]
pp(evens)

# ex 2
dict_evens = {x : [x, x*x, x*x*x] for x in nums if is_even(x)}
pp(dict_evens)

# ex 3
dict_evens = {x : (x, x*x, x*x*x) for x in nums if is_even(x)}
pp(dict_evens)

# ex 4
dict_evens = [[x, x*x, x*x*x] for x in nums if is_even(x)]
pp(dict_evens)