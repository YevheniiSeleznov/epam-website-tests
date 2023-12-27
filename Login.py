import pytest
import requests

# URL for the Pet Store API
base_url = "https://petstore.swagger.io/v2"

# Test case for logging in as a user
def test_login_as_user():
    # Create a user for testing purposes (you may use an existing user)
    create_user_endpoint = f"{base_url}/user"
    user_data = {
        "id": 123,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test.user@example.com",
        "password": "testPassword",
        "phone": "123-456-7890",
        "userStatus": 1
    }
    requests.post(create_user_endpoint, json=user_data)

    # Define the endpoint for user login
    login_endpoint = f"{base_url}/user/login"

    # Define login credentials
    login_credentials = {
        "username": user_data["username"],
        "password": user_data["password"]
    }

    # Send a GET request to log in as the user
    response = requests.get(login_endpoint, params=login_credentials)

    # Assert that the status code is 200 (OK) indicating successful login
    assert response.status_code == 200

    # Optionally, you can also assert other conditions based on the response content
    # For example, you may check if the response JSON contains a token or session information

    # Clean up (optional): Delete the test user after testing
    delete_endpoint = f"{base_url}/user/{user_data['username']}"
    delete_response = requests.delete(delete_endpoint)
    assert delete_response.status_code == 200

if __name__ == "__main__":
    pytest.main([__file__])
