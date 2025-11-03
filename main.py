import random; import time

#variables
playing = True
roundcount = 0

#welcome message
print("Welcome to the Number Guessing Game!")
time.sleep(1.5)
print("Here's how this will work.")
time.sleep(1.5)
print("You will have 5 guesses.")
time.sleep(1.5)
print("The number will be between 1 and 50 inclusive and is randomly generated every time you restart the game.")
time.sleep(3)
print("Please ensure you only enter a number, or the program will crash. ")
time.sleep(2)
print("Have fun!")
time.sleep(2)

#main gameplay loop
while True:

    #reseting variables
    randomNumber = random.randint(1, 50)
    roundcount = 0
    playing = True

    #round 1-5 loop
    while playing:
        if roundcount < 5:
            guess = int(input("Take your guess: "))
            if guess == randomNumber:
                print("Correct!")
                playagain = input("Would you like to play again?").lower()
                if playagain == "yes":
                    playing = False
                elif playagain == "no":
                    print("Thanks for playing, goodbye!")
                    exit()
            elif guess != randomNumber:
                roundcount += 1
                if roundcount == 5:
                    print("You have reached the maximum number of guesses.")
                    playagain = input("Would you like to play again?").lower()
                    if playagain == "yes":
                        playing = False
                    elif playagain == "no":
                        print("Thanks for playing, goodbye!")
                        exit()
                else:
                    print("Wrong! Try again!")

