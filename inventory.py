inventory = {
    "Laptop": {"price": 799.99, "quantity": 12},
    "Keyboard": {"price": 29.99, "quantity": 4},
    "Mouse": {"price": 19.99, "quantity": 2},
    "Monitor": {"price": 149.99, "quantity": 5},
    "USB Cable": {"price": 7.99, "quantity": 0},
}


def check_low_stock(threshold):
    for item_name, details in inventory.items():
        if details["quantity"] < threshold:
            print(f"{item_name}: {details['quantity']} in stock")


if __name__ == "__main__":
    print("Products with fewer than 5 in stock:")
    check_low_stock(5)
