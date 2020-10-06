'''
"Generators" are defined by any Python function/def that has used yield atleast once.

Simply speaking, a generator is a function that returns an object (iterator)
which we can iterate over (one value at a time).

- Generators are single use objects
- To re-create a generator from a generator expression (see generator_expression), you must execute teh expression again
'''
import random
from pprint import pprint as pp


# Infinite Stream of even numbers
def demo_even_number_generator():
    '''if you remove "while" condition, only one value will be yielded. i.e. for first succesfull if even number comes
    of StopIteration if odd number comes.
    in case, even is generated in first call, next call will, throw StopIteration Exception.
    to keep the value yielded, we need this infinite while loop'''
    while True:
        num = random.randint(1, 100)
        if num % 2 == 0:
            yield num


generator_obj = demo_even_number_generator()
pp(generator_obj)
pp(next(generator_obj))
pp(next(generator_obj))
pp(next(generator_obj))
pp(next(generator_obj))


def get123():
    print("About to Give 1")
    yield 1
    print("About to Give 2")
    yield 2
    print("About to Give 3")
    yield 3
    print("About to Give Exception")


generator_obj2 = get123()
pp(next(generator_obj2))
pp(next(generator_obj2))
pp(next(generator_obj2))

# throws exception
# pp(next(generator_obj2))

obj3 = get123()
obj4 = get123()

# two different generator objects, can be traversed/yielded/maintain-state independently
pp(obj3 is obj4)

pp(next(obj3))
pp(next(obj3))
pp(next(obj4))

# very important example
for x in get123():
    pp(x)  # check : do not use "next(x)"

for x in get123():
    print(x)
    '''You can put as many statements till the loop is complete. Generator will be called
    first in start (before entering the for loop) and then only when the loop iteration is complete.
    As per programming flow. :)'''
    print("This is {}. ".format(x))
