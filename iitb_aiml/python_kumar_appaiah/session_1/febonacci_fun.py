
# RAMANUJAN NUMBER
# R = a^3 + b^3 = c^3 + d^3

my_dict = dict()
tuple_list = [(x, y, x** 3 + y ** 3) for x in range(1, 21) for y in range(1, 21)]

for x in tuple_list:
    if x[-1] in my_dict:
        my_dict[x[-1]].append((x[0], x[1]))
    else:
        my_dict[x[-1]] = [(x[0], x[1])]

for x, y in my_dict.items():
    if len(y) > 2:
        print(x, " is RAMANUJAN NUMBER. Pairs are: ", y)


