def factorial(num):
  """Calculates the factorial of a given number."""
  if num < 0:
    print("Factorial is not defined for negative numbers.")
    return None
  elif num == 0:
    return 1
  else:
    fact = 1
    for i in range(1, num + 1):
      fact *= i
    return fact

number = int(input("Enter a non-negative number: "))
factorial_result = factorial(number)
if factorial_result is not None:
  print("The factorial of", number, "is", factorial_result)
