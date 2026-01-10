
# Online Python - IDE, Editor, Compiler, Interpreter
# ASSIGNMENT 1: Online Exam Score Analyzer (List + Operators)
scores = [78, 85, 90, 66, 72]
print("Total Score:", sum(scores))
print("Average Score:", sum(scores) / len(scores))
print("Count:", len(scores))


# ASSIGNMENT 2: Website Traffic Analysis (List)
visitors = [120, 150, 90, 200, 175, 160, 140]
print("Highest Traffic:", max(visitors))
print("Lowest Traffic:", min(visitors))


# ASSIGNMENT 3: Customer Purchase Validation (If-Else)
amount = float(input("Enter purchase amount: "))
if amount > 0:
    print("Valid Purchase")
else:
    print("Invalid Purchase")


# ASSIGNMENT 4: Course Fee Billing System (If-Else only)
course = input("Enter course name: ")
if course == "Python":
    fee = 5000
elif course == "Data Analytics":
    fee = 8000
elif course == "AI & ML":
    fee = 12000
else:
    fee = 0

discount = fee * 0.10
print("Final Fee:", fee - discount)


# ASSIGNMENT 5: Product Discount Function
def calculate_discount(price, customer_type):
    if customer_type == "Regular":
        return price * 0.95
    elif customer_type == "Premium":
        return price * 0.85
    elif customer_type == "Employee":
        return price * 0.75
    else:
        return price

print(calculate_discount(1000, "Premium"))


# ASSIGNMENT 6: Password Strength Checker
def password_strength(password):
    if len(password) >= 8:
        return "Strong Password"
    else:
        return "Weak Password"

print(password_strength("mypassword"))


# ASSIGNMENT 7: Arithmetic Operators
price = 1000
gst = price * 0.18
print("Total Bill:", price + gst)


# ASSIGNMENT 8: Assignment Operators
wallet = 2000
wallet -= 500
print("Wallet Balance:", wallet)


# ASSIGNMENT 9: Product Price Lock System (Tuple)
prices = (100, 200, 300)
print("Product Price:", prices[1])
print("Tuple values cannot be changed")


# ASSIGNMENT 10: Order Summary Generator (Dictionary)
order = {
    "Product": "Laptop",
    "Price": 50000,
    "Quantity": 1
}

total_amount = order["Price"] * order["Quantity"]
print("Order Details:", order)
print("Total Amount:", total_amount)