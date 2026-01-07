# Course Fee Billing System

course = input("Enter course name: ")

if course == "Python Programming":
    fee = 5000
elif course == "Data Analytics":
    fee = 8000
elif course == "AI& ML":
    fee = 12000
else:
    print("Invalid course")
    exit()

# Discount calculation
student_discount = fee * 0.10     # 10%
early_discount = fee * 0.05       # 5%

total_discount = student_discount + early_discount
final_amount = fee - total_discount

# Output
print("\nCourse Name:", course)
print("Original Fee: ₹", fee)
print("Total Discount: ₹", total_discount)
print("Final Payable Amount: ₹", final_amount)
