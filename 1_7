import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_epam_contact_form_validation():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the EPAM contact page
    driver.get("https://www.epam.com/about/who-we-are/contact")

    try:
        # Locate the form elements
        name_field = driver.find_element(By.NAME, "name")
        email_field = driver.find_element(By.NAME, "email")
        message_field = driver.find_element(By.NAME, "message")

        # Submit the form without entering any data
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()

        # Check for validation messages
        name_validation = name_field.find_element(By.XPATH, "../span[@class='error-message']").text
        email_validation = email_field.find_element(By.XPATH, "../span[@class='error-message']").text
        message_validation = message_field.find_element(By.XPATH, "../span[@class='error-message']").text

        # Assert that the required fields have validation messages
        assert "Required" in name_validation, f"Name field validation failed: {name_validation}"
        assert "Required" in email_validation, f"Email field validation failed: {email_validation}"
        assert "Required" in message_validation, f"Message field validation failed: {message_validation}"

    finally:
        # Close the browser
        driver.quit()

# Run the test
test_epam_contact_form_validation()
