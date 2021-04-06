#Name: file_append.py
#Author: Andrew McCloud
#Created: 
#Purpose: Write 3 lines of data to a text file

def main():

    # Catch any exceptions
    try:
        # Create a file handle
        # for writing to rockstars.txt
        rock_file = open('rockstars.txt', 'a')

        # Write the names of three rock stars to the file
        # Substitute your favorites
        # \n is an escape character creating a new line
        rock_file.write(f'Eddie Van Halen\n')
        rock_file.write(f'Eric Clapton\n')
        rock_file.write(f'Steve Gadd\n')
        print('File Written Successfully')

    # Let the user know when there was an exception
    except:
        print('The file was not written')

    # Regardless of what happens, the file handle is closed
    finally:
        # Close the file handle
        rock_file.close()

# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
