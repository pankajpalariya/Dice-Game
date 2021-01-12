import random

def dice_roll():
    diceroll = random.randint(1, 6)
    return diceroll

total_players = 0
while(total_players < 2):
 total_players = int(input("Enter the total number of players :\n"))
 if(total_players < 2):
    print(f"can not play with {total_players} player")

player_names = []

for player in range(total_players):
    name = str(input(f"enter the player {player+1} name :\n"))
    player_names.append(name)

total_rounds = int(input("Enter How many rounds you want to play :\n"))
print()

totalS = [0 for i in range(total_players)]

for round_number in range(1, total_rounds + 1):
    print(f"This is round number {round_number}\n")

    crs = [0 for i in range(total_players)]
    
    for player in range(total_players):
        cp_name = player_names[player]
        diceR = dice_roll()
        print(f"Player#{player+1}: {cp_name} got {diceR}")
        crs[player] += diceR
    print(f"round {round_number} has ended")
    totalS = [totalS[i] + crs[i] for i in range (total_players)]
    print(f"Score after round : {round_number} ", totalS)
    print("="*40)

print("total Scores : ", totalS)
max_score = max(totalS)
winner = []
for i in range(total_players):
    if(totalS[i]== max_score):
        winner.append(i)
print("Winner is : " + ", ".join([" player number "+str(i+1)+ " #" +player_names[i] for i in winner]))
