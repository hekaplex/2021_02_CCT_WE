#at least one input
#at least one validation of input in UI or code
#at least one calculation
#at least one returned value

print("Ninja Name Generator")

name = input("Enter your name: ")

if not name.isalpha():
    print("Your name must be alphabet characters only!  Try again!")

ninjaName = ""
ninjaParts = ["KA","ZU","MI","TE","KU","LU","JI","RI","KI","ZU","ME","TA","RIN","TO","MO","NO","KE","SHI","ARI","CHI","DO","RU","MEI","NA","FU","ZI"]

for i in range(0,len(name)):
    ninjaName += ninjaParts[ord(name[i].lower()) - ord('a')]

print("Your ninja name is: " + ninjaName)
