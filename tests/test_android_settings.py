import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAndroidSettings:
    """
    Android Settings Automation
    FINAL – Appium 2 + Python Client 3 compatible
    """

    def start_activity(self, driver, activity):
        """
        Start Android activity using Appium 2 / Python client 3 API
        """
        driver.execute_script(
            "mobile: startActivity",
            {
                "component": f"com.android.settings/{activity}"
            }
        )

    def test_settings_opens(self, driver):
        """
        Verify Settings app opens
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, "android.widget.TextView")
            )
        )
        print("\n✓ Settings app opened successfully")

    def test_open_date_and_time(self, driver):
        """
        Open Date & Time directly (NO UI, NO language, NO scroll)
        """
        self.start_activity(
            driver,
            "com.android.settings.Settings$DateTimeSettingsActivity"
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, "android.widget.Switch")
            )
        )
        print("\n✓ Date & Time opened via activity (stable)")

    def test_open_backup(self, driver):
        """
        Open Backup directly (stable across Android 13)
        """
        self.start_activity(
            driver,
            "com.android.settings.Settings$BackupSettingsActivity"
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, "android.widget.TextView")
            )
        )
        print("\n✓ Backup opened via activity (stable)")
