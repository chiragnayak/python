import pytest

@pytest.fixture(params=[1, {"Chirag":"Nayak"} ])
def setUpDataParams(request):
    return request.param

def test_printMe(setUpDataParams):
    if type(setUpDataParams) is int:
        print("Param is Integer")
    elif type (setUpDataParams) is dict:
        print("Param is Dictionary")
        for key in setUpDataParams:
            print(key, "-->", setUpDataParams[key])