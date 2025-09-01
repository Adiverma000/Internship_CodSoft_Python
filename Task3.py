class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            print("Error: Division by zero!")
            return None
def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    print("\nChoose Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number between 1 and 4.")
        return
    calc = Calculator(a, b)
    if choice == 1:
        print("Result:", calc.add())
    elif choice == 2:
        print("Result:", calc.subtract())
    elif choice == 3:
        print("Result:", calc.multiply())
    elif choice == 4:
        result = calc.divide()
        if result is not None:
            print("Result:", result)
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()
