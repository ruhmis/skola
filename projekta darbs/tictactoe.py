# https://docs.google.com/document/d/1U9n7BtNwANyPHRlP9Jwn6oYncnyPYR2V8lIIYN-ej78/edit?usp=sharing
# https://docs.google.com/document/d/1Cz-u84URpiy417TUwpI00pXLKeB02WcDePsRlz6uXLI/edit?usp=sharing

# izveido laukumu
board = [" " for i in range(9)]

# funkcija, kas izdrukā laukumu
def print_board():
    print()
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            
            # ja tukšs, rāda numuru
            if board[index] == " ":
                print(index + 1, end="")
            else:
                print(board[index], end="")
            
            if j < 2:
                print(" | ", end="")
        print()
        
        if i < 2:
            print("--+---+--")
    print()

# funkcija uzvaras pārbaudei
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for pos in win_positions:
        if board[pos[0]] == player and board[pos[1]] == player and board[pos[2]] == player:
            return True
    return False

# spēle
current_player = "X"

for turn in range(9):
    print_board()
    
    move = int(input("Spēlētājs " + current_player + ", izvēlies (1-9): "))
    
    if board[move - 1] == " ":
        board[move - 1] = current_player
    else:
        print("Šī vieta jau aizņemta!")
        continue
    
    if check_winner(current_player):
        print_board()
        print("Spēlētājs", current_player, "uzvarēja!")
        break
    
    # maina spēlētāju
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

else:
    print_board()
    print("Neizšķirts!")