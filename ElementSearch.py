import random

def element_search(inList,element):
    if element in inList:
        return True
    else:
        return False

theList = [random.randint(0,100) for i in range(100)]
theList.sort(reverse=False)
value = element_search(theList, random.randint(0,100))
print(value)