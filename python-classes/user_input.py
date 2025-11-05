try:
    value1 = int(input("Enter the an integer value: "))
    value2 = int(input("Enter the another integer value: "))
    result = value1 + value2
    print("Outcome:", result)
except Exception:
    print("Probably, you did not enter integer values.")