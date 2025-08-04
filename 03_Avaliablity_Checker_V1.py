def validate_seat_numbers(recliners, bunks, available_recliners, available_bunks):
    if recliners > available_recliners:
        return False, f"Only {available_recliners} recliner seats available. Please try again :)"
    if bunks > available_bunks:
        return False, f"Only {available_bunks} bunk beds available. Please try again :)"
    if recliners == 0 and bunks == 0:
        return False, "You must purchase at least one seat. Please try again :)"
    return True, ""


def main():
    # Routes and their initial availability
    routes = {
        "1": {"name": "One way to PMR", "recliner": 20, "bunk": 15},
        "2": {"name": "One way to AKL", "recliner": 20, "bunk": 15},
        "3": {"name": "Return to AKL", "recliner": 20, "bunk": 15},
    }

    print("Welcome to Massey Overnighter Booking System\n")

    while True:
        print("Available Routes:")
        for key, value in routes.items():
            print(f"{key}. {value['name']} (Recliners: {value['recliner']}, Bunks: {value['bunk']})")

        route_choice = input("\nEnter the route you want to book (1, 2, or 3): ").strip()
        if route_choice not in routes:
            print("Invalid route number. Try again.\n")
            continue

        route = routes[route_choice]

        # Validate seat numbers
        while True:
            try:
                recliners_requested = (input("How many recliner seats would you like to book (max: 20)? "))
                bunks_requested = (input("How many bunk beds would you like to book (max: 15)? "))
            except ValueError:
                print("Please enter a valid number (you can include decimals).\n")
                continue

            valid, message = validate_seat_numbers(
                recliners_requested, bunks_requested,
                route["recliner"], route["bunk"]
            )
            if valid:
                break
            else:
                print(f"\n{message}\n")

        # Process booking
        route["recliner"] -= recliners_requested
        route["bunk"] -= bunks_requested
        print(f"\nBooking successful for {route['name']}!")

        # Show updated availability
        print("\nUpdated availability:")
        for key, value in routes.items():
            print(f"{value['name']}: Recliners - {value['recliner']}, Bunks - {value['bunk']}")

        # Ask to make another booking
        another = input("\nWould you like to make another booking? (yes/no): ").strip().lower()
        if another != "yes":
            print("\nThank you for using the booking system. Goodbye!")
            break


if __name__ == "__main__":
    main()
