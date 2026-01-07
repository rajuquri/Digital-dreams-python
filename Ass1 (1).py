name=input("enter a name:")
age=int(input("enter age:"))
email=input("enter email id:")
contact=input("enter cantact number:")
percentage=float(input("enter percentage:"))
if age>=18:
    if percentage>60:
        if len(contact)==10:
            print("eligible inter")
        else:
            print("cantact number must be 10 digits")
    else:
        print("percentage must be greater than 60")
else:
    print("age must be greater than 18")