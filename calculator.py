# CODSOFT Python Programming Internship
# Task 2 - Calculator

def calculator():
    print("==============================")
    print("       CALCULATOR")
    print("==============================")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect an operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")

        operation = input("\nEnter operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                print("❌ Cannot divide by zero.")
                return
            result = num1 / num2

        else:
            print("❌ Invalid operation.")
            return

        print("\n------------------------------")
        print(f"Result: {result}")
        print("------------------------------")

    except ValueError:
        print("❌ Please enter valid numbers.")


calculator()