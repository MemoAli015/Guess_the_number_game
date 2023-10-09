import random
count = 0 
number = random.randint(1,101)
#ALGORITM
while True:
    if count == 7:
        print("Game Over!")
        print(f"Number was: {number}")
        break 
    #We are starting here
    select = int(input("Guess: "))
    if select < number:
        print("-> UP <-")
    if select > number:
        print("-> DOWN <-")
    if select == number:
        print("YOU WON!")
        break
    if select > 100 or select < 0:
        print("You have to enter the number range of 0-100")

    count +=1
    print(f"Remaning health: {7 - count}")