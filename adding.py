#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on August 2020
# This program adds two user inputted integers


def main():
    # This function adds two user inputted integers

    # Input
    variable_x = float(input("Enter the first integer to be added: "))
    variable_y = float(input("Enter the second integer to be added: "))

    # Process
    total = variable_x + variable_y

    # Output
    print("")
    print("The equation is {0} + {1} = {2}"
          .format(variable_x, variable_y, total))


if __name__ == "__main__":
    main()
