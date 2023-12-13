from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_verify_computers_subgroups():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the Computers category
    driver.get("https://demowebshop.tricentis.com/computers")

    # Find and click on the 'Computers' category
    driver.find_element(By.LINK_TEXT, "Computers").click()

    # Wait for the page to load (you might want to enhance this part based on the actual behavior of the website)
    time.sleep(3)

    # Get the names of sub-groups under 'Computers'
    subgroups = driver.find_elements(By.CSS_SELECTOR, ".item-box h2 a")

    # Verify that there are 3 sub-groups with correct names
    expected_subgroup_names = ["Desktops", "Notebooks", "Accessories"]

    assert len(subgroups) == len(expected_subgroup_names), "Number of sub-groups doesn't match"

    for subgroup, expected_name in zip(subgroups, expected_subgroup_names):
        assert subgroup.text == expected_name, f"Unexpected sub-group name: {subgroup.text}"

    # Close the browser
    driver.quit()

# Run the test
test_verify_computers_subgroups()
