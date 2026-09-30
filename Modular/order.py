# Function to calculate order totals
def calculate_order_totals(order_list):
    detailed_orders = []
    grand_total = 0.0

    for item_name, quantity, price in order_list:
        total_item_price = price * quantity
        grand_total += total_item_price

        detailed_orders.append({
            "name": item_name,
            "quantity": quantity,
            "unit_price": price,
            "total_price": total_item_price
        })

    return detailed_orders, grand_total