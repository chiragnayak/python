print('-' * 75)

import time

# Decorators => Design Pattern (Nested Functions and Callback References)
def set_delay(delay):
    def measure_time_taken(func):
        def exec_function(*args, **kwargs):
            st_time = time.time()
            f_ret = func(*args, **kwargs)
            time.sleep(delay)
            end_time = time.time()

            diff = round(end_time - st_time, 2)
            print(f'{func.__name__} took {diff}secs')
            return f_ret, diff
        return exec_function
    return measure_time_taken

@set_delay(1)
def calc_sqr(num):
    sqr = num ** 2
    return sqr

@set_delay(2)
def calc_cube(num):
    cube = num ** 3
    return cube

@set_delay(3)
def display_emp(name, loc, sal):
    return f'{name} from {loc} earns Rs.{sal}'

print('calc_sqr -', calc_sqr(5))
print('calc_cube -', calc_cube(5))
print('display_emp -', display_emp('manual', 'mumbai', 8000))

print('-' * 75)
