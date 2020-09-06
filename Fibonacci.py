def fibonacci(repeatIters):
    fibonacciNums = [1]
    for i in range(repeatIters - 1):
        newNum = fibonacciNums[i] + fibonacciNums[i-1]
        fibonacciNums.append(newNum)
    return fibonacciNums
while True:
    print(fibonacci(int(input("Number of fibonacci numbers:"))))