import sys

# 1. Define all functions FIRST
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Error! Division by zero."
    return x / y
def modulus(x, y):
    if y == 0: return "Error! Division by zero."
    return x % y

# 2. The main logic
def calculator():
    if len(sys.argv) < 4:
        print("Usage: python proj1.py <choice> <num1> <num2>")
        return

    choice = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {modulus(num1, num2)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    calculator()