def fibonacci(n):
  """Generates the first n numbers in the Fibonacci sequence."""
  if n < 0:
    print("Invalid input: n must be non-negative.")
    return None
  elif n == 0:
    return []
  elif n == 1:
    return [0]
  else:
    fib_sequence = [0, 1]
    for i in range(2, n):
      next_num = fib_sequence[i-1] + fib_sequence[i-2]
      fib_sequence.append(next_num)
    return fib_sequence

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci_series = fibonacci(num_terms)
if fibonacci_series is not None:
  print("The first", num_terms, "Fibonacci numbers are:", fibonacci_series)
