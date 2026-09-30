import sys

from menu import MENU, display_menu
from order import calculate_order_totals
from receipt import print_receipt


def main():
    display_menu(MENU)

    user_choice = input("Do you want to order? (yes/no): ").strip().lower()

    if user_choice not in ['yes', 'y']:
        print("Thank you for visiting! Have a great day.")
        sys.exit()

    user_orders = []

    while True:
        item_name = input("\nEnter the item name: ").strip().title()

        if item_name not in MENU:
            print("Invalid item! Please select an item from the menu.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Invalid input! Please enter a valid number for quantity.")
            continue

        user_orders.append(
            (item_name, quantity, MENU[item_name])
        )

        another = input(
            "\nDo you want to order another item? (yes/no): "
        ).strip().lower()

        if another not in ['yes', 'y']:
            break

    if user_orders:
        processed_orders, grand_total = calculate_order_totals(user_orders)
        print_receipt(processed_orders, grand_total)


if __name__ == "__main__":
    main()