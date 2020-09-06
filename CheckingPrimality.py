def get_integer(message = "Enter a number: "):
    try:
        return int(input(message))
    except:
        print("Encountered an error.")
        get_integer(message)

while True:
    dividend = int(get_integer())
    divisorList = []
    for i in range(1, dividend+1):
        if dividend % i == 0:
            divisorList.append(i)
    if len(divisorList) <= 2:
        print("This number is a Prime number.")
    else:
        print("This number is not a Prime number.")
    print(f"Numbers that can divide into {dividend}: {divisorList}")

    