from selenium.webdriver.common.by import By


class Flipkarthomepage:
    def __init__(self, driver):
        self.driver = driver
    searchBox = (By.CLASS_NAME, 'LM6RPg')
    searchbutton = (By.CLASS_NAME, 'vh79eN')
    price = (By.CSS_SELECTOR, "._1vC4OE")
    iphone = (By.XPATH, "//div[contains(text(),'Apple iPhone XR (Yellow, 64 GB)')]")

    def getSearchBox(self):
        return self.driver.find_element(*Flipkarthomepage.searchBox)

    def clickPname(self):
        return self.driver.find_element(*Flipkarthomepage.iphone)

    def getPrice(self):
        return self.driver.find_element(*Flipkarthomepage.price)