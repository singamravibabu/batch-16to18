import sys

filename = input("Enter the file name: ")
try:
    with open(filename) as f:
        contents = f.read()
    value1 = int(input("Enter the an integer value: "))
    value2 = int(input("Enter the another integer value: "))
    result = value1 + value2
    print("Outcome:", result)
except ValueError:
    print("Please enter valid integer values.")
except FileNotFoundError as e:
    raise FileNotFoundError("The specified file was not found.")
except OSError:
    print("There was an error accessing the file.")
except Exception:
    print("Something went wrong.")
