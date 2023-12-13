from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_policies_list():
    # Set up the WebDriver
    driver = webdriver.Chrome()

    try:
        # Open EPAM.com
        driver.get("https://www.epam.com")

        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the policies list to be visible
        policies_list = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-policy-section"))
        )

        # Extract policy items
        policy_items = policies_list.find_elements(By.CSS_SELECTOR, "ul li")

        # Expected policy items
        expected_policies = [
            "INVESTORS",
            "COOKIE POLICY",
            "OPEN SOURCE",
            "APPLICANT PRIVACY NOTICE",
            "PRIVACY POLICY",
            "WEB ACCESSIBILITY"
        ]

        # Check if all expected policies are present
        for expected_policy in expected_policies:
            assert any(expected_policy.lower() in policy.text.lower() for policy in policy_items), f"Expected policy '{expected_policy}' not found."

    finally:
        # Close the browser after the test
        driver.quit()

# Run the test
test_check_policies_list()
