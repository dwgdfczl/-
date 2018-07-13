# coding=utf-8
import time
from selenium import webdriver

path = r'D:\学习资料\第三阶段python爬虫\day05\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://www.zhihu.com/'
browser.get(url)
time.sleep(3)
js = 'document.body.scollTop = 20000'
browser.execute_script(js)
time.sleep(5)
browser.save_screenshot('zhihu5.png')
browser.quit()