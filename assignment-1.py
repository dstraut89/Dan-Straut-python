# Section 1

name = "Student"
age = 40
height = "5.11"
is_student = True

# Section 2

name = input("Please enter your name: ")
is_student = bool(input("Are you a student?(True or False): "))
year_current = input("What year is it?: ")
conv_year = int(year_current)
Year_of_birth = input("Please enter the year you were born: ")
conv_age = int(Year_of_birth)
age = conv_year - conv_age
height = input("how tall are you (in inches): ")
conv_height = int(height)
ft_height = int(conv_height / 12)
inch_height = round(conv_height % 12)
if is_student == True:
  print(f"Hello, smartypants {name}! You are approximately {age} years old and you are {ft_height} feet and {inch_height} inches tall.")
else:
  print(f"Hello, {name}! You are approximately {age}  years old and you are {ft_height} feet and {inch_height} inches tall.")

# Section 3

num1 = input("What is your first favorite number (Whole number: 4)?: ")
num2 = input("What is your second favorite number (Decimal number: 12.3)?: ")
num3 = input("What is your third favorit number (Any number: 1.2, 5, 3.75)?: ")

flt_num1 = float(num1)
flt_num2 = float(num2)
flt_num3 = float(num3)

if flt_num1 + flt_num2 == flt_num3:
  print(f"Wow, Your first two favorite numbers {flt_num1} and {flt_num2} add up to your third favorite number {flt_num3}")
else:
  print(f"Interesting, Your third favorite number {flt_num3} is not the sum of your first two favorite numbers {flt_num1} and {flt_num2}")

# Section 4

Item = "Python Textbook"
pytxtbk = 25.99
quantity = 1

fun = bool(input("Are you ready to have some fun with Python(True or False)? "))
if fun == True:
  textbook = bool(input("Would you like to buy a textbook to help you along the way(True or False)? "))
  if textbook == True:
    quantity = input("Great, each book is $25.99. How many would you want?: ")
  else:
    print("Ok, well just let me know if you change your mind.")
else:
  print("I am sorry to hear that, I wonder what I can do to encourage you to desire fun because this is going to be one hell of a ride.")  

total = pytxtbk * float(quantity)

if fun == True & textbook == True:
  print("||===========================||")
  print("          Receipt              ")
  print("||===========================||")
  print(f"  Item:      {Item}   ")
  print(f"  Price:              ${pytxtbk}")
  print(f"  Quantity:            {quantity}")
  print("-------------------------------")
  print(f"  Total:              ${total}")
  print("||===========================||")
else: 
  print("Unfortunately, you didn't ask for your textbook today.")
