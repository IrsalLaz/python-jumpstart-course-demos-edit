import random
import time
from Actors import Creature, Wizard, SmallAnimal, Dragon


def main():
    print("-------------------------")
    print("WIZARD BATTLE".center(25, " "))
    print("-------------------------")

    game_loop()


def game_loop():
    looping = True

    # define the player
    player = Wizard("Gondalf", 20)

    # define other creatures
    creatures = [
        SmallAnimal("Toad", 1),
        SmallAnimal("Bat", 5),
        Creature("Tiger", 12),
        Dragon("Fire Dragon", 50, True),
        Wizard("Evil Wizard", 100)
    ]

    while looping:
        # make the creature appear randomly
        creature = random.choice(creatures)
        print(f"The wizard {player.name} sees a {creature.name}.")

        action = input("Do you [a]ttack, [r]un away, or [l]ook around? ")

        if action == "a":
            if player.attack(creature):
                # if player attack the creature and return true, then the creature will be removed from the list
                creatures.remove(creature)
            else:
                # if the creature win he won't be removed from list, then game pause for 10 seconds
                time.sleep(10)
                print("\nThe wizard respawned with full health!")
            print()

        elif action == "r":
            print(f"The wizard {player.name} runs away to finds some cover.")
            # pause the game and then continue
            time.sleep(3)
            print(f"The wizard {player.name} continue continue his journey.")
            print()

        elif action == "l":
            print(f"The wizard {player.name} look around and sees: ")
            # print all remaining creature then continue
            for creature in creatures:
                print(creature)
                # print(f" * A level {creature.level} of {creature.name}.")
            print()

        else:
            print("OK, exiting game... see you!")
            break


if __name__ == '__main__':
    main()
