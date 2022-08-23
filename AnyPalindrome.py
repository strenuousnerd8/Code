def anyPalindrome(s):
    for i in range(len(s)):
        if s[:i] + s[i + 1:] == s[:i] + s[i + 1:][::-1]:
            return True
    return False

name = "nitina"
print(anyPalindrome(name))