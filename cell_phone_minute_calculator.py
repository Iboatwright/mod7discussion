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
        minutesAllowed = 0
        minutesUsed = 0
        totalDue = 0
        minutesOver = 0

        # Calls functions/modules
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed,
                                          totalDue, minutesOver)
        display_results(minutesAllowed, minutesUsed, totalDue, minutesOver)
        endProgram = input("Do you want to end program? yes or no")
        while endProgram.lower() != 'yes' or endProgram.lower() != 'no':
            print('Error: Invalid entry.')
            endProgram = input("Do you want to end program? yes or no")
    return None

# todo: Add comments for all the functions.
def getAllowed(minsAllowed):
# todo: Add code for all the functions.
    return minsAllowed

def getUsed(minsUsed):

    return minsUsed

def calcTotal(minsAllowed, minsUsed, totalDue, minsOver):

    return totalDue, minsOver

def display_results(minsAllowed, minsUsed, totalDue, minsOver):

    return None


# Call main module.
main()