#Add a new key
employee = {
    "name": "Wilsom",
    "age": 30,
    "department": "IT",
    "salary": 90000
}
employee["city"] = "Hyderabad"
print(employee)

#Update a value
employee = {
    "name": "Wilson",
    "age": 30,
    "department": "IT",
    "salary": 90000
}
employee.update({"salary":85000})
for k,v in employee.items():print(k,v)

#Check whether a key exists
employee = {
    "name": "Wilson",
    "age": 30,
    "department": "IT",
    "salary": 90000
}
a=input("enter key to check")
if a in employee.keys():print("found")
else:print("not found")

#Q5. Count frequency of elements
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 20]
d={}
for i in numbers:
  d[i]=(numbers.count(i))
  
print(d)

#Find the highest salary
employees = {
    "wilson": 90000,
    "tony": 85000,
    "mony": 65000,
    "Pintu": 95000,
    "Rony": 72000
}
a=int(max(employees.values()))
for name,sal in employees.items():
  if a==sal:
   print(name)
   
  else: continue 


#Find employees earning above average salary
employees = {
     "wilson": 90000,
        "tony": 85000,
        "mony": 65000,
        "Pintu": 95000,
        "Rony": 72000
}
a=int(sum(employees.values())/(len(employees.values())))
print("average is :",a)
print("employee with sal greater than avg:")
for name,sal in employees.items():
  if sal>a:print(name,sal)
  else:continue


#find the email of employe by it name
Employee={101:["Ajay","Ajay@gmail.com",20000],102:["sachin","sachin@gmail.com,",90000]}
a=input("enter name")
for k,v in Employee.items():
   if a == v[0]:
    print(v[1])
   else:continue
