import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f" * A level {self.level} of {self.name}."

    def roll_the_dice(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, creature):
        print(f"The {self.name} fights {creature.name}!")

        player_role = self.roll_the_dice()
        creature_role = creature.roll_the_dice()

        print(f"The wizard roles {player_role}")
        print(f"The {creature.name} roles {creature_role}")

        # rule of the game
        if player_role >= creature_role:
            print(f"The wizard has triumphant over the {creature.name}!")
            # increase the level of the player by 1
            self.level += 1
            return True     # the creature will be removed from the list
        else:
            print(f"The wizard {self.name} has been defeated by the {creature.name}")
            return False   # the player will be defeated


class SmallAnimal(Creature):
    # modify the base method so the small animal will be easier to defeat
    def roll_the_dice(self):
        small_animal_role = super().roll_the_dice()
        return small_animal_role / 2


class Dragon(Creature):
    def __init__(self, name, level, breath_fire):
        super().__init__(name, level)
        self.breath_fire = breath_fire

    def roll_the_dice(self):
        dragon_role = super().roll_the_dice()
        fire_modifier = 5 if self.breath_fire else 1
        dragon_role *= fire_modifier
        return dragon_role
