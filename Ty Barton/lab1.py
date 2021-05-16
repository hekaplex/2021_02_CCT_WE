print('What is your name?')
x = input('Enter your name:')
print('Hello,' + x)

print('What is your age?')
x = input('Enter your age:')
print(x)
print('Add 10 to your age')
print("The sum is:",int(x) + 10)

print("Remember this number later, it is your Lucky Number.")

print("Welcome to the world created by you.")
print("You Have a Six Sided Die, Each Roll Will Earn You Gear")

def read_items():
    items = []
    with open("Items.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
    return items
    
import random

mylist = read_items()

print(random.choice(mylist))