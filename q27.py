def string_to_char_list(text):
  """Converts a string into a list of its characters."""
  char_list = list(text)
  return char_list

text = input("Enter a string: ")
character_list = string_to_char_list(text)
print("The list of characters:", character_list)

