"""
Program that gets the desired length of a password of a user
The password is error checked to make sure it is the right length
The length of the password is then used to print the same number of stars.
"""
def main():
    minimum_password_length = int(input("Enter minimum password length: "))
    password_length = get_password(minimum_password_length)
    method_name(password_length)


def print_asterisks\
                (password_length):
    for i in range(0, password_length):
        print("*", sep="", end="")


def get_password(minimum_password_length,):
    user_password = input("Input password: ")
    password_length = len(user_password)
    while password_length < minimum_password_length:
        print("invalid password")
        user_password = input("Input password: ")
        password_length = len(user_password)
    return password_length


main()

