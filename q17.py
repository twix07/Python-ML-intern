def to_title_case(text):
  """Converts a given string to title case (first letter of each word capitalized)."""
  return text.title()

text = input("Enter a string: ")
title_text = to_title_case(text)
print("The string in title case is:", title_text)
