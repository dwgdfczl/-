# coding=utf-8
import time
from selenium import webdriver
#创建谷歌浏览器对象,根据谷歌浏览器驱动创建对象。
#谷歌浏览器驱动路径为
path = r'C:\Users\zyw\Desktop\chromedriver.exe'
browser = webdriver.Chrome(path)

# print(browser)
# time.sleep(3)
url = 'http://www.baidu.com'
browser.get(url=url)
time.sleep(3)
#在发送请求成功之后再去查找指定的元素
my_input = browser.find_element_by_id('kw')
#往框里写字
my_input.send_keys('智联')

#找点击按钮
button = browser.find_element_by_id('su')
time.sleep(1)
button.click()
time.sleep(3)
browser.close()