"""tictactoe game for 2 players"""

choices = []
for x in range(1, 10):
    choices.append(x.__str__())

playerOneTurn = True
winner = False
counter = 0


def printBoard():
    print('\n -----')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print(' -----')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print(' -----')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print(' -----\n')


while not winner:
    printBoard()

    if playerOneTurn:
        print("Player 1:")
    else:
        print("Player 2:")

    try:
        choice = int(input(">> "))
        if choice > 9 or choice < 1:
            raise IndexError
    except IndexError:
        print("please enter a valid field")
        continue

    if choices[choice - 1] == 'X' or choices[choice - 1] == 'O':
        print("illegal move, please try again")
        continue

    if playerOneTurn:
        choices[choice - 1] = 'X'
        counter += 1
    else:
        choices[choice - 1] = 'O'
        counter += 1
    playerOneTurn = not playerOneTurn

    for x in range(0, 3):
        y = x * 3
        if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]:
            winner = True
            printBoard()
        if choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]:
            winner = True
            printBoard()

    if ((choices[0] == choices[4] and choices[0] == choices[8]) or
            (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printBoard()

    if counter == len(choices) and winner != True:
        printBoard()
        print('No winner')
        break
if winner:
    print("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
