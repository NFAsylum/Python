from random import randint, random, randrange

def Play():
    choice = "";
    otherChoice = "";

    try:
        choice = int(input("Write 1 for Rock, 2 for Paper and 3 for Scissors: \n"));
    except:
        choice = 10;

    otherChoice = randrange(1,3);

    try:
        if choice <= 3 and choice >= 0:
            match choice:
                case 1:
                    print("You choose Rock");
                case 2:
                    print("You choose Paper");
                case 3:
                    print("You choose Scissors");
                case _:
                    print("Command unidentified");
        else:
            print("Not an option");
    except:
        print("Not an option");

    match otherChoice:
        case 1:
            print("Opponent choose Rock");
        case 2:
            print("Opponent choose Paper");
        case 3:
            print("Opponent choose Scissors");

    if choice == otherChoice:
        print("Draw");
    elif (choice == 1 and otherChoice == 3) or (choice == 2 and otherChoice == 1) or (choice == 3 and otherChoice == 2):
        print("Won");
    else:
        print("Lost");

    choice = "";
    otherChoice = "";

    print("\n");
    Play();

Play();