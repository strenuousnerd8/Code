#Tuples and Unpacking
def formatFun(emailInfo):
    result = []
    for email, name in emailInfo:
        result.append("{name} <{email}>".format(name = name, email = email))
    return (result)
print(formatFun([("zakkiwat@gmail.com", "Faiz A."), ("azeemtalikoti@gmail.com", "Azim AT.")]))

#list Comprehension
languages = ['C', 'Java', 'Rust', 'Kotlin', 'Python', 'C++', 'JavaScript']
lengths = sum([len(language) for language in languages])
print(lengths)

multifive = sum([x for x in range(1, 101) if x % 5 == 0])
print(multifive)