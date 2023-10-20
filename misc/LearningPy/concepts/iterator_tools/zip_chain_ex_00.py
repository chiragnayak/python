'''
synchronize iteration across two or more iterables
'''
from itertools import chain


def get1234():
    yield 1
    yield 2
    yield 3
    yield 4


gen_obj1 = get1234()
gen_obj2 = get1234()

print(next(gen_obj1))
print(next(gen_obj1))
zip_obj = zip(gen_obj2, gen_obj1)
print(next(zip_obj))  # (1,3)

sunday = [11, 22, 33, 44, 55, 66, 77]
monday = [88, 99, 78, 12, 34, 56, 78]
Tuesday = [1, 2, 3, 4, 5, 6 ,7]

for x in zip(sunday, monday):
    print(x) # position wise tuple formed (11, 88) (22, 99)...

'''
Return a chain object whose .__next__() method returns elements from the first iterable until it is exhausted, 
then elements from the next iterable, 
until all of the iterables are exhauste'''
value = chain(sunday, monday, Tuesday)

for x in value:
    print(x)
