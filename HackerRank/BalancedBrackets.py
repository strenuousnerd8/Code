def isBalanced(s):
    # Write your code here
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return "NO" if len(s) > 0 else "YES"

if __name__ == '__main__':
        result = isBalanced(input())
        print(result)