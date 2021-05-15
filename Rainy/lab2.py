#---importing and defining functions
import csv
timeLog = "time_log.txt"
employeeList = "employees.csv"

def read_names():
    names = []
    with open(employeeList, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row)
    return names

def write_log():
    with open(timeLog, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(userName + totalTime + "\n")
        file.close()

def verify_user(userName):
    try:
        with open(employeeList as file)
            print("Validating user: " + userName)
            if userName in names
    except ValueError:
        print("Employee not found. Please check spelling, or contact lead engineer to be added to employee list.")
    else:
        print("User verified.")
    finally:
        file.close()
        print("Validation complete.")


#---Identify User
print("Welcome to the project time-logging system.")
userName = input("Insert name to begin: ")
read_names()
verify_user()

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
write_log()
print("Log entry complete. Total time for user \"", userName, "\" spent on project: ", totalTime, " minutes.")
print()
print("Your log has been submitted. Thank you for using the log entry system.")