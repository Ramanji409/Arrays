def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
n=6
print(factorial(n))

#Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=7
for i in range(n):
    print(fibonacci(i),end='')
