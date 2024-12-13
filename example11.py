# example11.py
# This script demonstrates a simple factorial function using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
