import pytest


@pytest.fixture()
def fixtureFunction1():
    print("this is fixture function1, setup() area")
    yield "This is my return value from setup"
    print("this is fixture function1, teardown() area")


@pytest.fixture()
def fixtureFunction2(request):
    print("this is fixture function2, setup() area")

    def teardown_1():
        print("this is teardown1 function area")

    def teardown_2():
        print("this is teardown2 function area")

    request.addfinalizer(teardown_1)
    request.addfinalizer(teardown_2)


def test_1(fixtureFunction1):
    print("test_1 OK")
    print(" viola : Set-up area returned value --> ", fixtureFunction1)
    assert True


def test_2(fixtureFunction2):
    print("test_2 OK")
    assert True
