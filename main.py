from Python.api_call_and_DB_save import get_random_user, create_database
from Python.automation_test import automation_test

def main ():
    # Run the test.
    automation_test()

    # Create the DataBase.
    create_database()

    # Get random user and save the data in the DB.
    get_random_user()

