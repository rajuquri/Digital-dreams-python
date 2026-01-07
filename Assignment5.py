# Input details
emp_name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
rating = int(input("Enter performance rating (1-5): "))

# Bonus calculation using conditional statements
if rating == 5:
    bonus = salary * 0.20
elif rating == 4:
    bonus = salary * 0.15
elif rating == 3:
    bonus = salary * 0.10
else:
    bonus = 0

# Final salary
final_salary = salary + bonus

# Display output
print("\nEmployee Name:", emp_name)
print("Performance Rating:", rating)
print("Bonus Amount: ₹", bonus)
print("Final Salary: ₹", final_salary)
