def main():
    times = input("How many times do you want to Meow? ")
    meow(times)
    print("You meowed, " + str(times) + " times")


def meow(n):
    for i in range(n):
        print("Meow")


main()
