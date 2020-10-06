from pprint import pprint as pp


def take(count, iterable):
    counter = 0;
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    list = [3, 6, 6, 2, 1, 4, 4]
    for item in take(3, distinct(list)):
        pp(item)


run_pipeline()