'''
Triple single or double quotes can be used for multi-line comments.

PROGRAM:  Program will find the range of marks in a class, which would be 
the difference between the lowest and the highest mark. The marks are not sorted, 
so the code must read through the entire list of marks, keeping track of which 
mark is the lowest and the highest. Assume all marks are in percents, between 0 and 100. 

PSEUDO-CODE:

declare a variable called highestMark, set to 0
declare a variable called lowestMark, set to 100
declare a variable called done, set to "N"
declare a variable called currentMark, to hold the mark the user enters
declare a variable called markRange, to hold the final output

while user is still entering marks

	prompt user for mark

	assign input to currentMark
	
	if currentMark is greater than highest mark, we have a new highest mark
		assign currentMark to highestMark
		
	if currentMark is less than lowest mark, we have a new lowest mark
		assign currentMark to lowestMark

	prompt user for Y or N to indicate if they are done entering marks
	assign user input to done
	back to start of loop

assign highestMark - lowestMark to markRange
output markRange to user


'''

# variables
highestMark = 0
lowestMark = 100
done = "N"
currentMark = 0
markRange = 0 

# Loop while user is still entering marks
while done == "N" or done =="n":
	
	# prompt user for mark
	print("Input a mark: ")
	
	# assign input to currentMark
	currentMark = int(input())

	# if currentMark is greater than highest mark, we have a new highest mark
	# 	assign currentMark to highestMark
	if currentMark > highestMark:
		highestMark = currentMark
		
	# if currentMark is less than lowest mark, we have a new lowest mark
	#	assign currentMark to lowestMark
	if currentMark < lowestMark:
		lowestMark = currentMark
	
	# prompt user for Y or N to indicate if they are done entering marks
	# assign user input to done
	print("Done entering marks? Y or N: ")
	done = input()
	
# assign highestMark - lowestMark to markRange
markRange = highestMark - lowestMark

# output markRange to user
print("Difference in marks is ", markRange)

