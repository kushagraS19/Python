import random

ran = random.randint(0,100)

while True:
    userChoice = int(input("Choose a number between 0 to 100 or Quit(-1) : "))
    if(userChoice == -1):
        break
    if(userChoice == ran):
        print("BOOYAH ! You choose the correct number.")
        break
    elif(userChoice > ran):
        print("Your number was bigger. Try again.")
    else:
        print("Your number was smaller. Try again")        

print("GAME OVER")    