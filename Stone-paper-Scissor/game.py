# stone, paper, scissors game
# 1 for stone
# 2 for paper
# 3 for scissors
import random

YouScore = 0
ComputerScore = 0

while(True):
    print("\n-------------------STONE PAPER SCISSORS-------------------\n")
    computer = random.randint(1,3)
    you = int(input("Enter your choice (1 for stone, 2 for paper, 3 for scissors):"))

    dict = {1:"stone",2:"paper",3:"scissors"}
    print(f"\nComputer chose {dict[computer]}")
    print(f"You chose {dict[you]}\n")

    if computer==you:
        print("It's a tie")
    
        
    else:
        if computer==1 and you==2:      #1-2=-1 .
            print("You win")        
        elif computer==1 and you==3:     #1-3=-2
            print("Computer wins")
        elif computer==2 and you==1:       #2-1=1
            print("Computer wins")
        elif computer==2 and you==3:       #2-3=-1  .
            print("You win")
        elif computer==3 and you==1:        #3-1=2   .
            print("You win")
        elif computer==3 and you==2:         #3-2=1
            print("Computer wins")
        else:
            print("Invalid choice")
    
    if(computer-you==1 or computer-you==-2):
        ComputerScore+=1
    elif(computer-you==-1 or computer-you==2):
        YouScore+=1
    else:
        pass
    
    print(f"\nComputer Score:{ComputerScore}")
    print(f"Your Score:{YouScore}")
        
    print("\n-----------------------------------------------------------\n")
    
    ch = input("Do you want to play again?(y/n):")
    if ch=='n':
        break
    else:
        pass
    
with open("Hi-score.txt") as f:
    hiScore = f.read()
    if hiScore=="":
        hiScore = 0
    else:
        hiScore = int(hiScore)
    
score = YouScore
if score>hiScore:
    with open("Hi-score.txt",'w') as f:
        f.write(str(score))
    print("Yah!! You break the score. It's HI-SCORE")
    print("Hi-score updated")
else:
    print("You did not break the Hi-score")