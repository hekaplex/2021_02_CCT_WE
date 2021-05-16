#---importing and defining functions
from datetime import date,time,datetime
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

#  TODO this function needs to have input parameters for userName and totalTime
def write_log():
    with open(timeLog, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(userName + datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S" + totalTime + "\n"))
        file.close()
    print("Log entry complete. Total time for user \"", userName, "\" spent on project: ", totalTime, " minutes.")
    print()
    print("Your log has been submitted. Thank you for using the log entry system.")

def get_times():
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


def verify_user():
    try:
        print("Validating user: " + userName)
        # TODO your function's result that returns teh list should be assigned to names
        read_names()
        if userName.lower() in names:
            pass
        else:
            pass
    except:
        print("Employee not found.")
        print("Please check spelling, or contact lead engineer to be added to employee list.")
        main()
    else:
        print("User verified.")
        get_times()

def main():
    print("Welcome to the project time-logging system.")
    print()
    userName = input("Insert name to begin, or type Exit to leave: ")
    # TODO should be == for comparison = is an assignment
    if userName.lower() = "exit":
        break
    else:
        verify_user()

if __name__ == "__main__":
    main()