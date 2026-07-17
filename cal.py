# Ask the user for the price of one item
price = float(input("Enter the price of one item: "))

# Ask the user for the quantity
quantity = int(input("Enter the quantity you want: "))

# Calculate the total cost
total = price * quantity

# Display the result using an f-string
print(f"{quantity} item(s) at {price:.2f} each = {total:.2f}")
