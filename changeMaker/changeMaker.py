# Get price of item
price = input("Price of the item ")
# Convert price to float
price = float(price)

# Get cash tendered
cash = input("Cash tendered ")
# Convert cash to float
cash = float(cash)

# Convert price to pennies
price *= 100
# Convert cash to pennies
cash *= 100

# Convert price to int
price = int(price)
# Convert cash to int
cash = int(cash)

# Make change from cash - price
change = cash - price
# Define dollars as change * 100
dollars = change/100
# Print change in dollars
print("Change: ${}".format(dollars))

# Calculate how many twenties go into the change
twenties = change // 2000
# subtract this from the change
change -= (twenties*2000)
# Print twenties
print("Twenties: {}".format(twenties))

# Calculate how many tens go into the change
tens = change // 1000
# subtract this from the change
change -= (tens*1000)
# Print tens
print("Tens: {}".format(tens))

# Calculate how many fives go into the change
fives = change // 500
# subtract this from the change
change -= (fives*500)
# Print fives
print("Fives: {}".format(fives))

# Calculate how many ones go into the change
ones = change // 100
# subtract this from the change
change -= (ones*100)
# Print ones
print("Ones: {}".format(ones))

# Calculate how many quarters go into the change
quarters = change // 50
# subtract this from the change
change -= (quarters*50)
# Print quarters
print("Quarters: {}".format(quarters))

# Calculate how many Dimes go into the change
dimes = change // 10
# subtract this from the change
change -= (dimes*10)
# Print dimes
print("Dimes: {}".format(dimes))

# Calculate how many Nickels go into the change
nickels = change // 5
# subtract this from the change
change -= (nickels*5)
# Print nickels
print("Nickels: {}".format(nickels))

# Calculate how many pennies go into the change
pennies = change
# subtract this from the change
change -= ones
# Print pennies
print("Pennies: {}".format(pennies))
