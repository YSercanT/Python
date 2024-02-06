print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ") 
add_pepperoni = input("Do you want pepperoni? Y or N:") 
extra_cheese = input("Do you want extra cheese? Y or N:")  
total=0
if(size=="S" or size=="s"):
  total+=15
  if(add_pepperoni=="Y"):
    total+=2
  if(extra_cheese=="Y"):
    total+=1
else:
  if(add_pepperoni=="Y" or add_pepperoni=="y"):
    total+=3
  if(extra_cheese=="Y" or extra_cheese=="y"):
    total+=1
  if(size=="M" or size=="m"):
    total+=20
  elif(size=="L" or size=="l"):
    total+=25
print("Your final bill is: ${}.".format(total))