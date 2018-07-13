# coding=utf-8
import time
from selenium import webdriver
start = time.clock()
path = r'C:\Users\zyw\Desktop\chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'http://www.baidu.com'
browser.get(url)
time.sleep(2)
baidu_map = browser.find_element_by_name('tj_trmap')
baidu_map.click()
time.sleep(2)
map_input = browser.find_element_by_id('sole-input')
time.sleep(2)
map_input.send_keys('北京大学')
map_button = browser.find_element_by_id('search-button')
map_button.click()
time.sleep(3)
browser.close()
end = time.clock()
print(end-start)