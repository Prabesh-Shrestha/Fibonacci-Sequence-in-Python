userval = int(input("How much do you wana print:  "))

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

for i in range(userval):
    print(fib(i))



    