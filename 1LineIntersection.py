import random
print([i for i in [random.randint(1,50) for y in range(1,40)] if i in [random.randint(1,50) for x in range(1,40)]])