# IfElifElse.py
# Example of the if ... elif ... else ... statement,
# using 3 branches.
# This program evaluates if a person is of driving age
# or needs a retest.  Seniors over 80 require a retest.

# Variables
DRIVING_AGE = 16
RETEST_AGE = 80

# Input
userAge = int(input("Please enter your age: "))

# Processing and Output
if userAge >= DRIVING_AGE and userAge < RETEST_AGE:
    print("You can drive!")  # old enough to drive, not senior
    
elif userAge >= RETEST_AGE:
    print("You will need a retest in order to drive.")
    # senior and needs retest for safety reasons

else:
    print("You are too young to drive!")
    # user's age must be less than driving age
    
    