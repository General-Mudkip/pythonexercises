def EndPoints(list):
    print(list)
    firstVal = list[0]
    lastVal = list[len(list)-1]
    return firstVal, lastVal
print(EndPoints([i for i in range(0,40)]))
