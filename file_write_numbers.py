#Name: file_write_numbers.py
#Author: Andrew McCloud
#Created:
#Purpose: Numbers must be converted to strings before
# they are written to a text file

# Constants for filename
FILE_NAME = 'numbers.txt'

def main():
    # Catch any exceptions
    try:
        # Open a file for writing
        number_file = open(FILE_NAME, 'w')

        # Get three numbers from the user
        number1 = int(input('Enter a whole number: '))
        number2 = int(input('Enter another whole number: '))
        number3 = int(input('Enter another whole number: '))

        # Write the numbers to the file using FStrings
        number_file.write(f'{number1}\n')
        number_file.write(f'{number2}\n')
        number_file.write(f'{number3}\n')

        # Let the user know it worked
        print('Data was successfuly written to numbers.txt')

    # Let the user know there was trouble
    except:
        print('There was trouble writing to the file')

    # No matter what happens, close the file
    finally:
        # Close the file
        number_file.close()





# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
