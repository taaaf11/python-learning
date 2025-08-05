def get_conversion_type():
    CONVERSION_TYPE_PROMPT = """What do you want to convert?
1. Celcius to Fahrenheit
2. Fahrenheit to Celcius
>>> """

    while True:
        try:
            value = int(input(CONVERSION_TYPE_PROMPT))

        # user entered a non-integer value
        except ValueError:
            continue

        # exception did not occur i.e. user entered an integer
        else:
            # reprompt if the user entered invalid conversion type
            if value not in [1, 2]:
                print("Invalid conversion type.\n")
                continue

            return value


def get_temperature():
    while True:
        try:
            value = float(input("Enter the temperature? "))

        # user entered a non-decimal value
        except ValueError:
            continue

        # exception did not occur i.e. user entered a decimal value
        else:
            return value


# converts celcius to fahrenheit
def convert_c_to_f(value):
    return value * 9 / 5 + 32


# Converts fahrenheit to celcius
def convert_f_to_c(value):
    return (value - 32) * 5 / 9


def main():
    conversion_type = get_conversion_type()
    value = get_temperature()

    # User wants to convert fahrenheit to celcius
    celcius_to_fahrenheit = conversion_type == 1

    if celcius_to_fahrenheit:
        converted = convert_c_to_f(value)
        print(f"Temperature in Fahrenheits: {converted:.2f}")
    else:
        converted = convert_f_to_c(value)
        print(f"Temperature in Celcius: {converted:.2f}")


if __name__ == "__main__":
    main()
