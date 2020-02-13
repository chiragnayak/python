import pytest


@pytest.fixture(scope="function", autouse=True)
def functionScopedFixture():
    print("This is functionScopedFixture set-up area")
    yield
    print("This is functionScopedFixture teardown area")


@pytest.fixture(scope="class", autouse=True)
def classScopedFixture():
    print("This is classScopedFixture set-up area")
    yield
    print("This is classScopedFixture teardown area")


@pytest.fixture(scope="module", autouse=True)
def moduleScopedFixture():
    print("This is moduleScopedFixture set-up area")
    yield
    print("This is moduleScopedFixture teardown area")


# @pytest.fixture(scope="Session")
# def sessionScopedFixture():
#     print("This is sessionScopedFixture set-up area")
#     yield
#     print("This is sessionScopedFixture teardown area")

class Test_UserClass:

    def test_1(self):
        print("test_1 OK")
        assert True

    def test_2(self):
        print("test_2 OK")
        assert True


