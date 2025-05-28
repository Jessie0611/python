# Temperature Converter celsius_to_fahrenheit() converts Celsius to Fahrenheit. fahrenheit_to_celsius() converts Fahrenheit to Celsius.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


# Let the user choose what to do
choice = input(
    "Type C to convert from Celsius to Fahrenheit, or F to convert from Fahrenheit to Celsius: ").upper()

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
else:
    print("Invalid choice.")
