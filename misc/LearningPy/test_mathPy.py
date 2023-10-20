from misc.LearningPy import mathPy


def test_mul():
    x = mathPy.mul(5, 4)
    assert x == 20


def test_add1():
    y = mathPy.add(10, 20)
    assert y == 30


def test_add2():
    y = mathPy.add(10, 20)
    assert y != 20


def test_add3():
    y = mathPy.add(10, 20)
    assert y != 330
