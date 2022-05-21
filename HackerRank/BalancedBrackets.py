def isBalanced(s):
    # Write your code here
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    if len(s) > 0: return "NO"
    return "YES"

if __name__ == '__main__':
        result = isBalanced(input())
        print(result)