# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get('https://www.indeed.com')
# driver.maximize_window()

# # Enter job title
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys("qa tester")
# time.sleep(7)

# # Enter location
# location = driver.find_element(By.NAME, 'l')
# location.clear()
# location.send_keys("delhi")
# time.sleep(3)



# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")

# # Save screenshot to the current folder
# driver.save_screenshot("google_screenshot.png")

# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import sys
# import os
# import pyautogui



# options = Options()
# options.add_argument("--disable-gpu")


# driver = webdriver.Chrome(options=options)

# driver.get("https://www.iexindia.com/market-data/day-ahead-market/market-snapshot")

# driver.maximize_window()

# market_data = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/nav[1]/div/div[2]/button")
# market_data.click()
# dam = driver.find_element(By.XPATH, "//a[@href='/market-data/day-ahead-market/market-snapshot']")
# dam.click()
# time.sleep(3)

# wait = WebDriverWait(driver, 20)
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-responsive")))

# # Locate the table
# table = driver.find_element(By.CLASS_NAME, "table-responsive")
# rows = table.find_elements(By.TAG_NAME, "tr")

# # Print all table data
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME, "td")
#     if cells:
#         data = [cell.text for cell in cells]
#         print(data)

# # Close the browser
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# options = Options()
# options.add_argument("--disable-gpu")
# options.add_argument("--start-maximized")

# driver = webdriver.Chrome(options=options)

# # Go to the IEX DAM snapshot page directly
# driver.get("https://www.iexindia.com/market-data/day-ahead-market/market-snapshot")

# # Wait for the table container to appear
# wait = WebDriverWait(driver, 30)
# try:
#     # This is the DIV that holds the table
#     table_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-responsive")))

#     # Now get the actual <tr> rows from inside the table
#     rows = table_container.find_elements(By.TAG_NAME, "tr")

#     for row in rows:
#         cells = row.find_elements(By.TAG_NAME, "td")
#         if cells:
#             data = [cell.text.strip() for cell in cells]
#             print(data)

# except Exception as e:
#     print("❌ Error loading table:", e)

# finally:
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
time.sleep(5)
upload = driver.find_element(By.ID,"file-upload")
# upload.send_keys("file")
upload.click()
driver.sleep(5)

