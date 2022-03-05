# We will use class to define our own datastructure
# It can be defined like this little example
class Car_manufacturer:
    def __init__(self, car):
        self.car = car

    def getCarName(self):
        return self.car

    def setCarName(self, car):
        self.car = car

car1 = Car_manufacturer("Maserati")
print("I have ordered a", car1.getCarName())

car1.setCarName("Lamborghini")
print("No no! I have actually ordered a", car1.getCarName())