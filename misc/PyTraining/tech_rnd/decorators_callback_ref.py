print('-' * 75)


def cal(num, value=2):
    return num ** value


def display_emp(name, loc, sal):
    return f"{name} {loc} {sal}"


def wrapper(func_name, *args, **kwargs):
    print(f"calling func : {func_name.__name__}")
    ret = func_name(*args, **kwargs)
    print(ret)


wrapper(cal, 5)
wrapper(cal, 5, 3)
wrapper(display_emp, "chirag", loc="pune", sal=10000)

print('-' * 75)


def wrapper_obj(func_name, args=(), kwargs={}):
    print(f"calling func : {func_name.__name__}")
    ret = func_name(*args, **kwargs)
    print(ret)


wrapper_obj(cal, (5,))
wrapper_obj(cal, (5, 3))
wrapper_obj(display_emp, ("chirag",), {"loc": "pune", "sal":10000})
wrapper_obj(display_emp, kwargs={"name":"chirag", "loc": "pune", "sal":20000})

print('-' * 75)
