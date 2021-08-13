class Car():
    def __init__(self, brand):
        self._brand = brand
        
    def getBrand(self):
        return self._brand

def hello(car: Car):
    print("hello " + car.getBrand())

world = lambda: hello(Car("Volvo"))
bello = lambda: hello(Car("BMW"))

world()
bello()

eval(compile("def hello():print('hello from the string')", "<string>", 'exec'))
hello()