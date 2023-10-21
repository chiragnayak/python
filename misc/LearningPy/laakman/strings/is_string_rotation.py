
class IsRotation:

    def __init__(self):
        pass

    def is_rotation(self, s1, s2):
        """
        split s1 with the first char of s2
        new_string = append [1] to [0] --> mimicking rotation
        this new_string should be substring of s2, if s2 is rotation of s1

        :param s1:
        :param s2:
        :return:
        """
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 != len_s2 or \
                (len_s1 == len_s2 == 0):
            return False

        sub_strs = s1.split(s2[0])
        sub_string = sub_strs[1]+sub_strs[0]

        if self.is_substring(s2, sub_string):
            return True
        else:
            return False

    def is_substring(self, s1, s2):

        pos_s1 = 0
        for i in range(0, len(s1)):
            if s2[0] == s1[i]:
                pos_s1 = i
                break

        start = pos_s1
        end = pos_s1+len(s2)

        if end > len(s1):
            return False

        sub_str = s1[start:end]

        if s2 == sub_str:
            return True
        else:
            return False


if __name__ == "__main__":

    s1 = "chirag"
    s2 = "iragch"

    o = IsRotation()
    print(o.is_rotation(s1, s2))