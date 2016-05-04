__author__ = 'nathan'

import datetime


def fix_date(date):
    date = date.replace("/"," ")
    date = date.replace("-"," ")
    fixing = date.split(" ")

    #Year first (#### ## ##)
    if len(fixing[0]) == 4:
        fixed = datetime.date(int(fixing[0]),int(fixing[1]),int(fixing[2]))
    #Month First (## ## ####)
    elif len(fixing[2]) == 4:
        fixed = datetime.date(int(fixing[2]),int(fixing[0]),int(fixing[1]))
    print(fixed)


if __name__ == '__main__':
    date= str(input("Enter a date to change to YYYY-MM-DD: "))
    fix_date(date)
