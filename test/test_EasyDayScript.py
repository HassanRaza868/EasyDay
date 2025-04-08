from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = AppiumOptions()
options.load_capabilities({
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "10",
    "appium:deviceName": "PL2GAR9841607456",
    "appium:app": "D:\\Awais Sarwar\\Mubashir\\EasydayAppBulb.apk",
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "enforceXPath1": True  # Enforces XPath 1.0

})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 20)  # 10 seconds timeout

def swipe_to_bottom():
    window_size = driver.get_window_size()
    width = window_size['width']
    height = window_size['height']

    start_x = width // 2
    start_y = int(height * 0.8)  # Start point (bottom 80% of screen)
    end_y = int(height * 0.2)    # End point (top 20% of screen)

    while True:
        previous_page_source = driver.page_source  # Save current page source
        driver.swipe(start_x, start_y, start_x, end_y, 800)  # Swipe with 800ms duration
        time.sleep(1)  # Short delay to allow UI to update
        
        # Break if no new content appears (end of page detected)
        if driver.page_source == previous_page_source:
            print("Reached the bottom of the page.")
            break

def Login_Easyday():
    print("Test Case # 1: Error should be shown if email format is invalid")
    LoginButton = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Login")))
    LoginButton.click()
    
    EnterEmail = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")))
    EnterEmail.click()
    EnterEmail.send_keys("hnlive")

    # Close the keyboard
    driver.hide_keyboard()

    EnterPassword = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")))
    EnterPassword.click()
    EnterPassword.send_keys("Hypernym@123")

    # Close the keyboard
    driver.hide_keyboard()

    LoginButton = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Login")))
    LoginButton.click()

    # Verify if the error message "Email format is not correct." appears
    try:
        # Wait for the error message to appear
        error_message = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Email is not valid")))

        # If the error message is found, pass the test case
        print("Test Case Passed: Error is shown if email format is invalid")
        
    except TimeoutException:
        # If the error message is not found within the timeout, fail the test case
        print("Test Case Failed: No error message displayed.")


def Login_Easyday1():
    print("Test Case # 2: User should not be able to login using invalid email/password")

    EnterEmail = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")))
    EnterEmail.click()
    EnterEmail.clear()
    EnterEmail.send_keys("easydaystag@yopmail.com")

    # Close the keyboard
    driver.hide_keyboard()

    EnterPassword = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")))
    EnterPassword.click()
    EnterPassword.clear()
    EnterPassword.send_keys("Hypernym@1234")

    # Close the keyboard
    driver.hide_keyboard()

    LoginButton = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Login")))
    LoginButton.click()


# Verify if the error message "Email format is not correct." appears
    try:
        # Wait for the error message to appear
        error_message = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Invalid email/password")))

        # If the error message is found, pass the test case
        print("Test Case Passed: Error message displayed for invalid login.")
        
    except TimeoutException:
        # If the error message is not found within the timeout, fail the test case
        print("Test Case Failed: No error message displayed for invalid login.")

def Login_Easyday2():
    print("Test Case # 3: Test Case # 3: User should be able to login using correct email/password")

    EnterEmail = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")))
    EnterEmail.click()
    EnterEmail.clear()
    EnterEmail.send_keys("easydaystag@yopmail.com")

    # Close the keyboard
    driver.hide_keyboard()

    EnterPassword = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")))
    EnterPassword.click()
    EnterPassword.clear()
    EnterPassword.send_keys("Aa123456@")

    # Close the keyboard
    driver.hide_keyboard()

    LoginButton = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Login")))
    LoginButton.click()

# Verify if the error message "Email format is not correct." appears
    try:
        # Wait for the error message to appear
        error_message = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Welcome to your everyday App to easily manage your smart devices")))

        # If the error message is found, pass the test case
        print("Test Case Passed: Login was successful with correct credentials.")
        
    except TimeoutException:
        # If the error message is not found within the timeout, fail the test case
        print("Test Case Failed: Unable to login using correct credentials.")

def deviceaddition():

    Adddnewdevicebutton = wait.until(EC.presence_of_element_located((
        AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"Add New Device\nScan or set Manually\"]/android.widget.ImageView")
    ))
    Adddnewdevicebutton.click()

    CatTrackerbutton = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Cat Tracker")))
    CatTrackerbutton.click()

    CatTrackeraddmanually = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Add Manually")))
    CatTrackeraddmanually.click()

    EnterPetName = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(0)")))
    EnterPetName.click()
    EnterPetName.send_keys("Cat Cat")

    # Close the keyboard
    driver.hide_keyboard()

    EnterDeviceID = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(1)")))
    EnterDeviceID.click()
    EnterDeviceID.send_keys("661122334411222")

    # Close the keyboard
    driver.hide_keyboard()
    
    Petkind = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(2)")))
    Petkind.click()
    Petkind.send_keys("Dasiy")

    # Close the keyboard
    driver.hide_keyboard()

    PetBreed = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(3)")))
    PetBreed.click()
    PetBreed.send_keys("sd")
    
    # Close the keyboard
    driver.hide_keyboard()

    PetWeight = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(4)")))
    PetWeight.click()
#    PetWeight.send_keys("2")

    PetWeight = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.EditText\").instance(3)")))
    PetWeight.click()
    PetWeight.send_keys("999")

    
    # Close the keyboard
    driver.hide_keyboard()


    time.sleep(5)
    

    driver.hide_keyboard()

    time.sleep(5)
    
    swipe_to_bottom()

    time.sleep(5)

    PressCountinue = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Continue")))
    PressCountinue.click()

    time.sleep(5)

    swipe_to_bottom()

    Savedevicebutton = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Save")))
    Savedevicebutton.click()

    try:
        error_message = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "pet has been added successfully")))
        print("Test Case Failed: Pet not added")

    except TimeoutException:
        print("Test Case Passed: successful")

def add_geo_zone():
    try:
        print("Adding Geo Zone...")

        # Click the main menu or navigation item
        threedotsnavigation = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, 
            "//android.widget.FrameLayout[@resource-id='android:id/content']"
            "/android.widget.FrameLayout/android.widget.FrameLayout"
            "/android.view.View/android.view.View/android.view.View"
            "/android.view.View/android.view.View[1]/android.view.View"
            "/android.widget.ImageView/android.widget.ImageView"
        )))
        threedotsnavigation.click()

        # Click 'Geo Zones'
        clickgeozone = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Geo Zones")))
        clickgeozone.click()

        time.sleep(10)
        # Click 'Add a new Geo Zone'
        addnewgezone = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, 
            "//android.widget.ImageView[@content-desc='Add a new Geo Zone\nDraw your Required area on Map']/android.widget.ImageView"
        )))
        addnewgezone.click()
        
        # Enter Geo Zone radius
        #el4 = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        #el4.send_keys("0")

        # Close the keyboard
        #driver.hide_keyboard()

        # Click 'Next'
        time.sleep(10)
        nextbutton = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Next")))
        nextbutton.click()

        # Enter Geo Zone name
        zonename = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        zonename.click()
        zonename.send_keys("zone abc")

        # Close the keyboard
        driver.hide_keyboard()

        # Select Device
        selectdevices = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Select Your Devices")))
        selectdevices.click()

        # Choose 'Dog Tracker'
        devicesdropdown = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Dog tracker")))
        devicesdropdown.click()
        
        Savedevices = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Save")))
        Savedevices.click()

        swipe_to_bottom()

        Savezone = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Save")))
        Savezone.click()

        try:
            # Wait for the error message to appear
            error_message = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Geo Zone has been created successfully")))
        
            print("Test Case Passed: Geo Zone has been created successfully")

        except TimeoutException:
            print("Test Case Passed: Unable to add Geo Zone")
    
    except TimeoutException:
            print("Test Case Failed: Zone creation failed.")

def navigate_through_app():
    try:
        print("Starting App Navigation Test...")

        devicespage = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Devices")))
        devicespage.click()

        devicesname = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Dog one\ntest")))
        devicesname.click()
        
        navigationpage = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, 
            "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.widget.FrameLayout"
            "/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]"
            "/android.view.View/android.view.View[1]/android.widget.ImageView/android.widget.ImageView")))
        navigationpage.click()
        
        Notificationpage = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Notifications")))
        Notificationpage.click()

        Settingpage= wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Settings")))
        Settingpage.click()

        Homepage = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Home")))
        Homepage.click()

    except TimeoutException:
        print("Test Case Failed: Element not found during navigation.")
        

# Call the function to execute


try:
    Login_Easyday()
    Login_Easyday1()
    Login_Easyday2()
    deviceaddition()
    add_geo_zone()
    navigate_through_app()


finally:
    time.sleep(30)
    driver.quit()