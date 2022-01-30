from turtle import color


class Apple:
    def greet(self):
        return "You have an {} of memory {} and {} color".format(self.phone, self.memory, self.color)

myphone = Apple()
myphone.phone = "iPhone 13 Pro Max"
myphone.memory = 512
myphone.color = "Blue"

print(myphone.greet())