def convert_temperature(value, unit):
  """Converts temperature from Celsius to Fahrenheit and vice versa based on user input."""
  if unit.lower() == "c":
    fahrenheit = (value * 9/5) + 32
    return fahrenheit, "Fahrenheit"
  elif unit.lower() == "f":
    celsius = (value - 32) * 5/9
    return celsius, "Celsius"
  else:
    print("Error: Invalid unit. Please enter 'C' or 'F'.")
    return None, None

temp_value = float(input("Enter the temperature value: "))
temp_unit = input("Enter the unit (C or F): ")
converted_value, converted_unit = convert_temperature(temp_value, temp_unit)
if converted_value is not None:
  print(temp_value, temp_unit, "is equal to", converted_value, converted_unit)
