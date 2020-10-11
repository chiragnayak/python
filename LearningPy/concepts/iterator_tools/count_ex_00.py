'''
itertools.count()
An unbounded arithmetic sequence of integers
'''

from itertools import count

for x in count(0, 5):
    print(x)
    if x == 1000:
        break

