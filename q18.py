from collections import Counter

def are_anagrams(str1, str2):
  """Checks if two strings are anagrams of each other."""
  char_count1 = Counter(str1.lower())
  char_count2 = Counter(str2.lower())
  return char_count1 == char_count2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams:
  print("string1 and string2 are anagrams of each other")
else:
  print("both strings are not anagrams of each other")

  

