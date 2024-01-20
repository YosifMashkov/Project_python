from api_call_and_DB_save import create_database, get_random_user
import json
import requests
import pytest

def automation_test():
    # Get a random user
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    user = data['results'][0]

    # Check if the keys exist in the response
    assert 'name' in user
    assert 'email' in user
    assert 'location' in user