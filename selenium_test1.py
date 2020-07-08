from selenium import webdriver
import chromedriver_binary
import time

#ブラウザを開く
driver = webdriver.Chrome()
driver.get("https://a-force.biz/index.aspx#!")

#チャットボットをクリック
chat = driver.find_element_by_id("button-area")
chat.click()

#フレーム切り替え
driver.switch_to.frame(driver.find_element_by_id("effect"))

#質問内容を入力
tweet = driver.find_element_by_id("tweet")
tweet.send_keys("採用情報")
time.sleep(3)

#送信ボタンをクリック
driver.find_element_by_id("send_btn").click()
time.sleep(3)

#回答を取得・出力
elements = driver.find_elements_by_class_name("alert.alert-warning")[1].text
print(elements)
time.sleep(5)

#ブラウザを閉じる
driver.close()
