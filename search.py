import sys
numbers = [3, 4, 2, 4, 5, 5, 6, 7, 7, 0]

if 0 in numbers:
    print("Found")
    sys.exit(0)
print("Not Found")
sys.exit(1)  # Sys is used to terminate a program continue
