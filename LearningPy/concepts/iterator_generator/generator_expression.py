'''
Syntax: Generators are type of comprehension that generates generator object.
Syntax is similar to list comprehension, instead of square brackets [], parenthesis are used ()
(expr(item) for item in iterable)

where needed : where you need,
- lazy evaluation of generators
and
- declarative way of writing comprehensions

Note:
- Generator are single use objects. Everytime we call generator function, a new generator object is created.
- To re-create a generator-object from a generator-expression, you must execute the expression again
- once it is used, it will not yield in the next call. See below &&&
'''
from LearningPy.concepts import util

'''
Task: to generate squares of 1 million numbers.
No memory is consumed, as no list of numbers is created yet, lazy evaluation, just a generator
object is created.

once we call upon a list() on this, then the generator will yield
'''

'''generator expression called and generator object is created'''
million_number_square = (x * x for x in range(1, 1000001))
print(million_number_square)

'''yielded or we can say it is consumed'''
list_of_first_ten = list(million_number_square)[:10]
print(list_of_first_ten)

'''&&& once it is yielded/consumed in someway, it will not yield in the next call. Below will print []'''
list_of_first_ten = list(million_number_square)[:10]
print(list_of_first_ten)

'''call again the generator-expression to get new generator object
generator expression called and generator object is created'''
million_number_square_02 = (x * x for x in range(1, 1000001))
print(million_number_square is million_number_square_02)

'''new generator object consumed'''
list_of_last_ten = list(million_number_square_02)[-10:]
print(list_of_last_ten)

''' Sum of squares if first 1 million numbers.'''
print(sum(x * x for x in range(1, 10000001)))


''' Sum of even numbers in first 1000 numbers '''
print(sum(x for x in range(1000) if util.is_even(x)))
