#---importing and defining
import csv

timeLog = "time_log.txt"
employeeList = "employees.csv"

def READ_EMP():
    with open(employeeList) as file:
        for line in file:
            line = line.replace("\n", "")
            employees.append(line)


def WRITE_LOG()


#---Identify User
print("Welcome to the project time-logging system.")
userName = input("Insert name to begin: ")

#---Collect data
print("Enter the amount of time (in minutes) spend working on the project.")
print("Reminder: if you spend over 60 minutes on the project, it must be reported directly to the lead engineer.")
timeClock = 0
totalTime = 0
while True:
    timeClock = int(input("Enter project time (type 1234 to finish):"))
    if timeClock >0 and timeClock <=60:
        totalTime += timeClock
    elif timeClock == 1234:
        break
    elif timeClock <=0:
        print("Time must be at least one minute. Please re-enter.")
    else:
        print("Please report times of over one hour to lead engineer.")
    

#---calculate total time and record in log


print("Log entry complete. Total time for user \"", userName, "\" spent on project: ", totalTime, " minutes.")
print()
print("Your log has been submitted. Thank you for using the log entry system.")