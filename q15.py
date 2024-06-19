import csv

def read_csv_file(filename):
  """Reads data from a CSV file and prints it to the console."""
  try:
    with open(filename, "r") as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        print(row)
  except FileNotFoundError:
    print("Error: File not found.")

file_name = input("Enter the name of the CSV file: ")
read_csv_file(file_name)
