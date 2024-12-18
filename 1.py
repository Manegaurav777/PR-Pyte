from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
driver.maximize_window()
driver.switch_to.frame("globalSqa")
time.sleep(4)
driver.find_element(By.ID,"mobile_menu_toggler").click()
time.sleep(3)
print("success")
driver.find_element(By.XPATH,'//*[@id="mobile_menu"]/ul/li[1]/a').click()
driver.switch_to.parent_frame()
time.sleep(3)
print("success")
print("Task cmompleted successfully")
driver.quit()
