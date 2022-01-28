str = str(input())
print(True if all(x in str for x in ['a','e','i','o','u']) else False)