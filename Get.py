import pytest
import requests

# URL for the Pet Store API
base_url = "https://petstore.swagger.io/v2"

# Test case for creating a user
def test_create_user():
    # Define the endpoint for creating a user
    endpoint = f"{base_url}/user"

    # Define user data for the request body (adjust based on Swagger documentation)
    user_data = {
        "id": 123,
        "username": "exampleUser",
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "password": "securePassword",
        "phone": "123-456-7890",
        "userStatus": 1
    }

    # Send a POST request to create a user
    response = requests.post(endpoint, json=user_data)

    # Assert that the status code is 200 (OK) indicating successful user creation
    assert response.status_code == 200

    # Optionally, you can also assert other conditions based on the response content
    # For example, you may check if the response JSON contains the created user details

    # Clean up (optional): Delete the user after testing (assuming you have a delete endpoint)

    # If there is a delete endpoint, you can uncomment and use the following code:
    # delete_endpoint = f"{base_url}/user/{user_data['username']}"
    # delete_response = requests.delete(delete_endpoint)
    # assert delete_response.status_code == 200

if __name__ == "__main__":
    pytest.main([__file__])
