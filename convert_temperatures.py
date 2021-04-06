#Name: convert_temperatures.py
#Author: Andrew McCloud
#Created:
#Purpose: Read a list of temperatures from a file, convert
# them to Fahrenheit. Write to a file and to the screen

# Constant for filename
CFILE = 'ctemps.txt'
FFILE = 'ftemps.txt'

def main():

    # Catch any exceptions
    try:
        # Open a file for writing
        cfile = open(CFILE, 'r')
        ffile = open(FFILE, 'w')

        # Strip the newline character off of every line in the file
        ctemp = [line.strip() for line in cfile]

        # Loop until all the temperatures have been converted
        for t in ctemp:
            # Convert the temperatures have been converted
            ftemp = float(t) * (9.0/5.0) + 32.0

            # Write the temperature to the file
            ffile.write(f'{ftemp}\n')

            # Print the conversion to the screen
            print(f'{t} Celsius equals {ftemp} Fahrenheit')

        # Let the user know there was an exception
    except:
        print('A file exception occured')

    # Regardless of what happens, the file is closed
    finally:
        # Close both files
        cfile.close()
        ffile.close()

# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
