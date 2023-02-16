"""
    CS051P Lab Assignments: Credit Cards

    Author: Pine Netcharussaeng

    Date:   WHEN YOU COMPLETED IT

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""

from random import randint
from creditcard_part1 import last_digit, decimal_right_shift

def luhn_sum(number13):
    """
    Calculates sum of a positive 13-digit integer

    :param number13: (int) a 13-digit positive integer
    :return: (int) sum of the 13-digit number
    """
    sum = 0
# Evaluate position in 13-digit number
    for digit in range(13):
        # Multiply the odd location by 2 and add it to the total sum
        if digit % 2 != 0:
            if last_digit(number13) >= 5:
                sum = sum + (last_digit(number13) * 2) - 9
            else:
                sum = sum + last_digit(number13) * 2
        # Add the even number to the total sum
        else:
            sum = sum + last_digit(number13)
        # Shift the 13-digit number to get a new last digit
        number13 = decimal_right_shift(number13)

    return sum


def verify(number13):
    """
      Verifies if the sum of a 13-digit positive integer is a luhn sum

      :param number13: (int) a positive 13-digit integer
      :return: True
    """
# Return true if last digit of luhn sum is 0
    sum = luhn_sum(number13)
    return last_digit(sum) == 0


def generate(number6):
    """
    Generates a 13-digit number from a 6-digit number that passes luhn sum

    :param number6: (int) a 6-digit positive integer
    :return: (int) a 13-digit number that passes the luhn sum
    """
# Multiply the 6-digit number by a million to get 12-digit number that ends in 000000
    number12 = number6 * 1000000
# Add 12-digit number to 6-digit random number and make number into a 13-digit number
    card_number = (number12 + randint(0,999999)) * 10
# Calculate the luhn sum of the 13-digit number
    total = luhn_sum(card_number)
# Find the remainder that will make 13-digit number pass luhn sum
    remainder = 10 - last_digit(total)

    return card_number + remainder

def main():
    """
    Generates three 13-digit numbers that passes the luhn sum

    :return: (int) three 13-digit numbers that passes the luhn sum
    """
# Ask user input for 6-digit number
    six_digit_int = input("Enter a six digit number:\n")
    # Check if input is a number and if the number is 6 digits
    while six_digit_int != six_digit_int.isdigit and len(six_digit_int) != 6:
        six_digit_int = input("Enter a six digit number:\n")
    # Generate three valid 13-digit card number
    for amount in range(3):
        print(generate(int(six_digit_int)))



if __name__ == "__main__":
    main()
