# This program outputs a specific month in any year a user requires
from calendar import *

year = input(" Enter calender year : ")
while not year.isnumeric():
   year = input(" Enter calender year : ")

mon = input(" Enter month? : \n(Enter any integer from 1 to 12): ")
while not mon.isnumeric():
   mon = input(" Enter month? : ")

output_month= month(int(year),int(mon))
print(output_month)


"""  Remove the # sign from the code below if you want to output it to a word document"""
# with open("text1.docx","w") as file:
#    file.write(output_month)