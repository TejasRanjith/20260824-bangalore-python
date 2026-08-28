'''
Leap Year Programming in Python

Write a program that takes a year as input from the user and checks whether it is a leap year or not.
'''


def main():
    year = int(input("Enter the year to check: "))
    if year <=0:
        print("Not a Valid year, please retry again.")
    elif year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
        print("It is a leap year.")
    else:
        print("It is not a leap year.")

main()