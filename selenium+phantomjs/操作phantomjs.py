# coding=utf-8
import time
from selenium import webdriver
#找到驱动程序
path = r'D:\学习资料\第三阶段python爬虫\day05\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
#创建浏览器对象
browser = webdriver.PhantomJS(path)
url = 'http://www.zhihu.com'
browser.get(url=url)
time.sleep(2)
browser.save_screenshot('知乎.png')
browser.close()