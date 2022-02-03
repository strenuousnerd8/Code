def toCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

for fahrenheit in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(fahrenheit, toCelsius(fahrenheit)))