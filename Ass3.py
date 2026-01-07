def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 4
    else:
        bill = (100 * 2) + (100 * 4) + (units - 200) * 6

    return bill
print(calculate_electricity_bill(80))    
print(calculate_electricity_bill(150))   
print(calculate_electricity_bill(250))   