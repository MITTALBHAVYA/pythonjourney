def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_factorials(n):
    for i in range(1, n + 1):
        fact = factorial(i)
        print(f"The factorial of {i} is: {fact}")

n = int(input("Enter the value of n: "))
print(factorial(n))
