# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# sum = x + y

# print(f"Sum is {sum}")

try:
    x = int(input("Enter x: "))
except ValueError:
    print("This is not a number")

try:
    y = int(input("Enter y: "))
except ValueError:
    print("This is not a number")

sum = x + y

print(f"Sum is {sum}")
