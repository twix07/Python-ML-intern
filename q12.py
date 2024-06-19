def sum_of_digits(number):
  """Calculates the sum of the digits of a given number."""
  if number < 0:
    number *= -1  # Handle negative numbers
  sum = 0
  while number > 0:
    digit = number % 10
    sum += digit
    number //= 10  # Integer division to remove last digit
  return sum

num = int(input("Enter a number: "))
digit_sum = sum_of_digits(num)
print("The sum of the digits of", num, "is", digit_sum)
