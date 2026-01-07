e_name=input("enter employee name:")
e_id=input("enter emplyee id:")
e_salary=float(input("enter employes salary:"))
hra=e_salary*0.20
da=e_salary*0.10
pf=e_salary*0.12
netsalary=e_salary+hra+da-pf
print(netsalary)
