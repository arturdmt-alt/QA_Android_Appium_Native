# Android Native Automation Testing with Appium

[![Android Tests](https://github.com/arturdmt-alt/QA_Android_Appium_Native/actions/workflows/tests.yml/badge.svg)](https://github.com/arturdmt-alt/QA_Android_Appium_Native/actions/workflows/tests.yml)

Automated testing framework for Android native applications using Appium 2.x, Python, and pytest.

---

## Project Overview

Automated testing suite for the Android Settings app. The tests use Activity-based navigation instead of UI element locators, making them stable across different Android versions and languages. This approach demonstrates real-world problem-solving in mobile test automation.

---

## Technology Stack

* Python 3.11
* Appium 2.x with UIAutomator2 driver
* Pytest testing framework
* Selenium 4.x WebDriver bindings
* Android Emulator (API 33 - Android 13)

---

## Test Coverage

The test suite currently covers:

* Settings app launch verification
* Date and Time settings navigation
* Backup settings navigation

All tests use Android Activity intents for reliable, UI-independent automation.

---

## Setup Instructions

**Prerequisites:**

* Python 3.11 or higher
* Node.js 18+ and npm
* Android Studio with an emulator configured
* Java JDK 11+

**Installation Steps:**

1. Clone the repository:
```bash
git clone https://github.com/arturdmt-alt/QA_Android_Appium_Native.git
cd QA_Android_Appium_Native
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install Appium globally:
```bash
npm install -g appium
appium driver install uiautomator2
```

5. Start your Android emulator from Android Studio (Pixel 5 or similar device)

6. Start Appium server in a separate terminal:
```bash
appium
```

---

## Running Tests

Run all tests with verbose output:
```bash
pytest tests/test_android_settings.py -v -s
```

Run a specific test:
```bash
pytest tests/test_android_settings.py::TestAndroidSettings::test_open_date_and_time -v
```

---

## Test Results

Sample output from successful test run:
```
tests/test_android_settings.py::TestAndroidSettings::test_settings_opens PASSED
tests/test_android_settings.py::TestAndroidSettings::test_open_date_and_time PASSED
tests/test_android_settings.py::TestAndroidSettings::test_open_backup PASSED

3 passed in 28.71s
```

---

## Project Structure
```
QA_Android_Appium_Native/
├── tests/
│   └── test_android_settings.py     # Main test suite
├── utils/
│   └── appium_config.py             # Appium driver configuration
├── conftest.py                      # Pytest fixtures
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## Technical Approach

### Why Activity-Based Navigation

The initial approach used UI element locators like XPath and text matching, but this ran into several issues:

* Text elements vary by device language
* UI structure changes between Android versions
* Element visibility depends on scroll position and app state

The solution was to use Android Activity intents to directly launch specific Settings screens:
```python
driver.execute_script(
    "mobile: startActivity",
    {"component": "com.android.settings/com.android.settings.Settings$DateTimeSettingsActivity"}
)
```

**This approach offers several advantages:**

* Works regardless of device language
* Stable across Android 12, 13, and 14
* No dependency on UI element visibility
* Faster test execution (no scrolling or element waiting)

---

## Challenges and Solutions

### Challenge 1: Settings App Opens to Unpredictable Pages

**Problem:** Android Settings doesn't consistently open to the main screen. Depending on device state, it might open to System settings, Date and Time, last visited page, or Network settings.

**Initial Approach:** Tried using `driver.back()` to navigate to the root screen, but this often closed the app entirely instead of going up one navigation level.

**Solution:** Switched to Activity-based navigation using `execute_script` with the `mobile: startActivity` command, which bypasses the UI entirely and opens the exact screen needed.

---

### Challenge 2: Element Locators Constantly Breaking

**Problem:** UI element locators failed across different test runs:

* XPath selectors like `//*[@text='Date & time']` worked inconsistently
* Element IDs like `com.android.settings:id/title` didn't exist on all screens
* Text-based searches failed when Settings opened to different initial pages

**Attempts Made:**
* XPath with exact text match - Failed because elements weren't always visible
* UiScrollable with textContains - Encountered syntax errors and timeout issues
* Resource ID selectors - Not stable across different Settings fragments

**Solution:** Use Android Activity intents to launch specific Settings screens directly. This completely avoids UI element dependencies and works reliably across test runs.

---

### Challenge 3: UiScrollable Syntax Issues

**Problem:** When attempting to use UiAutomator's UiScrollable for finding elements, the selector failed with an `InvalidSelectorException` error stating "Expected '.' at position 51".

**Cause:** Multi-line strings with line breaks in the UiScrollable query confused the UiAutomator expression parser.

**Learning:** While UiScrollable can work with proper single-line syntax, this entire UI-based approach was ultimately abandoned in favor of Activity-based navigation which proved significantly more reliable for system apps.

---

### Challenge 4: Emulator Connectivity Issues

**Problem:** Android emulator showed as "offline" in `adb devices` output, preventing test execution.

**Cause:** Previous emulator process didn't terminate properly, leaving a zombie process running in the background.

**Solution:**
* Killed the hung `qemu-system-x86_64.exe` process via Task Manager
* Verified clean state with `adb devices` command
* Restarted emulator fresh from Android Studio

This became part of the standard troubleshooting process when tests wouldn't connect.

---

### Challenge 5: Appium Server PATH Configuration

**Problem:** Node.js and Appium commands were not recognized in PowerShell after installation.

**Cause:** The Node.js installation path was not automatically added to the Windows PATH environment variable.

**Solution:** Manually added `C:\Program Files\nodejs` to the User PATH variable in Windows system settings. Verified the fix by running `node --version` and `npm --version` to confirm both commands were recognized.

---

## Key Technical Insights

### Activity-Based vs UI-Based Automation

For system apps like Android Settings, Activity-based navigation is superior to UI-based automation for several reasons:

**UI automation challenges with system apps:**
* UI structure varies significantly across Android versions
* Dynamic layouts change based on user state and preferences
* Multiple entry points and navigation patterns exist
* No guaranteed element IDs or stable view hierarchy

**Activity-based approach advantages:**
* Works regardless of current UI state
* Independent of device language settings
* Remains stable across Android 11, 12, 13, and 14
* Executes faster without needing to scroll or wait for elements
* More suitable for CI/CD pipelines where consistency is critical


---

## Author

**Artur Dmytriyev**  
QA Automation Engineer

* GitHub: [github.com/arturdmt-alt](https://github.com/arturdmt-alt)
* LinkedIn: [linkedin.com/in/arturdmytriyev](https://www.linkedin.com/in/arturdmytriyev)
