import random
import time


def main():
    print("\nWelcome to the game browser!\n")
    time.sleep(1)
    print("Please choose one of the following games: \n")
    time.sleep(1)
    valid = 1
    while valid:
        print("1. Dice roller\n2. Guess the number\n3. Higher or lower\n4. Math game\n0. Quit")
        time.sleep(1)
        gamewanted = int(input("\nGame number: "))
        if gamewanted == 1:
            diceroller()
            valid = playagain()
        elif gamewanted == 2:
            guessthenumber()
            valid = playagain()
        elif gamewanted == 3:
            higherorlower()
            valid = playagain()
        elif gamewanted == 4:
            mathgame()
            valid = playagain()
        elif gamewanted == 0:
            time.sleep(0.5)
            print("\nThanks for playing!\n")
            break

def diceroller():
    print("\nWelcome to dice roller!")
    time.sleep(1)
    print("Get as close to 21 as possible without going over!\n")
    time.sleep(1)
    rollorhold = ""
    total = 0
    randroll = 0
    while 1:
        rollorhold = input("Would you like to roll or hold? ")
        if rollorhold == 'roll':
            randroll = random.randint(1,6)
            total += randroll
            if total > 21:
                time.sleep(1)
                print("Bust! You lose!")
                time.sleep(1)
                print("Total: " + str(total) + "\n")
                time.sleep(1)
                break
            elif total == 21:
                time.sleep(1)
                print("You win!")
                time.sleep(1)
                print("Total: " + str(total) + "\n")
                break
            else:
                time.sleep(0.5)
                print("Roll : " + str(randroll))
                time.sleep(0.5)
                print("Total: " + str(total) + "\n")
        elif rollorhold == 'hold':
            time.sleep(1)
            print("Safe choice!")
            time.sleep(1)
            print("Total: " + str(total) + "\n")
            break
        else:
            time.sleep(1)
            print("Invalid input, try again.")
            time.sleep(1)

def guessthenumber():
    time.sleep(1)
    print("\nWelcome to guess the number!\n")
    time.sleep(1)
    print("If you guess the number you win!\n")
    time.sleep(1)
    while 1:
        guess = int(input("Guess a number 1-10: "))
        randnum = random.randint(1,10)
        if guess == randnum:
            time.sleep(1)
            print("The number: " + str(randnum))
            time.sleep(1)
            print("You win!\n")
            break
        else:
            time.sleep(0.5)
            print("The number: " + str(randnum))
            time.sleep(0.5)
            print("You lose!\n")

def higherorlower():
    total = 0
    time.sleep(1)
    print("\nWelcome to higher or lower!\n")
    time.sleep(1)
    print("Guess whether the number 1-100 will be higher or lower!")
    while 1:
        randomnumber = random.randrange(1,100)
        if total == 0:
            time.sleep(1)
            print("\nThe number: ", randomnumber)
        else:
            randomnumber = secondrandomnumber
        time.sleep(1)
        guess = input("\nHigher or lower? ")
        if guess == 'higher':
            secondrandomnumber = random.randrange(1,100)
            if secondrandomnumber > randomnumber:
                time.sleep(1)
                print("\nCorrect! The number was: ", secondrandomnumber)
                total += 1
            elif secondrandomnumber < randomnumber:
                time.sleep(1)
                print("\nIncorrect! The number was: ", secondrandomnumber)
                break
            else:
                time.sleep(1)
                print("\nWow! The number was the same! The number was: ", secondrandomnumber)
        if guess == 'lower':
            secondrandomnumber = random.randrange(1,100)
            if secondrandomnumber < randomnumber:
                time.sleep(1)
                print("\nCorrect! The number was: ", secondrandomnumber)
                total += 1
            elif secondrandomnumber > randomnumber:
                time.sleep(1)
                print("\nIncorrect! The number was: ", secondrandomnumber)
                break
            else:
                time.sleep(1)
                print("\nWow! The number was the same! The number was: ", secondrandomnumber)
    time.sleep(1)
    print("\nYour score: ", total, "\n")

def mathgame():
    time.sleep(1)
    print("\nWelcome to the math game!")
    time.sleep(1)
    print("\nSolve the math equation!")
    roundscompleted = 0
    valid = 1
    time.sleep(1)
    print("\nLevel 1")
    while 1:
        time.sleep(1)
        firstrand = random.randrange(1,16)
        secondrand = random.randrange(1,16)
        addorsub = random.randrange(1,3)
        if addorsub == 1:
            print("\nSolve", firstrand, " + ", secondrand)
            answer = int(input("\nAnswer: "))
        else:
            print("\nSolve", firstrand, " - ", secondrand,": ")
            answer = int(input("\nAnswer: "))
        if addorsub == 1 and answer == (firstrand + secondrand):
            time.sleep(1)
            print("\nCorrect!")
            roundscompleted += 1
            if roundscompleted == 3:
                break
        elif addorsub == 2 and answer == (firstrand - secondrand):
            time.sleep(1)
            print("\nCorrect!")
            roundscompleted += 1
            if roundscompleted == 3:
                break
        else:
            time.sleep(1)
            print("\nIncorrect! Game over!")
            valid = 0
            break
    time.sleep(1)
    if valid:
        print("\nLevel 2")
        roundscompleted = 0
        while 1:
            time.sleep(1)
            firstrand = random.randrange(1,21)
            secondrand = random.randrange(1,21)
            print("\nSolve", firstrand, " * ", secondrand)
            answer = int(input("\nAnswer: "))
            if answer == (firstrand * secondrand):
                time.sleep(1)
                print("\nCorrect!")
                roundscompleted += 1
                if roundscompleted == 4:
                    break
            else:
                time.sleep(1)
                print("\nIncorrect! Game over!")
                valid = 0
                break   
        time.sleep(1) 
        if valid:
            print("\nLevel 3")
            roundscompleted = 0
            while 1:
                time.sleep(1)
                firstrand = random.randrange(1,21)
                secondrand = random.randrange(1,21)
                thirdrand = random.randrange(1,21)
                mixer = random.randrange(1,3)
                if mixer == 1:
                    print("\nSolve(", firstrand, " + ", secondrand, ") *", thirdrand)
                    answer = int(input("\nAnswer: "))
                    if answer == ((firstrand + secondrand)*thirdrand):
                        time.sleep(1)
                        print("\nCorrect!")
                        roundscompleted += 1
                        if roundscompleted == 5:
                            break
                    else:
                        time.sleep(1)
                        print("\nIncorrect! Game over!")
                        valid = 0
                        break
                else:
                    print("\nSolve(", firstrand, " * ", secondrand, ") +", thirdrand)
                    answer = int(input("\nAnswer: "))
                    if answer == ((firstrand * secondrand)+thirdrand):
                        time.sleep(1)
                        print("\nCorrect!")
                        roundscompleted += 1
                        if roundscompleted == 3:
                            break
                    else:
                        time.sleep(1)
                        print("\nIncorrect! Game over!")
                        valid = 0
                        break
            time.sleep(1) 
            
def playagain():
    time.sleep(1)
    x = input("\nWould you like to play again? \n")
    if x.lower() == 'yes':
        time.sleep(1)
        return 1
    else:
        time.sleep(0.5)
        print("\nThanks for playing!\n")
        return 0        

if __name__ == '__main__':
    main()