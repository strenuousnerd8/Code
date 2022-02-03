mystr ="whyisthisworldsofunny"
findsub = "is"
if findsub in mystr:
    print("At " + str(mystr.index(findsub)) + " index first and then occured : " + str(mystr.count(findsub)) + " time/s.")
else:
    print("Substring: <{}> not found".format(findsub))