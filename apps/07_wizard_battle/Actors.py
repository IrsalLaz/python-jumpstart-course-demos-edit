class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def fight(self, creature):
        print(f"The {self.name} fights {creature.name}!")


class Wizard(Creature):
    print("this is Wizard")


class SmallAnimal(Creature):
    print("this is smallAnimal")


class Dragon(Creature):
    print("this is Dragon")
