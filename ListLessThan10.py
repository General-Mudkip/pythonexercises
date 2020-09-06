numList = [1,6,1245,5,3,9,1234,754,234,75,1345,84,5452]
underTen = []
overTen = []

for i in numList:
    if i < 10:
        underTen.append(i)
    else:
        overTen.append(i)

print(f"Numbers over 10: {overTen}")
print(f"Numbers under 10: {underTen}")