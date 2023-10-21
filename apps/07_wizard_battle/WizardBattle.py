import time


def main():
    print("-------------------------")
    print("WIZARD BATTLE".center(25, " "))
    print("-------------------------")

    game_loop()


def game_loop():
    looping = True

    while looping:
        # put the logic game here
        print("The wizard {player} sees a {creature}.")

        action = input("Do you [a]ttack, [r]un away, or [l]ook around? ")

        if action == "a":
            # put the attack logic here
            print()

        elif action == "r":
            print("The wizard {player} runs away to finds some cover.")
            # pause the game and then continue
            time.sleep(3)
            print("The wizard {player} continue continue his journey.")

        elif action == "l":
            print("The wizard {player} look around and sees: ")
            # print all creature then continue
        else:
            break


if __name__ == '__main__':
    main()
