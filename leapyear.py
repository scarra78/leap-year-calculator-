# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

#  Don't change the code below 👇
year = int(input("Which year do you want to check? "))
#  Don't change the code above 👆

# Write your code below:
if year % 4 ==0 and year % 100!= 0 or year % 100 ==0 and year % 400 ==0 and year % 4==0:
    print("this is a leap year")
else:  
    print("this is not a leap year")   