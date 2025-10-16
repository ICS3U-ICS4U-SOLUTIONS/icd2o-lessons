# Program gets grade from user, then determines level

grade = int(input("Enter your grade: "))

# level 0
if (grade < 50):
    print("Level 0")
    
# level 1
elif (grade < 60):
    print("Level 1")

# level 2
elif (grade < 70):
    print("Level 2")
    
# level 3 
elif (grade < 80):
    print("Level 3")
    
# level 4
else:
    print("Level 4")