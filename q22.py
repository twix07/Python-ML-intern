def min_max_in_list(numbers):
  """Returns the minimum and maximum values in a list of numbers."""
  if not numbers:
    print("Error: List is empty.")
    return None, None
  minimum = max(numbers)  # Initialize with opposite extreme for comparison
  maximum = min(numbers)
  for num in numbers:
    if num < minimum:
      minimum = num
    if num > maximum:
      maximum = num
  return minimum, maximum

numbers = []
while True:
  try:
    num_items = int(input("Enter the number of elements in the list (or enter 'q' to quit): "))
    break  # Exit the loop if valid input is received
  except ValueError:
    print("Invalid input. Please enter a number or 'q' to quit.")

if num_items != 'q':  # Check if user entered 'q' to quit
  for i in range(num_items):
    number = float(input("Enter element"))
    numbers.append(number)
  min_value, max_value = min_max_in_list(numbers)
  if min_value is not None:
    print("The minimum value is:", min_value)
    print("The maximum value is:", max_value)
else:
  print("Exiting program.")

