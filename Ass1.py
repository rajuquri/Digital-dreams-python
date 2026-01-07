def check_intern_eligibility(age, percentage):
    if age >= 18 and percentage >= 60:
        return "Eligible"
    else:
        return "Not Eligible"

print(check_intern_eligibility(20, 90))
print(check_intern_eligibility(17, 35))
