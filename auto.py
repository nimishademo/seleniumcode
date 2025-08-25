# r.find_element(By.CLASS_NAME,'gNO89b')
# click_box.click()
# from selenium import webdriver
# from selenium.webdriver.common.by import Byfrom


# driver = webdriver.Chrome()


# url = "https://www.google.com"


# driver.get(url)

# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys("Selenium with Python")

# click_box = driver
# print('lllllllllllllllllllllllll')

# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()



# #driver.quit()

# url = "https://www.google.com"
# driver.get(url)
# #print('nnnn')

# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys("amazon")

# click_box = driver.find_element(By.CLASS_NAME,'gNO89b')
# click_box.click()

# print('lllllllllllllllllllllllll')

####################################################
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Launch Chrome
# driver = webdriver.Chrome()

# # Maximize window
# driver.maximize_window()

# # Open Google
# driver.get("https://www.google.com")

# # Search for "Selenium Python"
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Selenium Python")
# search_box.send_keys(Keys.RETURN)

# # Wait to see results
# time.sleep(3)

# # Close browser
# #driver.quit()

############################################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # 1. Launch Chrome
# driver = webdriver.Chrome()

# # 2. Open DuckDuckGo (not Google)
# driver.get("https://duckduckgo.com")

# # 3. Let it load
# time.sleep(2)

# # 4. Search "amazon"
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("amazon")
# search_box.send_keys(Keys.RETURN)

# print("Search submitted.")

#############################################3
###### Open duckduckgo and search “Selenium Python”

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


# driver = webdriver.Chrome()
# url = 'https://duckduckgo.com'

# driver.get(url)
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('Amazon')
# search_box.send_keys(Keys.RETURN)  # press Enter key
# time.sleep(10)

#############################################################
#############Google Search Automation

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get('https://duckduckgo.com')

# search = driver.find_element(By.NAME, 'q')
# search.send_keys("selenium with python")
# search.send_keys(Keys.RETURN)

# time.sleep(2)

# titles = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div[1]/div/form/input[1]")
# for i, title in enumerate(titles[:5], start=1):
#    print(f"{i}. {title.text}")
   
####################################################
######Login Form (Dummy Site)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time



# driver = webdriver.Chrome()
# driver.get("https://practicetestautomation.com/practice-test-login/")

# # 1️⃣ Locate by ID
# username = driver.find_element(By.ID, "username")
# username.send_keys("student")

# # 2️⃣ Locate by NAME
# password = driver.find_element(By.NAME, "password")
# password.send_keys("Password123")

# # 3️⃣ Locate by CLASS_NAME
# login_button = driver.find_element(By.CLASS_NAME, "btn")
# login_button.click()

# time.sleep(3)
# driver.quit()


################################################
#########Click a Link

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get("https://www.python.org/")

# driver.find_element(By.LINK_TEXT,"Downloads").click()
# time.sleep(2)

#######################################
####program for selecting dropdown

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# # Step 1: Launch browser
# driver = webdriver.Chrome()

# # Step 2: Open BlazeDemo site
# driver.get("https://blazedemo.com/")
# time.sleep(2)

# # Step 3: Locate "From port" dropdown using NAME
# from_port = Select(driver.find_element(By.NAME, "fromPort"))

# # Step 4: Select by visible text
# from_port.select_by_visible_text("Boston")

# # Optional: select "To port" dropdown as well
# to_port = Select(driver.find_element(By.NAME, "toPort"))
# to_port.select_by_visible_text("London")

# # Step 5: Wait and close
# time.sleep(3)
# driver.quit()

###########################################
######count element on page

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time

# driver = webdriver.Chrome()
# driver.get("https://www.w3schools.com/html/html_forms.asp")

# # 1️⃣ Get all input elements
# inputs = driver.find_elements(By.TAG_NAME, "input")

# print(f"Total input fields: {len(inputs)}")
# driver.quit()

################################################
#####login Automation interating web element

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get("https://practicetestautomation.com/practice-test-login/")

# driver.find_element(By.ID,"username").send_keys("student")
# driver.find_element(By.ID,"password").send_keys("Password123")
# driver.find_element(By.ID,"submit").click()

# time.sleep(2)
# msg = driver.find_element(By.TAG_NAME, "strong").text
# print("Message:", msg)

# driver.quit()

#########################################
################login automation using wait

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



# driver = webdriver.Chrome()
# driver.get("https://practicetestautomation.com/practice-test-login/")

# driver.find_element(By.ID,"username").send_keys("student")
# driver.find_element(By.ID,"password").send_keys("Password123")
# driver.find_element(By.ID,"submit").click()

# wait = WebDriverWait(driver, 10)
# welcome = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
# print("✅ Message:", welcome.text)

# driver.quit()


#############################
#####program for mouse hover

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
# driver.get("https://demo.guru99.com/test/drag_drop.html")

# hover_target = driver.find_element(By.LINK_TEXT, "BANK")

# actions = ActionChains(driver)
# actions.move_to_element(hover_target).perform()


#####################################
############mouse drag and drop


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
# driver.get("https://demo.guru99.com/test/drag_drop.html")

# source = driver.find_element(By.XPATH, "//a[text()=' BANK ']")
# target = driver.find_element(By.XPATH, "//ol[@id='bank']")

# actions = ActionChains(driver)
# actions.drag_and_drop(source, target).perform()

##########################################
########### right click

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

# button = driver.find_element(By.CSS_SELECTOR, ".context-menu-one")

# actions = ActionChains(driver)
# actions.context_click(button).perform()

##########################
#########program for doubleclick

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
# driver.get("https://testpages.herokuapp.com/styled/events/javascript-events.html")

# dbl_btn = driver.find_element(By.ID, "dblclick")

# actions = ActionChains(driver)
# actions.double_click(dbl_btn).perform()

##############################################
###########select drop down menu

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
# driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

# dropdown_element = driver.find_element(By.NAME, "dropdown")
# dropdown = Select(dropdown_element)
# dropdown.select_by_visible_text("Drop Down Item 5")


# submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
# submit_button.click()

################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
import pyautogui

target_folder = os.path.abspath("C:/Users/Nimisha/Desktop/Python1/doc")
os.makedirs(target_folder, exist_ok=True)

options = Options()
options.add_argument("--disable-gpu")


driver = webdriver.Chrome(options=options)

def download_dam_excel(url):

    try:

        driver.get(url)

        driver.maximize_window()

        # wait = WebDriverWait(driver, 10)

        market_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav[1]/div/div[2]/button")
        market_data.click()
        dam = driver.find_element(By.XPATH, "//a[@href='/market-data/day-ahead-market/market-snapshot']")
        dam.click()
        time.sleep(3)

        export = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/section/div[1]/div[1]/div[2]/div/button')
        export.click()

        time.sleep(5)

        download_excel = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/button[1]')

        download_excel.click()

        time.sleep(3)
        time.sleep(2)  # give it time to trigger download

        print("download started")
        pyautogui.hotkey("ctrl", "s")   # Open Save dialog
        time.sleep(2)

        pyautogui.typewrite(os.path.join(target_folder, "DAM_Market Snapshot.xlsx"))
        time.sleep(2)

        pyautogui.press("enter")
        time.sleep(5)

        print("File save simulation complete. Check: {target_folder}")


        # filename = "DAM_Market Snapshot.xlsx"
        # full_path = os.path.join(target_folder, filename)
        # print("Waiting for file to download...")
        # for i in range(60):  
        #     if os.path.exists(full_path):
        #         print(f"✅ File saved successfully to: {full_path}")
        #         break
        #     time.sleep(1)
        
        # else:

        #     print("❌ File was not downloaded in time.")

        
        time.sleep(20)
        print("++++")

    except Exception as err:
        msg = f"{type(err).__name__} was raised: {err} error on line" + format(sys.exc_info()[-1].tb_lineno)
        print ({'status': 'Failed', 'message':msg})

download_dam_excel("https://www.iexindia.com/")

##############################################################

def download_gdam_excel(url):

    try:

        driver.get(url)

        driver.maximize_window()

        # wait = WebDriverWait(driver, 10)

        market_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav[1]/div/div[2]/button")
        market_data.click()
        gdam = driver.find_element(By.XPATH, "//a[@href='/market-data/green-day-ahead-market/market-snapshot']")
        gdam.click()
        time.sleep(3)

        export = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/section/div[1]/div[1]/div[2]/div/button')
        export.click()

        # time.sleep(5)

        download_excel = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/button[1]')

        download_excel.click()

        time.sleep(20)
        print("++++")

    except Exception as err:
        msg = f"{type(err).__name__} was raised: {err} error on line" + format(sys.exc_info()[-1].tb_lineno)
        print ({'status': 'Failed', 'message':msg})


#download_gdam_excel("https://www.iexindia.com/")

##############################################################


def download_rtm_excel(url):

    try:

        driver.get(url)

        driver.maximize_window()

        # wait = WebDriverWait(driver, 10)

        market_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav[1]/div/div[2]/button")
        market_data.click()
        gdam = driver.find_element(By.XPATH, "//a[@href='/market-data/real-time-market/market-snapshot']")
        gdam.click()
        time.sleep(3)

        export = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/section/div[1]/div[1]/div[2]/div/button')
        export.click()

        # time.sleep(5)

        download_excel = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/button[1]')

        download_excel.click()

        time.sleep(20)
        print("++++")

    except Exception as err:
        msg = f"{type(err).__name__} was raised: {err} error on line" + format(sys.exc_info()[-1].tb_lineno)
        print ({'status': 'Failed', 'message':msg})


#download_rtm_excel("https://www.iexindia.com/")

##############################################################


