import allure
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Util.readConfig import readConfig
from Util.generateLogs import LogGenerator
from pytest_html_reporter import attach
from allure_commons.types import AttachmentType

''''
https://pypi.org/project/pytest-html/
pytest -v -s --html-report=../ReportS/report.html

'''

class TestDemo:
    logger = LogGenerator.loggen()

    @pytest.fixture()
    def prestep(self):
        self.logger.info("-------Prestep----------")
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(readConfig.getConfig(self,"commoninfo","baseURL"))

        self.logger.info("-------Login----------")
        lp = LoginPage(self.driver)
        lp.enterUserName("standard_user")
        lp.enterPassword("secret_sauce")
        lp.clickLogin()


    def test_1_homepage(self,prestep):
        self.logger.info("-------Verify Logo----------")
        hp = HomePage(self.driver)
        if hp.verifyLogo() == True:
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/logo.png")
            attach(data = self.driver.get_screenshot_as_png())
            assert False
    def test_2_sortdropdown(self,prestep):
        self.logger.info("-------High to Low----------")
        hp = HomePage(self.driver)
        hp.selectFilterDropdown("Price (high to low)")
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



