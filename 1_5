import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_switch_location_list_by_region():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open EPAM.com
        driver.get("https://www.epam.com")

        # Scroll to the Our Locations part
        our_locations_link = driver.find_element(By.XPATH, "//a[contains(text(),'Our Locations')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", our_locations_link)

        # Wait for the regions to be visible
        regions = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".location-filter a"))
        )

        # Expected regions
        expected_regions = ["AMERICAS", "EMEA", "APAC"]

        # Check that 3 regions are presented
        assert len(regions) == len(expected_regions), f"Expected {len(expected_regions)} regions, but found {len(regions)}."

        # Check that each expected region is presented
        for expected_region in expected_regions:
            assert any(expected_region in region.text for region in regions), f"Expected region '{expected_region}' not found."

        # Switch to each region and verify the locations list
        for region in regions:
            region_name = region.text.strip()
            region.click()

            # Wait for the region switch to take effect
            time.sleep(2)  # Adjust the sleep time as needed

            # Check that the region's locations list is visible
            locations_list = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".location-list"))
            )

            # Check that the locations list is not empty
            assert locations_list.text.strip() != "", f"Locations list for region '{region_name}' is empty."

    finally:
        # Close the browser after the test
        driver.quit()

# Run the test
test_switch_location_list_by_region()
