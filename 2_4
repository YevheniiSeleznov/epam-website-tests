from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_sort_items():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to a product category (you can replace the URL with the desired category)
    driver.get("https://demowebshop.tricentis.com/computers")

    # Select the sorting dropdown element
    sorting_dropdown = driver.find_element(By.ID, "products-orderby")

    # Define the sorting option
    sorting_option = "Price: High to Low"

    # Select the sorting option from the dropdown
    sorting_dropdown.click()
    driver.find_element(By.XPATH, f"//option[text()='{sorting_option}']").click()

    # Wait for the page to load (you might want to enhance this part based on the actual behavior of the website)
    time.sleep(3)

    # Verify that items are sorted correctly (you may need to adapt this verification based on your website's structure)
    sorted_items = driver.find_elements(By.CSS_SELECTOR, ".product-item .product-title")
    item_names = [item.text for item in sorted_items]

    # Check if items are sorted in the expected order
    assert item_names == sorted(item_names), f"Items are not sorted correctly for option: {sorting_option}"

    # Close the browser
    driver.quit()

# Run the test
test_sort_items()
