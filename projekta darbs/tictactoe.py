# https://docs.google.com/document/d/1U9n7BtNwANyPHRlP9Jwn6oYncnyPYR2V8lIIYN-ej78/edit?usp=sharing
# https://docs.google.com/document/d/1Cz-u84URpiy417TUwpI00pXLKeB02WcDePsRlz6uXLI/edit?usp=sharing

# izveido laukumu
laukums = [" " for i in range(9)]

# funkcija, kas izdrukā laukumu
def print_laukums():
    print()
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            
            # ja tukšs, rāda numuru
            if laukums[index] == " ":
                print(index + 1, end="")
            else:
                print(laukums[index], end="")
            
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
        if laukums[pos[0]] == player and laukums[pos[1]] == player and laukums[pos[2]] == player:
            return True
    return False

# spēle
pasreiz_spele = "X"

for turn in range(9):
    print_laukums()
    
    move = int(input("Spēlētājs " + pasreiz_spele + ", izvēlies (1-9): "))
    
    if laukums[move - 1] == " ":
        laukums[move - 1] = pasreiz_spele
    else:
        print("Šī vieta jau aizņemta!")
        continue
    
    if check_winner(pasreiz_spele):
        print_laukums()
        print("Spēlētājs", pasreiz_spele, "uzvarēja!")
        break
    
    # maina spēlētāju
    if pasreiz_spele == "X":
        pasreiz_spele = "O"
    else:
        pasreiz_spele = "X"

else:
    print_laukums()
    print("Neizšķirts!")