while True:
    pauser = input("")
    import random
    print([i for i in [random.randint(1,40) for i in range(1,40)] if i % 2 == 0])