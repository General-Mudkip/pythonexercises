import datetime

# Introductory text
print("What year will you be 100 in?")

# Gets basic details
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
printNo = int(input("How many times do you want it to print: "))

# Calculation that figures out when they will turn 100, using datetime to get the current year.
year = 100 - age + datetime.datetime.now().year

# Prints the info

for i in range(printNo):
    print(f"{name}, You will turn 100 in the year {year}. Loop {i}")