class Restaurant:
    def __init__(self):
        self.menu = {
            "Burger": 50.00,
            "Fries": 30.00,
            "Fried Chicken": 85.00,
            "Spaghetti": 60.00,
            "Soda": 25.00,
            "Ice Cream": 20.00
        }

        self.orders = []

    def display_menu(self):
        print("=" * 35)
        print(f"{'FAST FOOD MENU':^35}")
        print("=" * 35)

        for item, price in self.menu.items():
            print(f"{item:<20} ₱{price:>8.2f}")

        print("=" * 35)

    def add_order(self, item_name, quantity):
        price = self.menu[item_name]

        self.orders.append({
            "name": item_name,
            "quantity": quantity,
            "unit_price": price,
            "total_price": price * quantity
        })

    def calculate_total(self):
        total = 0.0

        for order in self.orders:
            total += order["total_price"]

        return total

    def print_receipt(self):
        total_amount = self.calculate_total()

        print("\n" + "*" * 35)
        print(f"{'FAST FOOD RESTAURANT':^35}")
        print(f"{'Official Receipt':^35}")
        print("*" * 35)

        print(f"{'QTY':<4} {'ITEM':<15} {'PRICE':>6} {'TOTAL':>7}")
        print("-" * 35)

        for order in self.orders:
            print(
                f"{order['quantity']:<4} "
                f"{order['name']:<15} "
                f"{order['unit_price']:>6.2f} "
                f"{order['total_price']:>7.2f}"
            )

        print("-" * 35)
        print(f"{'TOTAL AMOUNT DUE:':<25} ₱{total_amount:>7.2f}")
        print("*" * 35)
        print(f"{'Thank you for dining with us!':^35}")
        print("*" * 35)