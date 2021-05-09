#---importing and defining
import csv
timeLog = "time_log.txt"
employeeList = "employees.csv"

with open(employeeList) as file:
    employee = []
    minutes = []
    for l in lines:
        as_list = l.split(", ")
        employee.append(as_list[0])
        minutes.append(as_list[1].replace("\n", ""))
print(employee)
print(minutes)