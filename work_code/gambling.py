import random 

player1_balance = int(input("Player 1, enter your total amount: "))
player2_balance = int(input("Player 2, enter your total amount: "))


while player1_balance > 0 and player2_balance > 0:
    player1_bet = int(input("Player 1, enter your bet amount: "))
    player2_bet = int(input("Player 2, enter your bet amount: "))

    if player1_bet > player1_balance or player2_bet > player2_balance: 
        print("Bet amount exceeds your current balance. Please enter a valid bet.")
        continue

    player1_roll = random.randrange(1, 6) + random.randrange(1, 6) 
    player2_roll = random.randrange(1, 6) + random.randrange(1, 6) 

    print(f'Player 1 rolled: {player1_roll}')
    print(f'Player 2 rolled: {player2_roll}')

    if player1_roll > player2_roll: 
        player1_balance += player2_bet
        player2_balance -= player2_bet
        print("Player 1 wins this round") 

    elif player1_roll < player2_bet: 
        player2_balance += player1_bet 
        player1_balance -= player1_bet
        print("Player 2 wins this round")

    else :
        print("It's a tie! No one wins")

    print(f"Player 1 balanceL {player1_balance}")
    print(f"Player 2 balanceL {player2_balance}")

    continue_playing  = input('Do you want to continue playing? (yes/no):').lower() 
    if continue_playing != 'yes' & continue_playing != 'y': 
        break 

if player1_balance <= 0: 
    print("player 1 is out of money. Player 2 wins the game!")

elif player2_balance <= 0: 
    print("player 2 is out of money. Player 2 wins the game!")

else: 
    print("Game ended by players' choice.")
