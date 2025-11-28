# variables
TAX_RATE = 0.13
subtotal = 0

# output
print("Tax Calculation Program.")

# Input/Output - User prompt, with a sentinel (-1) to signal completion
price = float(input("Enter price (-1 to Exit): "))

# Input - continue to get prices until user tells us to stop
while price != -1: 
    
    subtotal = subtotal + price
    price = float(input("Enter price (-1 to Exit): "))
    
# Processing - calculation of tax, total and total including tax
tax = subtotal * TAX_RATE
total = subtotal + tax

# Output all calculations to user
print("Total Cost is: $", subtotal)
print("Tax is: $:", tax)
print("Cost with tax is: $", total)


