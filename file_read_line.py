#Name: file_read_line.py
#Author: Andrew McCloud
#Created:
#Purpose: Read and display a text file line by line

def main():

    # Catch any exceptions in the program
    try:
        # Open a file in the same folder as the program
        text_file = open('rockstars.txt', 'r')

        # Read each line into a seperate string
        line1 = text_file.readline()
        line2 = text_file.readline()
        line3 = text_file.readline()

        line1 = line1.rstrip('\n')
        line2 = line2.rstrip('\n')
        line3 = line3.rstrip('\n')

        # Print the strings
        print(line1)
        print(line2)
        print(line3)
        print('The file was successfully read.')

    # Let the user know if there was an exception
    except:
        print('There was a problem reading the file.')

    # No matter what else happened, close the file handle
    finally:
        # close the file handle
        text_file.close()





# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
