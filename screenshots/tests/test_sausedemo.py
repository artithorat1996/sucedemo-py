import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")
    driver.save_screenshot("screenshots/login_page.png")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    driver.save_screenshot("screenshots/after_login.png")

    dropdown = Select(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))))
    dropdown.select_by_visible_text("Price (low to high)")

    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[3]"))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']"))).click()

    time.sleep(2)  # For demo, prefer using wait conditions
