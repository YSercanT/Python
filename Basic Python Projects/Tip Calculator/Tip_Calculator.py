print("Welcome to the tip calculator.")
total_bill=int(input("What was the total bill? $"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people=int(input("How many people to split the bill? "))
total=(total_bill+ ((total_bill/100)*tip_percentage))/people
total = "{:.2f}".format(total)
print("Each person should pay : $" + str(total))
