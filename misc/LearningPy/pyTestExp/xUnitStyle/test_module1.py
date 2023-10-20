def test_module1_method1():  # will be considered for test parsing
    print("this is test_module1_method1")
    assert True


def test_module1_method2():  # will be considered for test parsing
    print("this is test test_module1_method2")
    assert True


class Test_class1:  # will be considered for test parsing
    def test_module1_class1_method1(self):  # will be considered for test parsing
        print("this is test test_module1_class1_method1")
        assert True

    def setup_class(cls):
        print("this is %% setup_class %% ")

    def teardown_class(cls):
        print("this is %% teardown_class %% ")

    def setup_method(self):
        print("this is ## setup_method ## ")

    def teardown_method(self):
        print("this is ## teardown_method ## ")

class My_test_class2:  # will NOT be considered for test parsing
    def test_module1_class2_method1(self):  # will NOT be considered for test parsing as class is not considered
        print("this is test test_module1_class2_method1")
        assert True




def setup_module():
    print("this is ** setup_module ** ")


def teardown_module():
    print("this is ** tear_module ** ")


def setup_function(function):
    print("this is -- setup_function --")
    if function == test_module1_method1 :
        print ("this is Sparta !!")
    elif function == test_module1_method2:
        print ("this is India !!")

def teardown_function(function):
    print("this is -- teardown_function --")
