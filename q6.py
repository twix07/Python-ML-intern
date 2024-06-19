def read_from_file():
  """Reads the content of a text file and prints it to the console."""
  filename = "user_input.txt"  # Replace with your desired filename
  try:
    with open(filename, "r") as file:
      content = file.read()
      print("Content of", filename, ":\n", content)
  except FileNotFoundError:
    print("Error: File not found.")

read_from_file()
