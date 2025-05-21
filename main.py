## Calculator
##----------------
## Uncomment here the LCD Display
## and resources/init.py
## To enable Display

# Imports


# Funxtions
def add(a: float, b: float):
    return a + b


def subtract(a: float, b: float):
    return a - b


def multiply(a: float, b: float):
    return a * b


def divide(a: float, b: float):
    return a / b


def main():

    # Initalize LCD Display
    # lcd = resources.LCD(2, 0x27, True)

    # User Input
    # Pico: Replace input with Button Routine
    menu = input("calc:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n  ")

    if menu == "1":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(add(a, b))
    elif menu == "2":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(subtract(a, b))
    elif menu == "3":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(multiply(a, b))
    elif menu == "4":
        a = float(input("num1: "))
        b = float(input("num2: "))
        print(divide(a, b))
    else:
        print("invalid input")

    # Output to LCD Display
    #    lcd.message("calculation completed")
    #    time.sleep(10)
    #    lcd.clear()

    # End of Line
    print("end of line")


# Main
if __name__ == "__main__":
    main()
