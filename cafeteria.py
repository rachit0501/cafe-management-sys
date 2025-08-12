# Cafeteria Management System with Numbered Menu

menu = {
    1: ("Espresso", 120),
    2: ("Cappuccino", 150),
    3: ("Latte", 160),
    4: ("Mocha", 180),
    5: ("Hot Chocolate", 140),
    6: ("Iced Coffee", 130),
    7: ("Blueberry Muffin", 90),
    8: ("Chocolate Croissant", 100),
    9: ("Cheese Sandwich", 120),
    10: ("Veg Wrap", 110),
    11: ("Chicken Panini", 170)
}

print("Welcome to Brew & Bite Cafe ☕🍰")
print("\nMenu:")
for number, (item, price) in menu.items():
    print(f"{number}. {item} - ₹{price}")

order_list = []
total = 0

while True:
    order_input = input("\nEnter the item number you want to order (or type 'done' to finish): ").strip()

    if order_input.lower() == 'done':
        break

    if order_input.isdigit():
        order_number = int(order_input)
        if order_number in menu:
            item_name, item_price = menu[order_number]
            try:
                quantity = int(input(f"Enter quantity for {item_name}: "))
                cost = item_price * quantity
                order_list.append((item_name, quantity, cost))
                total += cost
                print(f"{item_name} x {quantity} added to your order. Subtotal: ₹{total}")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Invalid item number. Please try again.")
    else:
        print("Please enter a valid number or 'done' to finish.")

print("\n----- Bill Summary -----")
for item, qty, cost in order_list:
    print(f"{item} x {qty} = ₹{cost}")
print(f"Total Bill: ₹{total}")
print("Thank you for visiting Brew & Bite Cafe! Have a great day! 😊")
