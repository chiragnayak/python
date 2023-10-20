print('-' * 75)

def calc(num, value=2):
    return num ** value

def display_emp(name, loc, sal):
    return f'{name} from {loc} earns Rs.{sal}'

# Wrapper function
def wrapper(func, *args, **kwargs):
    print(f'Calling Function "{func.__name__}"')
    ret = func(*args, **kwargs)
    print('Returns -', ret)

wrapper(calc, 5)
wrapper(calc, 5, 3)
wrapper(display_emp, 'justin', loc='bangalore', sal=5000)

print('-' * 75)

# Wrapper function
def wrapper_obj(func, args=(), kwargs={}):
    print(f'Calling Function "{func.__name__}"')
    ret = func(*args, **kwargs)
    print('Returns -', ret)

wrapper_obj(calc, (5,))
wrapper_obj(calc, (5, 3))
wrapper_obj(display_emp, kwargs={'name': 'davies', 'loc': 'bangalore', 'sal': 5000})

print('-' * 75)
