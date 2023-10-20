
class CheckPermutations :

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def get_count_dict(self, s1):

        dic = {}
        for c in s1:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1

        return dic

    def check_permutation(self):

        if len(self.s1) != len(self.s2):
            return False

        dic1 = self.get_count_dict(self.s1)
        dic2 = self.get_count_dict(self.s2)

        for k, v in dic1.items():
            if not(k in dic2 and dic2[k] == dic1[k]):
                return False

        return True


if __name__ == "__main__":

    s1 = "chira"
    s2 = "cihar"

    obj = CheckPermutations(s1, s2)
    print(obj.check_permutation())