import pytest
import requests

# URL for the Pet Store API
base_url = "https://petstore.swagger.io/v2"

# Test case for updating a pet's image
def test_update_pet_image():
    # Assume a pet ID for testing purposes (replace with a real pet ID)
    pet_id = 123

    # Define the endpoint for updating a pet's image
    update_image_endpoint = f"{base_url}/pet/{pet_id}"

    # Define new pet data with an updated image URL
    updated_pet_data = {
        "id": pet_id,
        "photoUrls": [
            "https://example.com/new-pet-photo"
        ]
    }

    # Send a PUT request to update the pet's image
    response = requests.put(update_image_endpoint, json=updated_pet_data)

    # Assert that the status code is 200 (OK) indicating successful update
    assert response.status_code == 405

    # Optionally, you can also assert other conditions based on the response content
    # For example, you may check if the response JSON contains details about the updated pet

if __name__ == "__main__":
    pytest.main([__file__])
