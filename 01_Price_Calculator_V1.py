# Doesn't validate decimal or whole number input yet

def validate_seat_numbers(recliners, bunks):
    max_recliner_seats = 20
    max_bunks_seats = 15

    if recliners < 0 or bunks < 0:
        return False, "Invalid response: we cannot accept negative integers. Please try again :)"
    if recliners > max_recliner_seats:
        return False, f"The max number of recliners is {max_recliner_seats}. Please try again :)"
    if bunks > max_bunks_seats:
        return False, f"The max number of bunks is {max_bunks_seats}. Please try again :)"
    if recliners == 0 and bunks == 0:
        return False, "You must purchase at least one seat. Please try again :)"
    return True, ""


def calculate_cost(recliners, bunks):
    price_per_recliner = 25
    price_per_bunk = 50

    total_recliners = recliners * price_per_recliner
    total_bunks = bunks * price_per_bunk
    total_cost = total_recliners + total_bunks

    gst_portion = total_cost - (total_cost / 1.15)
    gst_portion = round(gst_portion, 2)

    return total_cost, gst_portion


def main():
    while True:
        print("How many seats would you like to buy?")
        recliner_input = input("Recliners: ")
        bunks_input = input("Bunks: ")

        # No check for whole numbers or decimals
        recliners = int(recliner_input)
        bunks = int(bunks_input)

        valid, message = validate_seat_numbers(recliners, bunks)
        if not valid:
            print(message)
            continue

        total, gst = calculate_cost(recliners, bunks)

        print("\n--- Purchase Summary ---")
        print(f"Recliners: {recliners}")
        print(f"Bunks: {bunks}")
        print(f"Total cost: ${total}")
        print(f"GST portion: ${gst}")
        print("------------------------\n")

        again = input("Would you like to enter another booking? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you. Program ended.")
            break


if __name__ == "__main__":
    main()
