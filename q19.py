def remove_punctuation(text):
  """Removes all punctuation from a given string."""
  punctuation = "!\"#$%&()*+, -./:;<=>?@[\]^_`{|}~"
  no_punct = ""
  for char in text:
    if char not in punctuation:
      no_punct += char
  return no_punct

text = input("Enter a string: ")
text_without_punct = remove_punctuation(text)
print("The string without punctuation:", text_without_punct)
