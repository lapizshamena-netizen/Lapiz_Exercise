# Menu dictionary storing items and prices
MENU = {
    "Burger": 50.00,
    "Fries": 30.00,
    "Fried Chicken": 85.00,
    "Spaghetti": 60.00,
    "Soda": 25.00,
    "Ice Cream": 20.00
}


def display_menu(menu_data):
    print("=" * 35)
    print(f"{'FAST FOOD MENU':^35}")
    print("=" * 35)

    for item, price in menu_data.items():
        print(f"{item:<20} ₱{price:>8.2f}")

    print("=" * 35)