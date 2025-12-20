from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Locators
    DIGIT_1 = (AppiumBy.ID, "com.android.calculator2:id/digit_1")
    DIGIT_2 = (AppiumBy.ID, "com.android.calculator2:id/digit_2")
    DIGIT_5 = (AppiumBy.ID, "com.android.calculator2:id/digit_5")
    PLUS = (AppiumBy.ID, "com.android.calculator2:id/op_add")
    EQUALS = (AppiumBy.ID, "com.android.calculator2:id/eq")
    RESULT = (AppiumBy.ID, "com.android.calculator2:id/result")
    
    def click_digit(self, digit_locator):
        element = self.wait.until(EC.presence_of_element_located(digit_locator))
        element.click()
    
    def click_operation(self, operation_locator):
        element = self.wait.until(EC.presence_of_element_located(operation_locator))
        element.click()
    
    def get_result(self):
        result_element = self.wait.until(EC.presence_of_element_located(self.RESULT))
        return result_element.text
    