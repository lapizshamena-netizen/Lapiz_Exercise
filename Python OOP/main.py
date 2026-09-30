from restaurant import Restaurant


def main():
    restaurant = Restaurant()

    restaurant.display_menu()

    user_choice = input(
        "Do you want to order? (yes/no): "
    ).strip().lower()

    if user_choice not in ['yes', 'y']:
        print("Thank you for visiting! Have a great day.")
        return

    while True:
        item_name = input(
            "\nEnter the item name: "
        ).strip().title()

        if item_name not in restaurant.menu:
            print(
                "Invalid item! Please select an item from the menu."
            )
            continue

        try:
            quantity = int(
                input(f"Enter quantity for {item_name}: ")
            )

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print(
                "Invalid input! Please enter a valid number "
                "for quantity."
            )
            continue

        restaurant.add_order(item_name, quantity)

        another = input(
            "\nDo you want to order another item? (yes/no): "
        ).strip().lower()

        if another not in ['yes', 'y']:
            break

    if restaurant.orders:
        restaurant.print_receipt()


if __name__ == "__main__":
    main()