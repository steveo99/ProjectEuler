# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

# create a generator expression for Fibonacci numbers
def fibonacciGenerator(): 
    a: int = 0
    b: int = 1
    while(True):
        yield b
        a, b= b, a+b

obj = fibonacciGenerator()
sum: int = 0
n: int = next(obj)
while n < 4000000:
    if n % 2 == 0:
        sum += n
    n = next(obj)

print(sum)

