#LIST
students=["Somanth","Raghav","Ravi"] #creation of list
print(students)
#accessing the list elements
print(students[0])
print(students[-1])
print(students[-3:-1])#slicing
#method of lists
students.append("Rakshita")
students.insert(1,"Shankar")
students.remove("Rakshita")
#students.pop()
print(students)
#sorting the list
students.sort()
print(students)
students.reverse()
print(students)
len(students)
['Somanth', 'Raghav', 'Ravi']
Somanth
Ravi
#tuple
course=("Python",3,12500,12500)
#access tuple element
print(course[1])
print(course[-1])
print(course[0:2])
#methods
print(course.count(12500))
print(course.index(3))
print(course)
#delete element indirect way
cou=list(course)
cou.pop()
course=tuple(cou)
print(course)
3
12500
('Python', 3)
2
1
('Python', 3, 12500, 12500)
('Python', 3, 12500)
#dictionary
employees={
 1001:"Ramesh",1002:"Suresh",1003:"Rajesh"
}
print(employees)
print(employees[1002])
print(employees.keys())
print(employees.values())
employees[1005]="Radhika"
employees[1001]='Rakesh'
employees[1005]='Rakesh'
print(employees)
len(employees)