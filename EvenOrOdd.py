while True:
    num = input("Your Number:")
    if num == "kill":
        break
    if not num.isdecimal():
        print(f"{num} is not a valid integer!")
        continue
    if int(num) % 2 == 0:
        print("Your number is even!")
    else:
        print("Your number is odd!")
print("Killed")