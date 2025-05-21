## Calculator
##----------------
## Uncomment here the LCD Display
## and resources/init.py
## To enable Display

# Imports


# Funxtions
def add():
    num1 = input("num1:  ")
    num2 = input("num2:  ")
    return num1 + num2


def main():

    # Initalize LCD Display
    # lcd = resources.LCD(2, 0x27, True)

    # User Input
    menu = input("calc:\n1) Add  ")

    if menu == "1":
        print(add())
    elif menu == "2":
        print("nothing")
    elif menu == "3":
        print("nothing")
    else:
        print("invalid input")
    # Use Try / Catch while using file usage.

    # Output to LCD Display
    #    lcd.message(" record recorded")
    #    time.sleep(10)
    #    lcd.clear()

    # End of Line
    print("end of line")


# Main
if __name__ == "__main__":
    main()
