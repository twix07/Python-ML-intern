def check_substring(text, substring):
  """Checks if a substring is present in a given string."""
  return substring in text

text = input("Enter a string: ")
substring_to_find = input("Enter the substring to check: ")
if check_substring(text, substring_to_find):
  print("The substring", substring_to_find, "is present in the text.")
else:
  print("The substring", substring_to_find, "is not present in the text.")
