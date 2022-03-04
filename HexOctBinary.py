#Print hexadecimal, octal and binary values in a formatted table.
def print_formatted(number):
    for i in range(1, number+1):
        print(str(i) + "\t" + str(oct(i)[2:])  + "\t" + str(hex(i).upper()[2:]) + "\t" + str(bin(i)[2:]))

print_formatted(17)