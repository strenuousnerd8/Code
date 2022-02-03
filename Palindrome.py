def palindromeCheck(word):
    palindrome = list(word)
    palindrome.reverse()
    palindrome = ''.join(palindrome)
    if palindrome == word:
        return True
    else:
        return False
    return palindrome

print(palindromeCheck("what"))
print(palindromeCheck("nitin"))