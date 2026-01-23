import sys

# ... keep your add, subtract, etc. functions the same ...

def calculator():
    # Jenkins will pass these values as arguments
    if len(sys.argv) < 4:
        print("Usage: python calculator.py <choice> <num1> <num2>")
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