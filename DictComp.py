my_dict = dict()

my_dict = {i: i * i for i in range(1,11)}

print(my_dict)

my_dict = {k: v - k for (k, v) in my_dict.items() if v % 2 == 0 if v < 40}

print(my_dict)