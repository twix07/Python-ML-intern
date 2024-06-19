def count_element(element, list1):
  """Counts the occurrences of a specific element in a list."""
  count = 0
  for item in list1:
    if item == element:
      count += 1
  return count

list1 = []
num_items = int(input("Enter the number of elements in the list: "))
for i in range(num_items):
  number = int(input("Enter element"))
  list1.append(number)
element_to_find = int(input("Enter the element to count: "))
element_count = count_element(element_to_find, list1)
print("The element", element_to_find, "appears", element_count, "times in the list.")
