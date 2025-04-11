while True:

    try:

        num = int(input("Please input a number: "))

        print("Valid Input")

        break

    except ValueError:

        while True:

            try:

                num = int(input("Just Numbers are Allowed! Please try again: "))

                print("Valid Input")

                break

            except ValueError:

                continue

        break

