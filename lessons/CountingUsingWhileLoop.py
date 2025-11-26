# Counting using a conditional loop

# variables
num = 1
countTo = 0

# Program Title
print("This program will count up from 1 to any number.")

countTo = int(input("Please enter a number: "))

# evaluate the value of num against countTo
while num <= countTo:
    
    # output current num to screen
    print(num)
    
    # increase value of num by 1 on each repetition
    num = num + 1
    
# output to indicate end of program
print("Finished Counting")
    