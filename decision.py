s = input("Do you agree? ")

lower = s.lower()

if lower == 'y':
    print("Agreed.")
elif lower == 'n':
    print("Disagreed.")
else:
    print("Neither agreed nor Disagreed")
