#Small Pizza: $15 , Medium Pizza: $20 ,Large Pizza: $25 . Pepperoni for Small Pizza: +$2,
#   Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Assume that all user inputs are correct, no validation needed 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


pizza_calc = 0

#checking size and defining initial price by size - this is the first input 
if size == "S":
  pizza_calc += 15
elif size == "M":
  pizza_calc += 20
else:
  pizza_calc += 25
#we have price by size 

#now checking pepperoni and adding to the price if needed- second input 
if add_pepperoni == "Y":
  if size == "S":
    pizza_calc += 2
  else:
    pizza_calc += 3
# price including size and pepperoni     
if extra_cheese == "Y":
  pizza_calc += 1

#we covered all the options for each input and difined final price that covers all options 
  
print(f"Your final price is: ${pizza_calc}.")







