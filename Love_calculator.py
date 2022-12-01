#request name of 2 people, check how much times the words t-r-u-e l-o-v-e appears. 
#give score according to: less than 10 or more than 90 :"Your score is **x**, you go together like coke and mentos."
#between 40 and 50- "Your score is **y**, you are alright together."
#Otherwise- "Your score is **z**."


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



#string that contains both names 
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e
#counting needed leeters 
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e
# 2 digit score 
score = int(str(first_digit) + str(second_digit))
#conditiones for the score 
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")