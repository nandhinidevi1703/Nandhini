import random

Li1 = ["rock","paper","scissor"]
No_of_play =int(input("Number of games you wnat to play: "))
user_points = 0
system_points = 0
Tie = 0

for i in range(1, No_of_play+1):
    user_input = input("Give your input rock, psper, scissor :")
    system_input = random.choice(Li1)
    print(system_input)
    if user_input == system_input:
        Tie += 1
    elif user_input == "rock":
        if system_input == "paper":
            system_points += 1
        else:
            user_points += 1
    elif user_input == "paper":
        if system_input == "scissor":
            system_points += 1
        else:
            user_points += 1
    elif user_input == "scissor":
        if system_input == "rock":
            system_points += 1
        else:
            user_points += 1
    else:
        print("wrong input")

if user_points > system_points:
    print ("user wins")
elif user_points < system_points:
    print("system wins")
else:
    print("Tie")
    

'''print(random.choice(Li1))
print(random.choice(Li1))
print(random.choice(Li1))
print(random.choice(Li1))
print(random.choice(Li1))'''
