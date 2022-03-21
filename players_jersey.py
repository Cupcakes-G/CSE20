'''
8.24 LAB*: Program: Soccer team roster (Dictionaries)
This program will store roster and rating information for a soccer team.
Coaches rate players during tryouts to ensure a balanced team.

(1) Prompt the user to input five pairs of numbers: A player's jersey number (0 - 99) and the player's rating (1 - 9). S
tore the jersey numbers and the ratings in a dictionary. Output the dictionary's elements with the jersey numbers in ascending order
(i.e., output the roster from smallest to largest jersey number)

(2) Implement a menu of options for a user to modify the roster. Each option is represented by a single character.
The program initially outputs the menu, and outputs the menu after a user chooses an option.
The program ends when the user chooses the option to Quit. For this step, the other options do nothing.
'''

player1_num = int(input("Enter player 1's jersey number:\n"))
player1_rating = int(input("Enter player 1's rating:\n"))

player2_num = int(input("\nEnter player 2's jersey number:\n"))
player2_rating = int(input("Enter player 2's rating:\n"))

player3_num = int(input("\nEnter player 3's jersey number:\n"))
player3_rating = int(input("Enter player 3's rating:\n"))

player4_num = int(input("\nEnter player 4's jersey number:\n"))
player4_rating = int(input("Enter player 4's rating:\n"))

player5_num = int(input("\nEnter player 5's jersey number:\n"))
player5_rating = int(input("Enter player 5's rating:\n"))

players = {player1_num: player1_rating, player2_num: player2_rating, player3_num: player3_rating,
           player4_num: player4_rating, player5_num: player5_rating}

players_jersey = sorted(players.keys())
print("\nROSTER")
for x in players_jersey:
    print(f'Jersey number: {x}, Rating: {players[x]}')

print(
    "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")

option = input("Choose an option:\n")
while option != "q":
    if option == "o":
        print("\nROSTER")
        for x in players_jersey:
            print(f'Jersey number: {x}, Rating: {players[x]}')
        print(
            "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
        option = input("Choose an option:\n")
    if option == "a":
        player_num = int(input("Enter a new player's jersey number:\n"))
        player_rating = int(input("Enter the player's rating:\n"))
        players[player_num] = player_rating
        players_jersey = sorted(players.keys())
        print(
            "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
        option = input("Choose an option:\n")
    if option == "d":
        player_del = int(input("Enter a jersey number:"))
        players.pop(player_del)
        players_jersey = sorted(players.keys())
        print(
            "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
        option = input("Choose an option:\n")
    if option == "u":
        player_del = int(input("Enter a jersey number:"))
        player_new_rating = int(input("Enter a new rating for player:"))
        players[player_del] = player_new_rating
        print(
            "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
        option = input("Choose an option:\n")
    if option == "r":
        rating = int(input("Enter a rating:"))
        print(f'\nABOVE {rating}')
        for x in players_jersey:
            if players[x] > rating:
                print(f'Jersey number: {x}, Rating: {players[x]}')
        print(
            "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")
        option = input("Choose an option:\n")