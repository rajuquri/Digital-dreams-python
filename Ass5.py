def calculate_discount(price, customer_type):
    if customer_type == "Regular":
        return price - (price * 0.05)
    elif customer_type == "Premium":
        return price - (price * 0.15)
    elif customer_type == "Employee":
        return price - (price * 0.25)
    else:
        return price

# Example
print(calculate_discount(1250, "Regular"))
print(calculate_discount(1250, "Premium"))
print(calculate_discount(1250, "Employee"))