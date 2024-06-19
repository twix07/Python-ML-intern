def copy_text_file(source_file, destination_file):
  """Copies the contents of one text file to another."""
  try:
    with open(source_file, "r") as source, open(destination_file, "w") as dest:
      content = source.read()
      dest.write(content)
    print("Successfully copied", source_file, "to", destination_file)
  except FileNotFoundError:
    print("Error: File not found. Please check file paths.")

source_filename = input("Enter the source text file name: ")
destination_filename = input("Enter the destination text file name: ")
copy_text_file(source_filename, destination_filename)
