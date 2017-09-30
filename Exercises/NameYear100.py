import datetime as dt
from datetime import datetime

name = input("Can you please state your name ? ")
age = int(input("Can you please state your age ?" ))
yearsToHundred = 0

if(age < 100):
    now = datetime.now()
    yearsToHundred = now.year + (100-age)


print("Your name is " + name)
print("You will be a Hundred Years old in %s" %(yearsToHundred))