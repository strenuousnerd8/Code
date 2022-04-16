# Find the difference between lengths of longest and shortest palindromes in a given string.
# Amazon Question
class Difference(object):
    @classmethod
    def finder(self, stri):
        res = []
        for i in range(len(stri)):
            for j in range(len(stri)):
                if stri[i:j+1] == stri[i:j+1][::-1] and stri[i:j+1] != '':
                    res.append(stri[i:j+1])
        lens = [len(i) for i in res]
        print(max(lens) - min(lens))

Difference.finder('level')