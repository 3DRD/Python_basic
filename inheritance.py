class Mammal:
    def walk(self):
        print("Walks")


class Dog(Mammal):

    def bark(self):
        print("Barks")


class Cat(Mammal):

    def Meow(self):
        print("Meows")


dog1=Dog()
cat1=Cat()
dog1.bark()
dog1.walk()
cat1.Meow()
cat1.walk()


