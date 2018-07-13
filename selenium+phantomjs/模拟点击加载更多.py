# coding=utf-8
from selenium import webdriver
import time

path = r'D:\学习资料\第三阶段python爬虫\day05\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://www.jianshu.com/'
browser.get(url)
time.sleep(3)
browser.save_screenshot('jianshu3.png')

js = 'document.body.scrollTop = 20000'
browser.execute_script(js)
time.sleep(2)
browser.save_screenshot('jainshu4.png')
# loadmore = browser.find_element_by_class_name('flow-list-placeholder-load-more')
# loadmore.click()
# time.sleep(3)
# browser.save_screenshot('jianshu3.png')

browser.quit()
print('截取结束')