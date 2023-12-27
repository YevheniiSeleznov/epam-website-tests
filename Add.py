import pytest
import requests

# URL for the Pet Store API
base_url = "https://petstore.swagger.io/v2"

# Test case for adding a new pet
def test_add_new_pet():
    # Define the endpoint for adding a new pet
    add_pet_endpoint = f"{base_url}/pet"

    # Define pet data for the request body
    pet_data = {
        "id": 123,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": "TestPet",
        "photoUrls": [
            "https://example.com/pet-photo"
        ],
        "tags": [
            {
                "id": 1,
                "name": "tag1"
            }
        ],
        "status": "available"
    }

    # Send a POST request to add a new pet
    response = requests.post(add_pet_endpoint, json=pet_data)

    # Assert that the status code is 200 (OK) indicating successful addition
    assert response.status_code == 200

    # Optionally, you can also assert other conditions based on the response content
    # For example, you may check if the response JSON contains details about the added pet

    # Clean up (optional): Delete the added pet after testing
    delete_pet_endpoint = f"{base_url}/pet/{pet_data['id']}"
    delete_response = requests.delete(delete_pet_endpoint)
    assert delete_response.status_code == 200

if __name__ == "__main__":
    pytest.main([__file__])
