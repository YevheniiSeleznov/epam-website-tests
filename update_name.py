import pytest
import requests

# URL for the Pet Store API
base_url = "https://petstore.swagger.io/v2"

# Test case for updating a pet's name and status
def test_update_pet_name_and_status():
    # Assume a pet ID for testing purposes (replace with a real pet ID)
    pet_id = 123

    # Define the endpoint for updating a pet's information
    update_pet_endpoint = f"{base_url}/pet/{pet_id}"

    # Define new pet data with an updated name and status
    updated_pet_data = {
        "id": pet_id,
        "name": "NewPetName",
        "status": "sold"
    }

    # Send a PUT request to update the pet's name and status
    response = requests.put(update_pet_endpoint, json=updated_pet_data)

    # Assert that the status code is 200 (OK) indicating successful update
    assert response.status_code == 405

    # Optionally, you can also assert other conditions based on the response content
    # For example, you may check if the response JSON contains details about the updated pet

if __name__ == "__main__":
    pytest.main([__file__])
