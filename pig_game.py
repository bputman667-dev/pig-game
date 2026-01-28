import random
global player_score
global computer_score
global roll_total
global current_turn
player_score = 0
computer_score = 0
roll_total = 0
current_turn = "player"


#this, if it's a player, rolls it and queries if it's above 1 after adding the roll to the total
#if it's not above one, it sets roll_total to 0 and holds
def roll():
    global current_turn
    global roll_total
    roll_value = 0
    if(current_turn=="player"):
        roll_value = random.randint(1, 6)
        if(roll_value==1):
            roll_total = 0
            print("you got 1, turn over")
            hold("player")
        else:
            roll_total = roll_total + roll_value
            print("roll_total: " + str(roll_total))
            query()
    elif(current_turn=="computer"):
        while(roll_total < 20 and roll_value != 1):
            roll_value = random.randint(1, 6)
            if(roll_value==1):
                roll_total = 0
                hold("computer")
                print("the computer rolled a one, turn over")
            else:
                print("the computer's roll is " + str(roll_value))
                roll_total = roll_total + roll_value
                print("it's roll total now is " + str(roll_total))
        if(roll_total > 1):
            hold("computer")
            print("the computer holds")

#asks the player what to do
def query():
    choice = input("do you want to hold or roll? to hold, type 1, to roll, type 2: ")
    if(choice=="1"):
        hold("player")
    elif(choice=="2"):
        roll()
    else:
        print("not a choice")
        query()

#this just increases score and swaps turns when holding
def hold(turn):
    global player_score
    global computer_score
    global current_turn
    global roll_total
    if(turn=="player"):
        player_score = player_score + roll_total
        current_turn = "computer"
        roll_total = 0
    elif(turn=="computer"):
        current_turn = "player"
        computer_score = computer_score + roll_total
        current_turn = "player"
        roll_total = 0


#This just checks to see if one of the players has won yet
while(player_score < 100 and computer_score < 100):
    if(current_turn == "player"):
        query()
        print("player turn")
        print("player")
        print(player_score)
        print("computer")
        print(computer_score)
    elif(current_turn == "computer"):
        print("------------------------------------------")
        roll()
        print("computer turn")
        print("player")
        print(player_score)
        print("computer")
        print(computer_score)

#this determines the winner
if(player_score >= 100):
    print("player wins")
elif(computer_score >= 100):
    print("computer wins")