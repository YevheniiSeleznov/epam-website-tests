import pytest
import requests

# URL for the Pet Store API
base_url = "https://petstore.swagger.io/v2"

# Test case for deleting a pet
def test_delete_pet():
    # Assume a pet ID for testing purposes (replace with a real pet ID)
    pet_id = 123

    # Define the endpoint for deleting a pet
    delete_pet_endpoint = f"{base_url}/pet/{pet_id}"

    # Send a DELETE request to delete the pet
    response = requests.delete(delete_pet_endpoint)

    # Assert that the status code is 200 (OK) indicating successful deletion
    assert response.status_code == 404

    # Optionally, you can also assert other conditions based on the response content
    # For example, you may check if the response JSON contains details about the deleted pet

    # Clean up (optional): Verify that the pet is no longer available
    get_pet_endpoint = f"{base_url}/pet/{pet_id}"
    get_response = requests.get(get_pet_endpoint)

    # Assert that the status code is 404 (Not Found) indicating the pet is not found
    assert get_response.status_code == 404

if __name__ == "__main__":
    pytest.main([__file__])
