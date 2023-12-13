from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_wishlist():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to a product page (you can replace the URL with the desired product)
    driver.get("https://demowebshop.tricentis.com/build-your-own-expensive-computer")

    # Click the "Add to wishlist" button
    add_to_wishlist_button = driver.find_element(By.ID, "add-to-wishlist-button-19")
    add_to_wishlist_button.click()

    # Wait for the success message to appear (you might want to enhance this part based on the actual behavior of the website)
    time.sleep(3)

    # Verify that the success message is displayed
    success_message = driver.find_element(By.CSS_SELECTOR, ".bar-notification.success .content").text
    assert "The product has been added to your wishlist" in success_message, "Adding to wishlist failed"

    # Close the browser
    driver.quit()

# Run the test
test_add_to_wishlist()
