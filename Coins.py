# Find charity given my a person i**2 coins for n days
class UserMainCode(object):
    @classmethod
    def charity(cls, input1):
        return sum([i**2 for i in range(1, input1+1)])

print(UserMainCode.charity(2))