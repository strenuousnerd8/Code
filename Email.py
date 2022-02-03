def changeEmail(emailInfo):
    email, oldDomain, newDomain = emailInfo
    if "@" + oldDomain in email:
        index = email.index("@" + oldDomain)
        newEmail = email[:index] + "@" + newDomain
        # or newEmail = email.replace("@" + oldDomain, "@" + newDomain)
    return f"{newEmail}".format(newEmail)

print(changeEmail(("zakkiwat@outlook.com", "outlook.com", "gmail.com")))
print(changeEmail(("azimat@xbox.com", "xbox.com", "outlook.com")))