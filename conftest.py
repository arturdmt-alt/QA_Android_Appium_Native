import pytest
from utils.appium_config import AppiumConfig

@pytest.fixture(scope='function')
def driver():
    """Setup and teardown Appium driver for each test"""
    appium_driver = AppiumConfig.get_driver()
    
    yield appium_driver
    
    appium_driver.quit()
    