import random

Random_Num=int(random.randint (1,100))
Trails=10
User_trails =0

while User_trails <= Trails:
    User_trails += 1
    if User_trails > Trails:
        print("You lost the game.No available trials. ")
        break

    User_Num = int(input("Guess a Number between 1 and 100 : "))
    if int(Random_Num)==User_Num:
        print("Yay,Congrats.You have guessed the number {0} correctly in your {1} trial!!".format(Random_Num,User_trails))
        break

    elif int(User_Num) < Random_Num:
        print("Sorry,guess again.Too low.")

    elif int(User_Num) > Random_Num:
        print("Sorry,guess again.Too High.")







