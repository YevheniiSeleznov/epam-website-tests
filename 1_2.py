from selenium import webdriver
from selenium.webdriver.common.by import By


def test_switch_theme():
    # Start Chrome browser
    driver = webdriver.Chrome()

    # Open EPAM website
    driver.get("https://www.epam.com")

    # Check initial theme
    initial_theme = get_theme(driver)
    print(f"Initial theme: {initial_theme}")

    # Click the theme toggle
    toggle_button = driver.find_element(by=By.CSS_SELECTOR, value="[data-testid='theme-switch']")
    toggle_button.click()

    # Wait for theme change
    driver.implicitly_wait(5)

    # Check new theme
    new_theme = get_theme(driver)
    print(f"New theme: {new_theme}")

    # Verify theme switched
    assert new_theme != initial_theme, "Theme did not switch!"

    # Close the browser
    driver.quit()


def get_theme(driver):
    # Get the class attribute of the body element
    body_class = driver.find_element(by=By.TAG_NAME, value="body").get_attribute("class")

    # Check for the presence of "dark-theme" class
    if "dark-theme" in body_class:
        return "Dark"
    else:
        return "Light"


# Run the test
test_switch_theme()