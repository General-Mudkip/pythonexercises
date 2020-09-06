while True:
    dividend = int(int(input("Dividend: "))/2)
    divisorList = []
    for i in range(1, dividend):
        if i % 2 == 0:
            divisorList.append(i)

    print(divisorList)