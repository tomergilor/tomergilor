

def get_employee(obj):
    return ("{0} his salary is {1} and position is {2}".format(obj["name"], obj["salary"], obj["position"]))

def get_salary(obj):
    name = obj["name"]
    print("Your salary is {0}".format(obj["salary"]))

def update_salary(obj, salary):
    obj["salary"] = salary

emp1 = {"name":"roman","position":"cyber","salary":1000}
my_emp = get_employee(emp1)
print (my_emp)

get_salary(emp1)
update_salary(emp1,2000)
get_salary(emp1)

