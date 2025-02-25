import random

print("\n********PERFECT GUESS*********\n")
Com_num =random.randint(0, 100)

Count = 0
while(True):
    Count += 1
    User_num = int(input("\nGuess the Number(bet 0 to 100):"))

    if (Com_num < User_num):
        print("Guess is wrong, Try again! Lower Number please!!")
    elif (Com_num >  User_num):
        print("Guess is wrong, Try again! Higher Number please!!")
    else:
        print(f"Yah!! you did Perfect in -{Count}- Guesses")
        break
