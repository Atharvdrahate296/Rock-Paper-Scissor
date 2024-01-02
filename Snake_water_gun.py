#snake beats water , water beats gun and gun beats snake
import random
def game(comp,mine):                #game logic
    if(comp =='S' and mine == "G"):
        return True
    elif(comp =="W" and mine == "S"):
        return True
    elif(comp =="G" and mine == "W"):
        return True
    else:
        return False

choice=('S','W','G')        #random choice by computer
comp=random.randint(0,2)
comp=choice[comp]

mine=input("Choose either S(snake) , W(water) or G(gun) :")    #player input
print(f"You choose : {mine}")
print(f"Computer choose : {comp}")

if(mine != "S" and mine != "G" and mine != "W"):  #error management
    print("Incorrect choice.")
    exit()
elif(mine == comp ):
    print("Draw!!")
    exit()


win=game(comp,mine)             #passing both choices to evaluate
if(win):                        #if true:you win , else :lose
    print("You Won!")
else:
    print("You lose")
