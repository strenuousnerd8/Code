#Input 1, contagious digits. Input 2, target sum val
class Sum(object):
    @classmethod
    def targetSum(self, lis, tar):
        res = []
        for i in range(len(lis)):
            for j in range(len(lis)):
                if lis[i:j+1] != []:
                    if sum(lis[i:j+1]) == tar:
                        res.append(lis[i:j+1])
        return lis.index(res[0][0]), lis.index(res[0][1])

print(Sum.targetSum(
    list(map(int, input().split())),
    int(input())
))