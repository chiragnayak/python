from pytest import raises


def raiseValueError():
    return 1/0


def test_valueError():
    with raises(ZeroDivisionError):
        raiseValueError()
