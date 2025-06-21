# question 2.2.2
class Octopus:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def __repr__(self):
        return f"name: {self._name}\nage: {self._age}\n"


oc1 = Octopus("leonardo", 15)
oc2 = Octopus("messi", 22)

oc1.birthday()

print(oc1)
print(oc2)


# question 2.3.3
class Octopus:
    count_animals: int = 0

    def __init__(self, age, name="Octavio"):
        self._name = name
        self._age = age

        self.__class__.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, n_name):
        self._name = n_name

    def get_name(self):
        return self._name

    def get_count_animals(self):
        return self.__class__.count_animals

    def __repr__(self):
        return f"name: {self._name}\nage: {self._age}\n"


oc1 = Octopus(15, "leonardo")
oc2 = Octopus(22, "messi")

oc1.birthday()

print(oc1)
print(oc2)
print(f"{oc1.get_count_animals()} instances been created so far!")


# question 2.3.4
class Pixel:
    def __init__(self, r, g, b):
        self._green = g
        self._blue = b
        self._red = r
        self._x = 0
        self._y = 0

    def set_cords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        self._blue = self._red = self._green = (self._blue + self._red + self._green) // 3

    def print_pixel_info(self):
        color = ""
        if self._blue + self._red + self._green == self._blue:
            color = "Blue"
        elif self._blue + self._red + self._green == self._green:
            color = "Green"
        elif self._blue + self._red + self._green == self._red:
            color = "Red"

        print(f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) {color}")


p = Pixel(5, 6, 250)
p.print_pixel_info()
p.set_grayscale()
p.print_pixel_info()


# question 2.4.2
class BigThing(object):
    def __init__(self, obj):
        self.obj: object = obj

    def size(self):
        if isinstance(self.obj, int):
            return self.obj
        elif isinstance(self.obj, (str, list)):
            return len(self.obj)


my_thing = BigThing("balloon")
print(my_thing.size())
my_thing2 = BigThing(23)
print(my_thing2.size())


class BigCat(BigThing):
    def __init__(self, name, size):
        super().__init__(size)
        self._name = name

    def size(self):
        val = super(BigCat, self).size()
        if val > 15: return "Fat"
        if val > 20:  return "Very Fat"


# question 2.5
class Animal(object):
    Hayaton: list[object]
    def __init__(self):
        self._hunger = 0
        self._name = ""

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def set_name(self, name):
        self._name = name
        return self

    def set_hunger(self, hunger):
        self._hunger = hunger
        return self

    def feed(self):
        self._hunger += -1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof	")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, st=6):
        super().__init__()
        self._stink_count = st

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...	")


class Dragon(Animal):
    def __init__(self, c="Green"):
        super().__init__()
        self._color = c

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


zoo_list: list[Animal] = [Dog().set_hunger(10).set_name("Brownie"), Cat().set_hunger(3).set_name("Zelda"),
                          Skunk().set_hunger(0).set_name("Stinky"), Unicorn().set_hunger(7).set_name("Keith"),
                          Dragon().set_hunger(1450).set_name("Lizzy")]

Animal.Hayaton = zoo_list

# dict of functions
funcs_dict: dict[str, object] = {}
funcs_dict[Dog.__name__] = Dog.fetch_stick
funcs_dict[Cat.__name__] = Cat.chase_laser
funcs_dict[Skunk.__name__] = Skunk.stink
funcs_dict[Unicorn.__name__] = Unicorn.sing
funcs_dict[Dragon.__name__] = Dragon.breath_fire

for animal in zoo_list:
    print(f"{animal.__class__.__name__} {animal.get_name()}")
    while animal.is_hungry():
        animal.feed()

for animal in zoo_list:
    animal.talk()
    funcs_dict[animal.__class__.__name__](animal)







