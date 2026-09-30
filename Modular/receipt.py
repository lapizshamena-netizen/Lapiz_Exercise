# Function to print receipt
def print_receipt(processed_orders, total_amount):
    print("\n" + "*" * 35)
    print(f"{'FAST FOOD RESTAURANT':^35}")
    print(f"{'Official Receipt':^35}")
    print("*" * 35)

    print(f"{'QTY':<4} {'ITEM':<15} {'PRICE':>6} {'TOTAL':>7}")
    print("-" * 35)

    for order in processed_orders:
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
    print("*" * 35 + "\n")