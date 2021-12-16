import random

dotted_line = "-" * 47

print(f"""Hi there!\n{dotted_line}\nI've generated a random 4 digit number for you.\nLet's play a "bulls and cows" game.\n{dotted_line}\nEnter a number:\n{dotted_line}""")

#generation of random 4-digit number (data type string)
generated_number = list()

while len(generated_number) < 4:
  if len(generated_number) == 0: #the first digit cannot be 0
    first_random_digit = str(random.randrange(1,10))
    generated_number.append(first_random_digit)
  else:
    random_digit = str(random.randrange(0,10))
    if random_digit in generated_number:
      random_digit = str(random.randrange(0,10))
    else:
      generated_number.append(random_digit)

generated_number = "".join(generated_number) #all digits put together as a string instead of list

#print(generated_number) #FOR TESTING PURPOSES ONLY

#---------------------------------------------------------------------------------------------------
number_from_user = "" #declaration of variable of number from the user. Keeping it blank so the while cycle is initiated.

count_of_tries = 0 #This variable is used to count the tries to inform the user how well he did at guessing at the end of the game.

#---------------------------------------------------------------------------------------------------
#verification cycle
while generated_number != number_from_user:
  number_from_user = input()
  count_of_tries += 1

  #user is asked to repeat the input until the format is correct and informs the user on the issue
  while number_from_user.isnumeric() == False or (number_from_user.isnumeric()== True and len(number_from_user) != 4) or number_from_user.count(number_from_user[0]) > 1 or number_from_user.count(number_from_user[1]) > 1 or  number_from_user.count(number_from_user[2]) > 1 or number_from_user.count(number_from_user[3]) > 1 or number_from_user[0] == "0":
    #verification if the input was provided correctly:
    if number_from_user.isnumeric() == False:
      print("The input is invalid as it contains invalid characters. It has to contain 4 digits.")
    elif number_from_user.isnumeric()== True and len(number_from_user) != 4:
      print("You entered too many or not enough digits. The input has to have 4 digits.")
    elif number_from_user.count(number_from_user[0]) > 1 or number_from_user.count(number_from_user[1]) > 1 or  number_from_user.count(number_from_user[2]) > 1 or number_from_user.count(number_from_user[3]) > 1:
      print("The digits in the input shall not repeat. Each digit must be unique.")
    elif number_from_user[0] == "0":
      print("The input cannot start with 0.")

    number_from_user = input()
  #hints to the user which digits are correct:
  bull = 0 # =>digit sits on the correct position
  cow = 0 # => digit appearing in the number but wrong position
  
  index = 0
  while index < 4:
    if number_from_user[index] == generated_number[index]:
      bull += 1 #
    index += 1

  index = 0
  while index < 4:
    if number_from_user[index] in generated_number:
      cow += 1
    index += 1
  
  #bull or bulls?
  if bull > 1:
    bull_name = "bulls"
  else:
    bull_name = "bull"

  cow = cow - bull #correction of the cow count due to the fact that the "cow" contains also the bulls

  #cow or cows?
  if cow > 1:
    cow_name = "cows"
  else:
    cow_name = "cow"
  
  print(f"{bull} {bull_name}, {cow} {cow_name}")
  print(dotted_line)

  

else:
  if count_of_tries == 1:
    level = "unbelievable"
  elif count_of_tries > 20:
    level = "not so good"
  elif count_of_tries > 8:
    level = "average"
  elif count_of_tries > 1:
    level = "amazing"
  
  if count_of_tries == 1:
    guess = "guess"
  else:
    guess = "guesses"
  print(f"Correct, you've guessed the right number\nin {count_of_tries} {guess}!")

print(dotted_line)
print(f"That's {level}.")