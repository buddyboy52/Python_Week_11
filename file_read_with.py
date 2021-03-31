#Name: file_read.py
#Author: Andrew McCloud
#Created: 
#Purpose: Read and display a text file using with

def main():

    # Open a file in the same folder as the program
    # We create an object named text_file
    # This is called a file handle
    with open('example.txt') as file_object:

        # Read the entire contents of the file into a string
        file_contents = file_object.read()

    # Print the string
    print(file_contents)

# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
