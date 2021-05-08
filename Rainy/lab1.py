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
    

#---calculate total time
print("Log entry complete. Total time for user \"", userName, "\" spent on project: ", totalTime, " minutes.")
print()
print("Thank you for using the log entry system.")