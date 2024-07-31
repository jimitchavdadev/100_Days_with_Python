from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps Brave browser open
brave_options = webdriver.ChromeOptions()
brave_options.binary_location = "/usr/bin/brave-browser"
brave_options.add_experimental_option("detach", True)

# Initialize the Brave browser driver
driver = webdriver.Chrome(options=brave_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # Closes Brave
    # driver.quit()
    driver.close()
