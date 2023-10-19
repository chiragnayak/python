class OneAway:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def one_replaced(self):

        l1 = len(self.s1)
        l2 = len(self.s2)

        if l1 != l2 :
            return False

        diff = 0
        for i in range(0, l1):
            if self.s1[i] != self.s2[i]:
                diff += 1

        if diff > 1:
            return False
        else:
            return True

    def one_inserted_or_removed(self):

        l1 = len(self.s1)
        l2 = len(self.s2)

        large = self.s1 if l1 > l2 else self.s2
        small = self.s1 if l1 < l2 else self.s2
        max = len(large)

        pos_l = 0
        pos_s = 0
        diff = 0
        for i in range(0, max):
            if large[pos_l] == small[pos_s]:
                pos_l += 1
                pos_s += 1
            else:
                pos_l += 1
                diff += 1

        if diff > 1:
            return False
        else:
            return True


if __name__ == "__main__":

    s1 = ""
    s2 = ""

    obj = OneAway(s1, s2)

    print(f" One Inserted or Removed : {obj.one_inserted_or_removed()}")
    print(f" One Replaced : {obj.one_replaced()}")

    if obj.one_replaced() or obj.one_inserted_or_removed():
        print("One Away/No Edit !!")
    else:
        print("NOT One Away !!")