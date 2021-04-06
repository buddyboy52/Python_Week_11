#Name: file_read_numbers.py
#Author: Andrew McCloud
#Created:
#Purpose: Numbers must be converted from strings to ints

# Constants for filename
FILE_NAME = 'numbers.txt'

def main():

    # Catch any exceptions
    try:
        # Open a file for reading
        number_file = open(FILE_NAME, 'r')

        # Read 3 numbers from a file
        number1 = int(number_file.readline())
        number2 = int(number_file.readline())
        number3 = int(number_file.readline())

        # Sum the numbers
        total = number1 + number2 + number3

        # Display the numbers and the total
        # A different way of printing numbers as strings
        print(f'The numbers are: {number1} {number2} {number3}')
        print(f'The total is: {total}')

    # Let the user know there was trouble
    except:
        print('There was trouble reading the file.')

    # No matter what happens, close the file
    finally:
        # Close the file
        number_file.close()


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
