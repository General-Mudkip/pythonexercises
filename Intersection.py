import random
a = []
b = []
intersection = []

for aa in range(1,40):
    aa = random.randint(0,40)
    a.append(aa)
for bb in range(1,40):
    bb = random.randint(0,40)
    b.append(bb)

for i in a:
    if i in b:
        intersection.append(i)
print(f"Intersection: {intersection}")