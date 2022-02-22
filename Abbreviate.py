# Abbreviation from text
print(''.join([x[0].upper() for x in str(input()).split() if x[0].isalpha()]))