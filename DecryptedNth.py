class UserMainCode(object):
    @classmethod
    def characterAt(cls, input1, input2):
        stre = input1[::2]
        ints = [int(x) for x in input1 if x.isnumeric()]
        res = []
        for i in range(len(ints)):
            res.append(stre[i] * ints[i])
        res = ''.join(res)
        try:
            return res[input2-1] if res[input2-1] in res else -1
        except IndexError:
            return -1

print(UserMainCode.characterAt("a2b3", 3))