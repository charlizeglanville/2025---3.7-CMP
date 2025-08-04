import re


# Used to validate clients name
def validate_client_info(name, phone_number, email_address):
    # .strip() is used leading and trialling white spaces
    if not name.strip():
        return False, "Please do not leave any sections blank. Please Try Again :)"
    if any(char.isdigit() for char in name):
        return False, "Sorry numbers cannot be accepted as a name -- Please Try Again :)"

    # Used to validate the phone number is a Valid New Zealand Phone Number
    if not phone_number.strip():
        return False, "Please do not leave any sections blank. Please Try Again :)"
    if not phone_number.isdigit():
        return False, "Please only enter digits as your phone number. Please Try Again :)"
    if not (7 <= len(phone_number) <= 9):
        return False, "Phone number must be between 7 and 9 digits long."

    # Function used to validate the users email
    if not email_address.strip():
        return False, "Please do not leave any sections blank. Please Try Again :)"
    if "@" not in email_address and "." not in email_address:
        return False, "Please enter a valid email which includes at least one ‘.’ and one ‘@’. Please Try Again :)"
    return True, ""


def main():
    while True:
        print("Please enter the correct Information:")
        name = input("Name: ")
        phone = input("Phone: (+64)")
        email = input("Email: ")

        valid, message = validate_client_info(name, phone, email)
        if not valid:
            print(message)
            continue

        nz_phone_number = "+64" + phone

        print("\n— Clients Info —")
        print(f"Name: {name}")
        print(f"Phone: {nz_phone_number}")
        print(f"Email: {email}")
        print("-------------------\n")

        again = input("Would you like to enter another booking? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you. Program ended.")
            break

if __name__ == "__main__":
    main()
