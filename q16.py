from collections import Counter

def character_frequency(text):
  """Counts the frequency of each character in a string."""
  char_count = Counter(text)
  for char, count in char_count.items():
    print(char, ":", count)

text = input("Enter a string: ")
character_frequency(text)