#code contributed by Sumit
import random 
import math
name = input("Enter Your Name : ")
lsb = int(input("Enter the lower limit : "))
msb = int(input("Enter the higher limit : "))
randnumber = random.randint(lsb,msb)
total_try = round(math.log(msb - lsb + 1 , 2))
curr_try =  0
userGuess = None

print(f"Hello {name}  play the game by guessing the number between {lsb} and {msb} inclusive range.")
print(f"You have total  {total_try} guesses.")

while(curr_try < total_try):
    userGuess = int(input(f"{name} Enter your Guess : "))
    curr_try+=1;

    if userGuess==randnumber :
        print(f"Congratulation {name}!, you guessed the exact number. ")
        print(f"You guessed it in just {curr_try} guesses. ")
        break
    else : 
        if userGuess > randnumber : # when choosing higher number 
            print(f"Sorry, {name},you guessed it wrong! Enter a lower number")
            print(f"You have used {curr_try} guesses. Now you have only {total_try - curr_try} guesses left. ")

        else :
            print(f"Sorry, {name},you guessed it wrong! Enter a higher number") #when choosing lower number
            print(f"You have used {curr_try} guesses. Now you have only {total_try - curr_try} guesses left. ")

        if  userGuess != randnumber and curr_try == total_try : 
            print(f"Oops ! {name}, you counldn't guess the number correctly in {curr_try} guesses. ")
            print(f"It was {randnumber}.")
            print("Don't be sad, Better luck next time.")
