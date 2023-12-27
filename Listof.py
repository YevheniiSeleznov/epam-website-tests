import pytest
import requests

# URL for the Pet Store API
base_url = "https://petstore.swagger.io/v2"

# Test case for creating a list of users
def test_create_list_of_users():
    # Define the endpoint for creating a list of users
    create_users_endpoint = f"{base_url}/user/createWithList"

    # Define a list of user data for the request body
    users_data = [
        {
            "id": 123,
            "username": "user1",
            "firstName": "User",
            "lastName": "One",
            "email": "user.one@example.com",
            "password": "password1",
            "phone": "123-456-7890",
            "userStatus": 1
        },
        {
            "id": 124,
            "username": "user2",
            "firstName": "User",
            "lastName": "Two",
            "email": "user.two@example.com",
            "password": "password2",
            "phone": "123-456-7891",
            "userStatus": 1
        }
        # Add more users as needed
    ]

    # Send a POST request to create a list of users
    response = requests.post(create_users_endpoint, json=users_data)

    # Assert that the status code is 200 (OK) indicating successful creation
    assert response.status_code == 200

    # Optionally, you can also assert other conditions based on the response content
    # For example, you may check if the response JSON contains details about the created users

    # Clean up (optional): Delete the created users after testing

if __name__ == "__main__":
    pytest.main([__file__])
