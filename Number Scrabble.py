#file:CS112_A1_T2_Game2_20231166
#purpose:The "Number scrabble" is a game consists of nine numbers (1:9). the two players should take turns in picking numbers, The numers can not be chosen more than one, and finally the player who succeded in collecting three numbers their sum equals fifteen is the winner
#Author:Mariam Medhat Shawky Ahmed
#ID:20231166
# Welcome message and game instructions
print("Welcome to the game!")
print("The game consists of nine numbers.")
print("The objective is to get the number 15 from the summation of three chosen numbers.")
print("Players cannot choose the same number again.")
print("For example, if one player chooses the number 1, it cannot be chosen again by either player.")
print("Enjoy!")

first_player = str(input("player1 please insert your name: "))     # Input player names
second_player = str(input("player2 please enter your name: "))

# Set initial variables
set_numbers = [1,2,3,4,5,6,7,8,9]
allowed_nums = [1,2,3,4,5,6,7,8,9]
counter = 0                               # Counter to keep track of rounds
x = []                                    # List to store player 1's chosen numbers
y = []                                    # List to store player 2's chosen numbers
sum1 = 0
sum2 = 0

while counter <= 4:                       # Main game loop
    while True:                           # player one input loop
        try:
            player_one_num = int(input(f"{first_player},please enter a valid number from 1 to 9 : "))
            if player_one_num not in allowed_nums:                  # Check if the input is a valid number
                print("Invalid input. ")
                continue
            if player_one_num not in set_numbers:
                print("Number already chosen.")
                continue
            break
        except ValueError:
            print("Integers are only allowed.")
    x.append(player_one_num)                        # Add chosen number to player 1's list and remove from available numbers
    set_numbers.remove(player_one_num)              # remove chosen number  from available numbers


    if counter == 2:                                # Check if player 1 has won after certain rounds
        if sum(x) == 15:
            print(f"{first_player} congratulations you have won!")
            q = input("do you want to play again (yes/no) ")          # Ask if players want to play again
            if q == "yes":                                          # Restart or exit based on player input
                sum1, sum2, set_numbers, counter, x, y = 0, 0, [1,2,3,4,5,6,7,8,9], 0, [], []    # Reset game variables
                continue
            elif q == "no":
                print("Exiting the program, thank you!")
                break
            else:
                print("sorry! I can not get what you want. Existing the game...")
                break                   # Similar logic and checks continue for remaining rounds and 2nd players


    elif counter == 3:
        sum1 = [x[1] + x[0] + x[3], x[0] + x[2] + x[3], x[1] + x[2] + x[3]]
        if 15 in sum1:
            print(f"{first_player} congratulations you have won!")
            q=input("do you want to play again (yes/no) ")
            if q == "yes":
                sum1, sum2, set_numbers, counter, x, y = 0, 0, [1,2,3,4,5,6,7,8,9], 0, [], []
                continue
            elif q == "no":
                print("Exiting the program, thank you!")
                break
            else:
                print("Exiting the game due to unrecognized input...")
                break


    elif counter == 4:
        sum3 = [x[0]+x[1]+x[4], x[0]+x[2]+x[4], x[0]+x[3]+x[4], x[1]+x[2]+x[4], x[1]+x[3]+x[4]]
        if 15 in sum3:
            print(f"{first_player} congratulations you have won!")
            q=input("do you want to play again (yes/no) ")
            if q == "yes":
                sum1, sum2, set_numbers, counter, x, y = 0, 0, [1,2,3,4,5,6,7,8,9], 0, [], []
                continue
            elif q == "no":
                print("Exiting the program, thank you!")
                break
            else:
                print("Exiting the game due to unrecognized input...")
                break


        else:
            print("the game ended, no one has won")
            q=input("do you want to play again (yes/no) ")
            if q == "yes":
                sum1, sum2, set_numbers, counter, x, y = 0, 0, [1,2,3,4,5,6,7,8,9], 0, [], []
                continue
            elif q == "no":
                print("Exiting the program, thank you!")
                break
            else:
                print("Exiting the game due to unrecognized input...")
                break


    if counter < 4 :                             # loop included in the main loop
        while True:                           # to avoid talking inputs from the second user in the last round
            try:
                player_two_num = int(input(f"{second_player},please enter a valid number from 1 to 9 : "))
                if player_two_num not in allowed_nums:
                    print("Invalid input. ")
                    continue
                if player_two_num not in set_numbers:
                    print("Number already chosen.")
                    continue
                break
            except ValueError:
                print("Integers are only allowed.")
        y.append(player_two_num)
        set_numbers.remove(player_two_num)


        if counter == 2:
            if sum(y) == 15:
                print(f"{second_player} congratulations you have won!")
                q=input("do you want to play again (yes/no) ")
                if q == "yes":
                    sum1, sum2, set_numbers, counter, x, y = 0, 0, [1,2,3,4,5,6,7,8,9], 0, [], []
                    continue
                elif q == "no":
                    print("Exiting the program, thank you!")
                    break
                else:
                    print("Exiting the game due to unrecognized input...")
                    break


        elif counter == 3:
            sum2 = [ y[0] + y[1] +y[3] , y[1] + y[2] + y[3] , y[0] +y[2] + y[3] ]
            if 15 in sum2:
                print(f"{second_player} congratulations you have won!")
                q=input("do you want to play again (yes/no) ")
                if q == "yes":
                    sum1, sum2, set_numbers, counter, x, y = 0, 0, [1,2,3,4,5,6,7,8,9], 0, [], []
                    continue
                elif q == "no":
                    print("Exiting the program, thank you!")
                    break
                else:
                    print("Exiting the game due to unrecognized input...")
                    break

    counter += 1                        # Increment round counter

