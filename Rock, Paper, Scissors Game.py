import random, datetime

userScore = 0
comScore = 0
name = " "

def saveFile():
    with open (r"C:\Users\TRAIN 15\Desktop\RPS_Score.txt","a") as f:
        todayDate = datetime.datetime.today()
        f.write(todayDate.strftime("%d-%b-%Y   %H:%M:%S\n"))
        f.write(f"{name}'s Score: {userScore} \nComputer's score: {comScore}\n\n")

def score(comChoice, userChoice):
    global userScore, comScore
    if comChoice == userChoice:
        print("*"*30,"\nIt's a draw!?\n","*"*30)
        return 0
    elif comChoice == 'Rock' and userChoice == 'Scissors' or comChoice == 'Paper' and userChoice == 'Rock' or comChoice == 'Scissors' and userChoice == 'Paper':
        comScore += 1
        print("*"*30,"You Losed!","*"*30)
        return comScore
    elif userChoice == 'Rock' and comChoice == 'Scissors' or userChoice == 'Paper' and comChoice == 'Rock' or userChoice == 'Scissors' and comChoice == 'Paper':
        userScore += 1
        print("*"*30,"You Won!","*"*30)
        return userChoice

def computerChoice(choice):
    comChoice = random.choice(choice)
    return comChoice

def menu():
    print('-'*30,'\nChoose one of the following:\n', '1: ROCK\n','2: PAPER\n','3: SCISSORS','-'*30)

def main():
    global name
    print("-"*30,"\nWelcome to 'Play RPS'\n","-"*30)
    name = input("Please input your name: ")
    while True:
        count = 0
        while count < 3:
            menu()
            userChoice = int(input("Your choice? "))
            choice = ["Rock", "Paper", "Scissors"]
            computer = computerChoice(choice)
            userChoice -= 1
            user = choice[userChoice]
            print(f'Computer: {computer} \n{name}: {user}')
            score(computer,user)
            print(f"Computer's Score: {comScore} \n{name}'s Score: {userScore}")
            count += 1
        playAgain = input('Would you like to play again?(Y/N) ')
        if playAgain.upper() == "N":
            saveFile()
            print(f"\n\nThank you playing {name} & Goodbye...")
            break

main()