"""
Single
"""


class A:

    def __init__(self):
        print("In A")


class B(A):
    pass


class C(A):

    def __init__(self):
        super.__init__()  # or A.__init__(self)
        print("In C")


class D(B):

    def __init__(self):
        super.__init__()  # or A.__init__(self)
        print("In C")


class E:

    def __init__(self):
        super.__init__()  # or A.__init__(self)
        print("In C")

"""
multiple inheritance

__init__ to be looked from left to right F > E > A
for some method say calc, if present in E and A both with same signature, 
then also, the calling via F's object, will look first in F, then E and then A, if not then exception.
So, rule of "first valid find"
"""
class F(E, A):

    def __init__(self):
        super.__init__()  # or A.__init__(self)
        print("In C")

if __name__ == "__main__":
    """
    if no __init__ in B, look for init in parent
    if init in B, init of B will be executed only
    """
    B()
    C()
