from selenium.webdriver.common.by import By


class AmazonHomepage:
    def __init__(self, driver):
        self.driver = driver
    searchBox = (By.ID, 'twotabsearchtextbox')
    searchbutton = (By.CLASS_NAME, 'vh79eN')
    price = (By.CSS_SELECTOR, ".a-price-whole")
    iphone = (By.XPATH, "//span[contains(text(),'Apple iPhone XR (64GB) - Yellow')]")

    def getSearchBox(self):
        return self.driver.find_element(*AmazonHomepage.searchBox)

    def clickPname(self):
        return self.driver.find_element(*AmazonHomepage.iphone)

    def getPrice(self):
        return self.driver.find_element(*AmazonHomepage.price)