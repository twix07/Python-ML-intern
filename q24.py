def calculate(num1, operator, num2):
  """Performs basic arithmetic operations based on user input."""
  if operator in "+-*/":
    if operator == "+":
      result = num1 + num2
    elif operator == "-":
      result = num1 - num2
    elif operator == "*":
      result = num1 * num2
    else:  # operator == "/"
      if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
      else:
        result = num1 / num2
    print(num1, operator, num2, "=", result)
  else:
    print("Error: Invalid operator. Please enter +, -, *, or /.")

while True:
  try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    calculate(num1, operator, num2)
    break  # Exit the loop after a valid calculation
  except ValueError:
    print("Invalid input. Please enter numbers and a valid operator.")
