from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()
driver.get("https://a-force.biz/index.aspx#!")

chat = driver.find_element_by_id("button-area")
chat.click()

driver.switch_to.frame(driver.find_element_by_id("effect"))
tweet = driver.find_element_by_id("tweet")
tweet.send_keys("採用情報")
time.sleep(3)
driver.find_element_by_id("send_btn").click()

time.sleep(7)
driver.close()
