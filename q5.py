def write_to_file():
  """Takes a string input from the user and writes it to a text file."""
  filename = "user_input.txt"  # Replace with your desired filename
  text = input("Enter the text you want to write: ")
  with open(filename, "w") as file:
    file.write(text)
  print("Successfully written to", filename)

write_to_file()
