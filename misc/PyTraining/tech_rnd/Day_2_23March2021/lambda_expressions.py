print('-' * 75)

def calc_func(num, value=2):
    return num ** value

print(calc_func, '-', type(calc_func))
print('calc_func 1 -', calc_func(5))
print('calc_func 2 -', calc_func(5, 3))

print('-' * 75)

# Lambda Expressions
# Anonymous Functions (Nameless Functions)
# One-Liner Function
# Can take any number of parameters in any form
# But it evaluates only one expression
# The evaluated expression will be return to the caller by default
calc_lambda = lambda num, value=2: num ** value

print(calc_lambda, '-', type(calc_lambda))
print('calc_lambda 1 -', calc_lambda(5))
print('calc_lambda 2 -', calc_lambda(5, 3))

print('-' * 75)
