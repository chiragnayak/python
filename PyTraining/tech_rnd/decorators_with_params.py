import time

print("-" * 75)


def decorator_name_with_var(delay):
    def level_2_func(func):
        def level_3_func(*args, **kwargs):
            start_time = time.time()
            val = func(*args, **kwargs)
            time.sleep(delay)
            end_time = time.time()

            diff = round(end_time - start_time, 2)
            print("function ", func.__name__, "took", diff, "sec")
            return val
        return level_3_func
    return level_2_func


@decorator_name_with_var(2)
def calc_sqr(num):
    return num ** 2


@decorator_name_with_var(3)
def calc_cube(num):
    return num ** 3


print("cal_sqr", calc_sqr(5))
print("calc_cube", calc_cube(5))

print("-" * 75)


def display_emp(name, loc, sal):
    return f"{name} {loc} {sal}"
