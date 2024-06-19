from datetime import date

def calculate_age():
  """Asks the user for their birth year and calculates their age."""
  current_year = date.today().year
  birth_year = int(input("Enter your birth year: "))
  age = current_year - birth_year
  print("Your age is", age)

calculate_age()
