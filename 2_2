from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_user():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the login page
    driver.get("https://demowebshop.tricentis.com/login")

    # Fill in the login form
    driver.find_element(By.ID, "Email").send_keys("Yevhenii.doe@example.com")
    driver.find_element(By.ID, "Password").send_keys("Test@123")

    # Submit the login form
    driver.find_element(By.CSS_SELECTOR, 'input[value="Log in"]').click()

    # Wait for login to complete (you might want to enhance this part based on the actual behavior of the website)
    time.sleep(3)

    # Verify that login was successful
    welcome_message = driver.find_element(By.CLASS_NAME, "topic").text
    assert "Welcome, Yevhenii Doe!" in welcome_message

    # Close the browser
    driver.quit()

# Run the test
test_login_user()
