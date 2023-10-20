print('-' * 75)

import time

# Decorators => Design Pattern (Nested Functions and Callback References)
def measure_time_taken(func):
    def exec_function(*args, **kwargs):
        st_time = time.time()
        f_ret = func(*args, **kwargs)
        time.sleep(2)
        end_time = time.time()

        diff = round(end_time - st_time, 2)
        print(f'{func.__name__} took {diff}secs')
        return f_ret
    return exec_function

@measure_time_taken
def calc_sqr(num):
    sqr = num ** 2
    return sqr

@measure_time_taken
def calc_cube(num):
    cube = num ** 3
    return cube

@measure_time_taken
def display_emp(name, loc, sal):
    return f'{name} from {loc} earns Rs.{sal}'

print('calc_sqr -', calc_sqr(5))
print('calc_cube -', calc_cube(5))
print('display_emp -', display_emp('manual', 'mumbai', 8000))

print('-' * 75)
