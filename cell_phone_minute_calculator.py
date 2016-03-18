# cell_phone_minute_calculator.py
# Exercises selected: Lab 8.5 - Cell Phone Minute Calculator
# Name of program: Cell Phone Minute Calculator
# Description of program: This program calculates and displays the number
#   of minutes over the monthly contract minutes that a cell phone user
#   incurred.  The program asks how many minutes were used during the
#   month and how many were allowed.  The input is validated as such:
#   200 <= minutes allowed <= 800 and minutes used >= 0.
#
# Ivan Boatwright
# March 11, 2016

def main():
    # Declare local variables
    endProgram = 'no'
    while endProgram.lower() == 'no':
        minutesAllowed = 0.0
        minutesUsed = 0.0
        totalDue = 0.0
        minutesOver = 0.0

        # Calls functions/modules
        minutesAllowed = getAllowed()
        minutesUsed = getUsed()
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed)
        display_results(minutesAllowed, minutesUsed, totalDue, minutesOver)
        endProgram = input("Do you want to end program? yes or no\n    >>>")
        while endProgram.lower() != 'yes' and endProgram.lower() != 'no':
            print('Error: Invalid entry.')
            endProgram = input("Do you want to end program? yes or no\n    >>>")
    return None

# todo: Add comments for all the functions.
def getAllowed():
    minsAllowed = float(input('How many minutes are allowed?\n   >>> '))
    while minsAllowed < 200 or minsAllowed > 800:
        print('Please enter minutes between 200 and 800.')
        minsAllowed = float(input('How many minutes are allowed?\n   >>> '))
    return minsAllowed


def getUsed():
    minsUsed = float(input('How many minutes were used?\n   >>> '))
    while minsUsed < 0.0:
        print('Please enter minutes of at least 0.')
        minsUsed = float(input('How many minutes were used?\n   >>> '))
    return minsUsed


def calcTotal(minsAllowed, minsUsed):
    extra = 0.0
    if minsUsed <= minsAllowed:
        totalDue = 74.99
        minsOver = 0
        print('You were not over your minutes for the month')
    else:
        minsOver = minsUsed - minsAllowed
        extra = minsOver * .20
        totalDue = 74.99 + extra
        print('You were over your minutes by {} minutes.'.format(minsOver))
    return totalDue, minsOver

def display_results(minsAllowed, minsUsed, totalDue, minsOver):
    print('----------------MONTHLY USE REPORT----------------------')
    print('Minutes allowed were: {}'.format(minsAllowed))
    print('Minutes used were: {}'.format(minsUsed))
    print('Minutes over were: {}'.format(minsOver))
    print('Total due is ${}'.format(totalDue))
    return None


# Call main module.
main()