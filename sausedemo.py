import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']"))).send_keys("standard_user")
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
dropdowm = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
dropdowm.select_by_visible_text("Price (low to high)")
wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[3]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']"))).click()
time.sleep(5)
