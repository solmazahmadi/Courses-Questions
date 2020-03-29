#First solution
yearSt = input("Please enter the year: ")# Ask the user to enter a year
year = int(yearSt)
if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
#By zen of Python readibility is important which can be
# improved by second and thrid solutions

#Second solution
yearNum = int(input("Please enter the year: "))
if yearNum % 4 == 0:
    if yearNum % 100 == 0:
        if yearNum % 400 == 0:
            print("This is a leap year")
        else:
            print(" This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
#Although the second solution is more readible,
# it is nested and based on zen of Python but Flat is better
yearNum = int(input("Please enter the year: "))
if yearNum % 400 == 0:
    print("This is a leap year")
elif yearNum % 100 == 0:
    print(" This is not a leap year")
elif yearNum % 4 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")
#readibility, simplicity and effectivness are improved in the third one


