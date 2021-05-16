#---importing and defining functions
from datetime import date,time,datetime
import csv
from os import write
timeLog = "time_log.txt"
employeeList = "employees.csv"

def read_names():
    names = []
    with open(employeeList, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row)
    return names

def rowset_to_text(names):
    strg = ""
    for x in names:
        #each item is a list
        for i in x:
            strg +=i
            strg += ","
    return strg    

#  TODO this function needs to have input parameters for userName and totalTime
def write_log(userName, totalTime):
    with open(timeLog, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([userName,datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M"),totalTime])
        file.close()
    print("Log entry complete. Total time for user \"", userName, "\" spent on project: ", totalTime, " minutes.")
    print()
    print("Your log has been submitted. Thank you for using the log entry system.")
    quit()

def get_times(userName):
    print("Enter the amount of time (in minutes) spend working on the project.")
    print("Reminder: if you spend over 60 minutes on the project, it must be reported directly to the lead engineer.")
    timeClock = 0
    totalTime = 0
    while True:
        timeClock = int(input("Enter project time (type 1234 to finish logging or 6666 to cancel):"))
        if timeClock >0 and timeClock <=60:
            totalTime += timeClock
        elif timeClock == 1234:
            write_log(userName,totalTime)
        elif timeClock <=0:
            print("Time must be at least one minute. Please re-enter.")
        elif timeClock == 6666:
            break
        else:
            print("Please report times of over one hour to lead engineer.")
    write_log(userName, totalTime)


def verify_user(userName):
    names = read_names()
    print("names:", names)
    try:
        print("Validating user: " + userName)
        # TODO your function's result that returns teh list should be assigned to names
       
        if userName.lower() in rowset_to_text(names):
            print("User verified.")
            get_times(userName)
        else:
            print("Employee not found.")
            print("Please check spelling, or contact lead engineer to be added to employee list.")
            main()
    except Exception as e:
        print("An error occured:", e)

def main():
    print("Welcome to the project time-logging system.")
    print()
    userName = input("Insert name to begin, or type Exit to leave: ")

    if userName.lower() == "exit":
        quit()
    else:
        verify_user(userName)

if __name__ == "__main__":
    main()