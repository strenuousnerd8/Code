# Variables initialize, they dont lock each other when assigned to
a = 10
b = 10
print("Before updating: ", a, b)
a = 20
print("After updating: ", a, b)

# So, if we want to lock assignment to a value, we use dictionary
a = {'value' : 10}
b = a
print("Before updating: ", a, b)
a["value"] = 20
print("After updating: ", a, b)