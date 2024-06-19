def check_prefix_suffix(text, prefix, suffix):
  """Checks if a string starts with a given prefix or ends with a given suffix."""
  has_prefix = text.startswith(prefix)
  has_suffix = text.endswith(suffix)
  if has_prefix and has_suffix:
    print(text, "starts with", prefix, "and ends with", suffix)
  elif has_prefix:
    print(text, "starts with", prefix)
  elif has_suffix:
    print(text, "ends with", suffix)
  else:
    print(text, "does not start with", prefix, "or end with", suffix)

text = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
check_prefix_suffix(text, prefix, suffix)
