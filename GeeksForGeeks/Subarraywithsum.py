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
        for i in range(len(res[0])):
            print(lis.index(res[0][i]))

Sum.targetSum(
    list(map(int, input().split())),
    int(input())
)