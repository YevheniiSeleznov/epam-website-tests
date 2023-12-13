from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_cart():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to a product page (you can replace the URL with the desired product)
    driver.get("https://demowebshop.tricentis.com/build-your-own-expensive-computer")

    # Click the "Add to cart" button
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button-19")
    add_to_cart_button.click()

    # Wait for the success message to appear (you might want to enhance this part based on the actual behavior of the website)
    time.sleep(3)

    # Verify that the item is added to the cart
    cart_icon = driver.find_element(By.CSS_SELECTOR, ".cart-qty")
    assert int(cart_icon.text) > 0, "Adding to cart failed"

    # Navigate to the shopping cart page
    driver.get("https://demowebshop.tricentis.com/cart")

    # Verify that the added item is in the shopping cart
    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart .product")
    assert len(cart_items) > 0, "Item not found in the shopping cart"

    # Close the browser
    driver.quit()

# Run the test
test_add_to_cart()
