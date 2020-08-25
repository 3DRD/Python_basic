class Point:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} Talks")


point1 = Point("DRD")
point1.talk()
