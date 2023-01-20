
while True:
    try:
        height = int(input("Height: "))
        if (height > 0):
            break
        for i in range(height):
            print("#")
    except ValueError:
        print("This is not an integer!, Please enter an interger")
