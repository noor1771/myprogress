
""" #if wanted to have user input
menu = ['latte', 'tea', 'americano', 'flat white', 'cappuccino']
stock = {}
for key in menu:
    stock_value = int(input(f"Enter stock value for {key} here: "))
    stock[key] = stock_value

price = {}
for key in menu:
    price_value = float(input(f"Enter price of {key} here: "))
    price[key] = price_value
    """
# Define menu as a list of menu items
menu = ['latte', 'tea', 'americano', 'flat white', 'cappuccino']

# Define stock as a dictionary containing stock quantities for each menu item
stock = {
    'latte': 50,
    'tea': 75,
    'americano': 40,
    'flat white': 30,
    'cappuccino': 60
}

# Define price as a dictionary containing prices for each menu item
price = {
    'latte': 3.50,
    'tea': 2.20,
    'americano': 3.00,
    'flat white': 3.40,
    'cappuccino': 3.60
}

# Initialize total_stock as 0
total_stock = 0

# For each item in the menu:
for item in menu:
    # If the item exists both in stock and price dictionaries:
    if item in stock and item in price:
        # Calculate the value of the item by multiplying stock[item] with price[item]
        item_value = stock[item] * price[item]
        # Add the calculated value to total_stock
        total_stock += item_value

# Display the total_stock value in the desired format
print(f"Total stock value is £{total_stock:.2f}")  # Displaying total stock value with two decimal places