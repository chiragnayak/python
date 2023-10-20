print('-' * 75)

# Inheritance
# Class which is inherited => Base/Super/Parent
# Class which is inheriting => Derived/Sub/Child

print('Single - C1 is inherited by C2')

class A:
    num = 5

    def __init__(self):
        self.num = 50
        print('In A')

    def calc(self, num, value):
        return (num ** value) ** 2

class B(A):
    pass

obj_b = B()

print('-' * 75)

print('Hierarchial - C1 is inherited by C2 and C3')

class C(A):
    def __init__(self):
        super().__init__()          # A.__init__(self)
        self.value = 2
        print('In C')

    def calc(self):
        return self.num ** self.value

obj_c = C()
print('num using obj_c -', obj_c.num)
print('calc using obj_c -', obj_c.calc())

print('-' * 75)

print('Multilevel - C1 is inherited by C2; C2 is inherited by C3')

class D(B):
    pass

obj_d = D()

print('-' * 75)

print('Multiple - C1 and C2 are inherited by C3')

class E:
    def __init__(self):
        print('In E')

    def calc(self, num, value):
        return num ** value

class F(A, E):
    pass

obj_f = F()
print('calc -', obj_f.calc(5, 2))

print('-' * 75)
