a = int(input("Number: "))

def fib(a):
    if a in [1, 2]:
        return a-1
    return fib(a-1)+fib(a-2)

print (fib(a))