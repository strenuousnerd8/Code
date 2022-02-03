def charCount(yourStr):
    result = {}
    for letter in yourStr:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(charCount("What is going on"))