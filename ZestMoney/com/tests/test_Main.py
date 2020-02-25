import pytest
from selenium.webdriver.common.keys import Keys

from com.main.AmzonHomePage import AmazonHomepage
from com.utilites.UtilityClass import Utilityclass
from com.main.FlipkartHomePage import Flipkarthomepage


class TestMain(Utilityclass):
    def test_execute(self):
        log= self.getLogger()
        flipkartprice = ''
        amzonprice = ''
        home = Flipkarthomepage(self.driver)
        home.getSearchBox().send_keys("iPhone XR (64GB) - yellow", Keys.ENTER)
        log.info('In flipkart searching an iPhone XR (64GB) - yellow ')
        self.driver.implicitly_wait(8)
        if home.clickPname().text == "Apple iPhone XR (Yellow, 64 GB)":
            flipkartprice = home.getPrice().text
        self.driver.get("https://www.amazon.in/")
        amzon = AmazonHomepage(self.driver)
        log.info('In amazon searching an iPhone XR (64GB) - yellow')
        amzon.getSearchBox().send_keys("iPhone XR (64GB) - yellow", Keys.ENTER)
        if amzon.clickPname().text == "Apple iPhone XR (Yellow, 64 GB)":
            amzonprice = amzon.getPrice()
        log.info("Filpkart price : " +flipkartprice)
        log.info("Amazon price : " + amzonprice)
        if flipkartprice < amzonprice :
            print("In Filpkart price is less an price is "+flipkartprice+"!!")
        else:
            print("In amazon price is less an price is " + amzonprice + "!!")
        log.info("Sucess !")
    #@pytest.fixture(params=['iPhone XR (64GB) - yellow','Apple iPhone XR (Yellow, 64 GB)'])
    #def dataload(self,request):
    #   return request.param