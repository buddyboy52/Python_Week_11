#Name: json_dump_joke_file.py
#Author: Andrew McCloud
#Created:
#Purpose: Get a random jokes from the JokeAPI, dump
# to Json file

# Import the requests module
import requests, json

# Set this to False to only display the joke
IS_DEBUGGING = False

# Url for single random safe jokes
URL = 'https://v2.jokeapi.dev/joke/Any?type=twopart&safe-mode'

def main():
    filename = 'json_jokes_file.json'

    # Use the requests.get() function
    # with the parameter of the JokeAPI url
    joke = requests.get(URL)

    # If the status_code is 200, successful connection and data
    if(joke.status_code == 200):

        # Convert the JSON data into a python dictionary with key value pairs
        joke_data = joke.json()

        try:
            with open(filename, 'w') as file:
                # Dump the python dictionary to file
                json.dump(joke_data, file)
                print("Joke saved to a file")
        except:
            print('json data was not dumped to a file')

        # Used to debug process
        if(IS_DEBUGGING == True):
            # Display the status code
            print(f'\nThe status code for this APU request is {joke.status_code}')

            # Display the raw JSON data from by Open Notify API
            print('The raw data from the JokeAPI:')
            print(joke.text)

            # Display the Python Dictionary
            print('\nThe JSON data converted to a Python dictionary')
            print(joke_data)

        # Print the data using the dictionary created from the API JSON data
        print('\nTime for  a joke')
        print(f'{joke_data["setup"]}')
        print(f'{joke_data["delivery"]}')

    else:
        print('JokeAPI unavailable')



# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
