from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import pyautogui
import time

"""
Locators used in the code
"""
Bigcookie_id= "bigCookie"
web_version_button= "#mainBox > div:nth-child(2) > a:nth-child(2) > h3"
consent= "fc-button-label"
language_prompt= "promptContentChangeLanguage"
english_language= "langSelect-EN"
french_language= "langSelect-EN"
GotIt= "cc_btn cc_btn_accept_all"
PreviousSave= "close"
product_price_prefix= "productPrice"
product_prefix= "product"
cookies_id= "cookies"
options= "subButton"
change_language= "changeLanguageOption"
options_save= "option smallFancyButton"
Info= "logButton"
gotitlinktext= "Got it!"

class TestWebUi(unittest.TestCase):    
    def setUp(self):
        """
        Setup method to prepare the environment for testing:
        1. Initializes the WebDriver service with the path to the ChromeDriver executable.
        2. Launches the Chrome browser using the initialized service.
        3. Navigates to the Cookie Clicker game website (https://www.cookieclicker.com/).
        4. Maximizes the browser window for optimal viewing.
        5. Waits until the web version button is visible and then clicks on it to load the web version of the game.
        6. Locates and clicks on the consent button to acknowledge the site's terms.
        7. Waits until the "Got it!" link is visible and then clicks on it to confirm understanding of the site's policies.
        """        
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.cookieclicker.com/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, web_version_button))).click()
        self.conset_button= self.driver.find_element(By.CLASS_NAME,consent).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT,gotitlinktext))).click()
    
    def test1_english_button(self):
        """
        Test to verify functionality of the English language button:
        1. Clicks on the English language button to set the game's language to English.
        2. Waits for the "commentsText" element to become visible, indicating successful language change.
        3. Asserts that the displayed text matches the expected English text.
        4. Prints a confirmation message if the test passes.
        5. Quits the WebDriver session.
        """       
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, english_language))).click()
        self.driver.implicitly_wait(10)
        self.assertEqual((WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "commentsText")))).text, "You feel like making cookies. But nobody wants to eat your cookies.")
        if True:
            print("Test 1 - English button OK")    
        self.driver.quit()
       
    def test2_option_button(self):
        """
        Test to validate the functionality of the options button:
        1. Clicks on the English language button.
        2. Clicks on the options button to access game settings.
        3. Asserts that the menu element is visible, indicating successful access to game options.
        4. Prints a confirmation message if the test passes.
        5. Quits the WebDriver session.
        """        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, english_language))).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,options))).click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "menu"))))
        if True:
            print("Test 2 - Option button OK")
        self.driver.quit()
    
    def test3_change_language_button(self):
        """
        Test to ensure the functionality of the change language button:
        1. Clicks on the English language button.
        2. Clicks on the options button to access game settings.
        3. Clicks on the change language button to modify the game's language settings.
        4. Asserts that the prompt for language change is visible.
        5. Prints a confirmation message if the test passes.
        6. Quits the WebDriver session.
        """        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, english_language))).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,options))).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID,change_language))).click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "prompt"))))
        if True:
            print("Test 3 - Change Language button OK")
        self.driver.quit()
    
    def test4_game_functionality(self):
        """
        Test to evaluate the basic gameplay functionality:
        1. Clicks on the English language button.
        2. Enters a while loop to simulate continuous gameplay.
        3. Clicks on the big cookie to generate cookies.
        4. Retrieves the current count of cookies.
        5. Iterates through available products and purchases the first affordable product.
        6. Prints a confirmation message indicating successful execution of game functionality.
        7. Quits the WebDriver session.
        """        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, english_language))).click()
        

        while True:
            self.coockie = self.driver.find_element(By.ID, Bigcookie_id).click()
            self.coockie_count = int(self.driver.find_element(By.ID, cookies_id).text.split(" ")[0].replace(",", ""))

            for i in range(4):
                product_price = self.driver.find_element(By.ID, product_price_prefix + str(i)).text

                if not product_price.isdigit():
                    continue

                product_price = int(product_price.replace(",", ""))

                if self.coockie_count >= product_price:
                    self.product = self.driver.find_element(By.ID, product_prefix + str(i)).click()
                    break
               
            print("Test 4 - Game Functionality OK")           
            self.driver.quit()
            break    
            
    def tearDown(self):
        self.driver.quit()
        """
        1. Quits the WebDriver session to release system resources.
        """

if __name__ == '__main__':
    unittest.main()     
