def list_sum(numbers):
  """Takes a list of numbers and returns their sum."""
  total = 0
  for num in numbers:
    total += num
  return total

numbers = []
num_items = int(input("Enter the number of elements in the list: "))
for i in range(num_items):
  number = float(input("Enter element"))
  numbers.append(number)
list_total = list_sum(numbers)
print("The sum of the list elements is:", list_total)
