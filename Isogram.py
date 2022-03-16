def is_isogram(string):
    #your code here
    return len(set(list(string.lower()))) == len(string)

print(is_isogram("Dermatoglyphics"))