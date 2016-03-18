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
# March 17, 2016

def main():
    # Declare local variables
    endProgram = 'no'

    # The program will continue looping until the user sets
    #   endProgram == 'yes' when prompted.
    while endProgram.lower() in ['no','']:
        # This sets and resets the variables.
        minutesAllowed = 0.0
        minutesUsed = 0.0
        totalDue = 0.0
        minutesOver = 0.0

        # Calls functions/modules
        minutesAllowed = getAllowed()
        minutesUsed = getUsed()
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed)

        # Pass the arguements through the f_num filter before sending to
        #   the display module.
        display_results(f_num(minutesAllowed), f_num(minutesUsed),
                        f_num(totalDue), f_num(minutesOver))

        # User is given the option to end the program loop by entering 'yes'.
        #   The user can enter 'no' or press enter to start a new loop.
        endProgram = input("Do you want to end program? yes or (n)o\n    >>>")

        # If the user enters anything other than 'yes', 'no' or enter this loop
        #   requests new/valid input.
        while endProgram.lower() not in ['yes', 'no', '']:
            print('Error: Invalid entry.')
            endProgram = input("Do you want to end program? yes or "
                               "(n)o\n    >>>")
    return None


# This requests the user input the number of minutes in the cell phone plan.
#   Only values between 200 and 800 are accepted.  For any other value
#   the user is requested to re-enter a valid value.
def getAllowed():
    minsAllowed = float(input('How many minutes are allowed?\n   >>> '))
    while minsAllowed < 200 or minsAllowed > 800:
        print('Please enter minutes between 200 and 800.')
        minsAllowed = float(input('How many minutes are allowed?\n   >>> '))
    # The valid number of minutes allowed is returned.
    return minsAllowed


# getUsed requests the user to input the number of minutes used during this
#   billing period.  It validates the entry is a positive number and returns
#   the value.
def getUsed():
    minsUsed = float(input('How many minutes were used?\n   >>> '))
    while minsUsed < 0.0:
        print('Please enter minutes of at least 0.')
        minsUsed = float(input('How many minutes were used?\n   >>> '))
    # The valid number of minutes used is returned.
    return minsUsed


# calcTotal uses the minutes allowed and minutes used values passed from
#   the main module to calculate how much is due and how many minutes over
#   this month.  Those values are returned to the calling module.
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
        print('You were over your minutes by {} minutes.'.format(
                                                            f_num(minsOver)))
    return totalDue, minsOver


# Formats a float to either a whole number or two decimal places and returns
#   the value as a string.  Any other value passed is formatted to a string
#   and returned.
def f_num(n):
    if isinstance(n,float):
        n = '{}'.format(int(n)) if n.is_integer() else '{:.2f}'.format(n)
    else:
        n = '{}'.format(n)
    return n


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(minsAllowed, minsUsed, totalDue, minsOver):
    print('----------------MONTHLY USE REPORT----------------------')
    print('Minutes allowed were: {}'.format(minsAllowed))
    print('Minutes used were: {}'.format(minsUsed))
    print('Minutes over were: {}'.format(minsOver))
    print('Total due is ${}'.format(totalDue))
    return None


# Call main module.
main()