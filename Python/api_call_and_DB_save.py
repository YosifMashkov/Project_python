import requests
import sqlite3


def get_random_user():
    url = "https://randomuser.me/api/"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print relevant information
        user = data['results'][0]
        print("Name: {} {}".format(user['name']['first'], user['name']['last']))
        print("Email: {}".format(user['email']))
        print("Location: {}, {}, {}".format(user['location']['street'], user['location']['city'],
                                            user['location']['country']))

        # Insert the user data into the database
        insert_user_into_database(user)
    else:
        print("Failed to retrieve a random user. Status code: {}".format(response.status_code))

def create_database():
    # Connect to or create a SQLite3 database
    conn = sqlite3.connect('random_users.db')
    cursor = conn.cursor()

    # Create a table to store user data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            street TEXT,
            city TEXT,
            country TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def insert_user_into_database(user):
    # Connect to the SQLite database
    conn = sqlite3.connect('random_users.db')
    cursor = conn.cursor()

    # Insert user data into the 'users' table
    cursor.execute('''
        INSERT INTO users (first_name, last_name, email, street, city, country)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
    user['name']['first'], user['name']['last'], user['email'], user['location']['street'], user['location']['city'],
    user['location']['country']))

    # Commit changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Create the database and table if they don't exist
    create_database()

    # Get a random user and store the response in the database
    get_random_user()
