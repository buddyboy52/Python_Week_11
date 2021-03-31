#Name: file_read.py
#Author: Andrew McCloud
#Created: 
#Purpose: Read and Display a text file

def main():

    # Open a file in the same folder as the program
    # We create an object name text_file
    # This is called a file handle
    text_file = open('example.txt', 'r')

    # Read the entire contents of the file into a String
    file_contents = text_file.read()

    # Close the file handle
    text_file.close()

    # Print the string
    print(file_contents)


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
