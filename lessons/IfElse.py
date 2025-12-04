# Example of the if ... else ... statement, using two branches.
# This program evaluates whether a person is of driving age.
# ICS2O Unit 4, Activity 6

# Constants
DRIVING_AGE = 16

# Input
userAge = int(input("Please enter your age: "))

# processing and output
if userAge >= DRIVING_AGE:
    print("You can drive!")
    
else:
    print("You're too young to drive!")
