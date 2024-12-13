# example4.py
# This script demonstrates a simple division function

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print("Quotient:", divide_numbers(10, 2))
