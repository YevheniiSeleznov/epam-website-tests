from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_change_items_per_page():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to a product category (you can replace the URL with the desired category)
    driver.get("https://demowebshop.tricentis.com/computers")

    # Select the items per page dropdown element
    items_per_page_dropdown = driver.find_element(By.NAME, "products-pagesize")

    # Define the options for the number of items per page
    items_per_page_options = ["3", "6", "9", "12"]

    for option in items_per_page_options:
        # Select each option from the dropdown
        items_per_page_dropdown.click()
        driver.find_element(By.XPATH, f"//option[text()='{option}']").click()

        # Wait for the page to load (you might want to enhance this part based on the actual behavior of the website)
        time.sleep(3)

        # Verify that the correct number of items is displayed on the page
        displayed_items = driver.find_elements(By.CSS_SELECTOR, ".product-item")
        assert len(displayed_items) == int(option), f"Number of displayed items does not match selected option: {option}"

    # Close the browser
    driver.quit()

# Run the test
test_change_items_per_page()
