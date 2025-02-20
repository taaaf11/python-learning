
while True:
    print("=== Welcome to a simple calculator ===")

    number_one = int(input("Enter first number: "))
    number_two = int(input("Enter second number: "))

    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo")

    choice = input("Enter your choice: ")

    if choice == "1":
        sum = number_one + number_two
        print(f"The sum of {number_one} and {number_two} is {sum}")
    elif choice == "2":
        sub = number_one - number_two
        print(f"The subtraction of {number_one} and {number_two} is {sub}")
    elif choice == "3":
        product = number_one * number_two
        print(f"The product of {number_one} and {number_two} is {product}")
    elif choice == "4":
        div = number_one % number_two
        print(f"The division of {number_one} and {number_two} is {div}")
    elif choice == "5":
        mod = number_one % number_two
        print(f"The modulo of {number_one} and {number_two} is {mod}")
    else:
        print("Invalid choice, Please enter a valid choice.")

    want_to_continue = input("Would you like to continue? (y/n): ")

    if want_to_continue == "y" or want_to_continue == "Y":
        continue
    else:
        break