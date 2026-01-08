

# 1. Arithmetic Operators
price = 100
total = price + 18
print("Total bill:", total)

print("Remainder:", 10 % 3)
print("Power:", 2 ** 2)


# 2. Relational Operators
age = 20
print("Can vote:", age >= 18)

print("Salary compare:", 30000 > 25000)
print("PIN correct:", 1234 == 1234)


# 3. Logical Operators
marks = 50
attendance = 80
print("Pass:", marks > 40 and attendance > 75)

print("Login allowed:", True or False)
print("Blocked:", not False)


# 4. Assignment Operators
wallet = 500
wallet -= 100
print("Wallet:", wallet)

score = 5
score += 1
print("Score:", score)

stock = 20
stock -= 5
print("Stock:", stock)


# 5. Bitwise Operators
a = 4
b = 2
print("AND:", a & b)
print("OR:", a | b)

print("Left shift:", a << 1)
print("Right shift:", a >> 1)


# 6. Membership Operators
names = ["Raju", "Amit"]
print("Raju in list:", "Raju" in names)

items = ["Pen", "Book"]
print("Phone not in items:", "Phone" not in items)


# 7. Identity Operators
x = 10
y = 10
print("x is y:", x is y)
print("x is not y:", x is not y)