# Section 1

name = "Daniel"
age = 37
height = 5.11
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print("   ")

# Section 2

name = input("Please enter your name: ")
print("   ")
is_student = bool(input("Are you a student?(True or False): "))
print("   ")
year_current = input("What year is it?: ")
print("   ")
conv_year = int(year_current)
Year_of_birth = input("Please enter the year you were born: ")
print("   ")
conv_age = int(Year_of_birth)
age = conv_year - conv_age
height = input("how tall are you (in inches): ")
print("   ")
conv_height = int(height)
ft_height = int(conv_height / 12)
inch_height = round(conv_height % 12)
if is_student == True:
  print(f"Hello, smartypants {name}! You are approximately {age} years old and you are {ft_height} feet and {inch_height} inches tall.")
  print("   ")
else:
  print(f"Hello, {name}! You are approximately {age}  years old and you are {ft_height} feet and {inch_height} inches tall.")
  print("   ")

# Section 3

num1 = input("What is your first favorite number (Whole number: 4)?: ")
num2 = input("What is your second favorite number (Decimal number: 12.3)?: ")
print("   ")

flt_num1 = float(num1)
flt_num2 = float(num2)

num3 = flt_num1 * flt_num2

print(f"{num3} = {flt_num1} x {flt_num2} = {flt_num1 * flt_num2}")
print("   ")

# Section 4

item = "Python Textbook"
price = 25.99
quantity = 2
total = price * float(quantity)

if is_student == True:
  print("||===========================||")
  print("          Receipt              ")
  print("||===========================||")
  print(f"  Item:      {Item}   ")
  print(f"  Price:              ${pytxtbk}")
  print(f"  Quantity:            {quantity}")
  print("-------------------------------")
  print(f"  Total:              ${total}")
  print("||===========================||")
  print("   ")
else: 
  print("Unfortunately, you aren't registered for classes.")
  print("   ")

# Section 5

name = name
lname = input("What is your last name?: ")
print("   ")
hstate = input("What is your homestate? (2 Letter Initials. Example:CT, MA, FL...): ")
print("   ")
htown = input("What is your hometown?: ")
print("   ")
funfact = input("What is one fun fact about you?: ")
print("   ")
hobby = input("What is your go to hobby?: ")
print("   ")
age1 = age

print("||==========================||")
print(f"    PROFILE: {fname} {lname}   ")
print("||==========================||")
print(f"    Hometown: {htown}, {hstate} ")
print(f"    Hobby:   {hobby}  ")
print(f"    Fun fact: {funfact} ")
print(f"    Age: {age1}")
print("||==========================||")
print("   ")
print("   ")
