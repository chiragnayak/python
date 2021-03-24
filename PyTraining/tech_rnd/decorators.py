import time

print("-" * 75)


def outer_function_decorator(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        end_time = time.time()

        diff = round(end_time - start_time, 2)
        print("function ", func.__name__, "took", diff, "sec")
        return val

    return inner_function


@outer_function_decorator
def calc_sqr(num):
    time.sleep(2)
    return num ** 2


@outer_function_decorator
def calc_cube(num):
    time.sleep(3)
    return num ** 3


print("cal_sqr", calc_sqr(5))
print("calc_cube", calc_cube(5))

print("-" * 75)


def display_emp(name, loc, sal):
    return f"{name} {loc} {sal}"




