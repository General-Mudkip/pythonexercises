import random

def removeListDupes(givenList): return list(set(givenList))
    #for i in list:
    #    if not i in newList:
    #        newList.append(i)
    # newList = [i for i in list if not i in newList]


print(removeListDupes([random.randint(1,15) for i in range(1,50)]))