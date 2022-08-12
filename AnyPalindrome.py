def anyPalindrome(s):
    res = []
    for i in range(len(s)):
        if s[:i] + s[i + 1:] == s[:i] + s[i + 1:][::-1]:
            res.append(True)
    return any(res)

name = "nitina"
print(anyPalindrome(name))