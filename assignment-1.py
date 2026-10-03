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
ft_height = round(conv_height / 12, 2)
if is_student == True:
  print(f"hello, smartypants {name}! You are approximately {age} years old and you are {ft_height} feet tall.")
else:
  print(f"hello, {name}! You are approximately {age}  years old and you are {ft_height} feet tall.")
