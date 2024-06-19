def read_multiple_lines():
  """Reads multiple lines of input from the user until an empty line, then prints all the lines."""
  lines = []
  while True:
    line = input("Enter a line (or press Enter to finish): ")
    if not line:
      break
    lines.append(line)
  if lines:
    print("The entered lines are:")
    for line in lines:
      print(line)
  else:
    print("No lines were entered.")

read_multiple_lines()
