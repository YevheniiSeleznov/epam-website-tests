from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class EPAMWebsiteTest(unittest.TestCase):

    def setUp(self):
        # Set browser options for Chrome and Firefox
        chrome_options = webdriver.ChromeOptions()
        firefox_options = webdriver.FirefoxOptions()

        # Set headless mode (optional)
        chrome_options.add_argument("--headless")
        firefox_options.add_argument("--headless")

        # Initialize drivers
        self.drivers = {
            "Chrome": webdriver.Chrome(options=chrome_options),
            "Firefox": webdriver.Firefox(options=firefox_options),
        }

    def tearDown(self):
        # Close all browser windows
        for driver in self.drivers.values():
            driver.quit()

    def test_title(self):
        # Expected title
        expected_title = "EPAM | Software Engineering & Product Development Services"

        # Loop through each browser
        for browser, driver in self.drivers.items():
            # Open EPAM website
            driver.get("https://www.epam.com/")

            # Get actual title
            actual_title = driver.title

            # Assert title is correct
            self.assertEqual(actual_title, expected_title, f"Title mismatch on '{browser}' browser. Expected: '{expected_title}'. Actual: '{actual_title}'.")

if __name__ == "__main__":
    unittest.main()
