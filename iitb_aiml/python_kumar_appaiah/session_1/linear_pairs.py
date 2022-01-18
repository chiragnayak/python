from numpy import arange

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
s_str = input("number step : ")
s = int(s_str) if "." not in s_str else float(s_str)

number_pairs_equal = list()
number_pairs_less = list()
for x in arange(0, c, s):
    for y in arange (0, c, s):
        calc = (a * x) + (b * y)
        if calc == c:
            number_pairs_equal.append((x, y))
        elif calc < c:
            number_pairs_less.append((x, y))
        else:
            continue

print("Pairs on line represented by ax + by = c are. \n {}".format(number_pairs_equal))
print("Pairs on line represented by triangle (area) under line ax + by = c are. \n {}".format(number_pairs_less))

