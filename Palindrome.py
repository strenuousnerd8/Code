def palindromeCheck(word):
    return True if word[::-1] == word else False

print(palindromeCheck("what"))
print(palindromeCheck("nitin"))