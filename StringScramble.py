def StringScramble(str1,str2):
  # code goes here
  str1, str2 = list(str1), list(str2)
  newstr = [i for i in str2 if i in str1]
  return True if ''.join(newstr) == ''.join(str2) else False

# keep this function call here
print(StringScramble(input(), input()))