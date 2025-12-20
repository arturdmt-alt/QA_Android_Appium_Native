from appium import webdriver
from appium.options.android import UiAutomator2Options

class AppiumConfig:
    @staticmethod
    def get_driver():
        """Configure and return Appium driver for Android"""
        
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'
        options.automation_name = 'UiAutomator2'
        options.app_package = 'com.android.settings'
        options.app_activity = '.Settings'
        options.no_reset = True
        
        driver = webdriver.Remote(
            command_executor='http://localhost:4723',
            options=options
        )
        
        return driver
    