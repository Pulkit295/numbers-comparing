import random

computer=random.randint(1,100)
user= -1
guesses=0
while(user!=computer):
    guesses+=1

    user=int(input("Guess the number :"))
    if(user>computer):
        print("Lower number please")
        guesses+=1
    elif(user<computer):
        print("Higher number please")
        guesses+=1
print(f"You have guessed the number{computer} correctly in {guesses} attempts")

    