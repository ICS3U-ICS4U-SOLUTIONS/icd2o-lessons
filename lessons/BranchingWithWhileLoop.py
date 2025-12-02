# Use the while loop to demonstrate branching
# Unit 4, Activity 6

# Generate random numbers: seed() ensure they are actually random
import random
random.seed()

# variables
userContinue = 'y'
userAnswer = 0

# Print program title
print("Addition Questions Program")

# While loop used to allow player to play as many times as they like
while userContinue == 'y' or userContinue == 'Y':

    # create numbers for addition question
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    while userAnswer != (num1 + num2):
        
        # user prompt
        print("Answer the addition question: ")
        print(num1, " + ", num2, " = ", end='')
    
        # get user answer
        userAnswer = int(input())

    userContinue = input("Continue? (y/n)")



