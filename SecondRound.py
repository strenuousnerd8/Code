
class UserMainCode(object):
    @classmethod
    def charity(cls, input1):
        coins = 0
        for i in range(1, input1+1):
            coins += i ** 2
        return coins

print(UserMainCode.charity(2))