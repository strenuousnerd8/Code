def pigLatin(text):
    new_texts = text.split()
    result = []
    for word in new_texts:
        say = list(word)
        init  = say[0]
        del say[0]
        say.append(init)
        say.append("ay")
        say = ''.join(say)
        result.append(say)
    result = ' '.join(result)
    return result

print(pigLatin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pigLatin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"