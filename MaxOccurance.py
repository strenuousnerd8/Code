# Word with highest number of repeated characters without characters in event token

eventToken = 'xyfidwg'

def maxCharOccurance(word):
    words = word.split()
    my_dict = dict()
    res = []
    for i in words:
        my_dict[i] = {}
        for j in i:
            if j not in my_dict[i]:
                my_dict[i][j] = 1
            else:
                my_dict[i][j] += 1
    for i in my_dict:
        res.append(max(my_dict[i].values()))
    return filterToken(words[findMax(res)])

def findMax(arr):
    count = globmax = 0
    index = 0
    for i in range(len(arr)):
        if arr[i] > count:
            count = arr[i]
        if count > globmax:
            globmax = count
            index = i
    return index

def filterToken(word):
    res = ""
    for i in word:
        if i not in eventToken:
            res += i
    return res

print(maxCharOccurance(input()))