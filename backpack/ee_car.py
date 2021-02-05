class Person:
    """A person!"""

    def __init__(self, name, shout_phrase):
        self.name = name
        self.shout_phrase = shout_phrase

    def shout(self):
        print(f"{self.name} says '{self.shout_phrase}!'")


class Car:
    """A vehicle"""

    def __init__(self, brand, color, name, driver, top_speed_mph):
        self.brand = brand
        self.color = color
        self.name = name
        self.driver = driver
        self.top_speed_mph = top_speed_mph

        self.items = []

    def drive(self):
        print(f"{self.driver.name} drives the car.")
        self.driver.shout()

    def describe(self):
        print(f"This car is a {self.color} {self.brand} and driven by {self.driver.name}")

    def pack_car(self, item):
        self.items.append(item)

    def look_car(self):
        amount_items = 0

        if self.items:
            for item in self.items:
                amount_items = int(amount_items)
                amount_items += 1

                print(f'i found a {item} in {self.name}')

                amount_items = str(amount_items)
                print(f'in {self.name} there is/are {amount_items} item(s)')
        else:
            print(f'there are no items in your {self.brand}')

    def unpack_car(self):
        self.items = []


def race(car1, car2):
    car1.describe()
    car2.describe()

    car1.drive()
    car2.drive()

    if car1.top_speed_mph > car2.top_speed_mph:
        print(f"{car1.driver.name} wins!")
    else:
        print(f"{car2.driver.name} wins!")


person = Person(name='Jeffrey', shout_phrase='Hells Yes')
car = Car(
    color='Grey', brand='Toyota', name='Imogen', driver=person, top_speed_mph=60
)

person2 = Person(name='Elizabeth', shout_phrase='Yaaaaaaay')
car2 = Car(
    color='Hot Pink', brand='Subaru', name='Flash', driver=person2, top_speed_mph=189
)

race(car, car2)
