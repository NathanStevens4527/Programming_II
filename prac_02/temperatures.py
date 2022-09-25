"""Program for converting temperatures with functions"""
def convert_to_fahrenheit(celsius):

    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))
    main()

def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))
    main()

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
            print(MENU)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print("Result: {:.2f} F".format(celsius))
            print(MENU)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()




