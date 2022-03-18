# Find character at Nth index of a decrypted string
class UserMainCode(object):
    @classmethod
    def characterAt(cls, input1, input2):
        res = ''.join([input1[i] * int(input1[i+1]) for i in range(0, len(input1), 2)])
        try:
            return res[input2-1]
        except IndexError:
            return str(-1)

print(UserMainCode.characterAt("a3b2", 7))