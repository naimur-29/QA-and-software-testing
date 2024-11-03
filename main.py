from selenium import webdriver
from selenium.webdriver.common.by import By

def setup():
    driver = webdriver.Chrome()
    driver.get("https://nyaa.si/")
    return driver

def teardown(driver):
    driver.quit()

def test():
    driver = setup()
    
    title = driver.title
    print(title)
    
    lists = driver.find_elements(by=By.CSS_SELECTOR, value="tr > td:nth-child(2) > a")
    for ele in lists:
        print(ele.text)
    
    teardown(driver)
    
test()

    
