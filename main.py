from random import choice

score = 0
system_score = 0

picks = ("rock", "paper", "scissors")


def main():
    global score, system_score

    while True:
        user_pick = input("Choose - rock / paper / scissors (X to quit): \n- ")

        if user_pick.lower() == "x":
            break

        if user_pick.lower() not in picks:
            print("Incorrect pick :(")
            continue

        system_pick = choice(picks)
        print(f"Your choice - {user_pick}, system choice - {system_pick}")

        if (
            (user_pick.lower() == "rock" and system_pick.lower() == "paper")
            or (user_pick.lower() == "paper" and system_pick.lower() == "rock")
            or (user_pick.lower() == "scissors" and system_pick.lower() == "paper")
        ):
            score += 1
            print(f"You won computer, score - {score} \n")

        elif user_pick.lower() == system_pick.lower():
            print(f"Draw, nobody won! Your score - {score} \n")

        else:
            system_score += 1
            print(f"You lost :(, your score - {score} \n")

    print(f"Your final score - {score}, system final score - {system_score}")

    if score < system_score:
        print("You lost :( \n")
    elif score == system_score:
        print("Draw, nobody won! \n")
    else:
        print("You won, congratulations! :) \n")


if __name__ == "__main__":
    main()
