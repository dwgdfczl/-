# coding=utf-8
import time
from selenium import webdriver

start = time.clock()
path = r'D:\学习资料\第三阶段python爬虫\day05\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://www.zhihu.com/'
browser.get(url=url)
time.sleep(3)
print('3.png截取中，请耐心等待。。')
browser.save_screenshot('3.png')
print('3.png截取完毕')
#模拟滚动条滚动到底部
#执行依据JS代码
js = 'document.body.scrollTop = 2000'
browser.execute_script(js)
time.sleep(3)
print('4.png截取中，请耐心等待。。')
browser.save_screenshot('4.png')
print('4.png截取完毕')
browser.quit()
end = time.clock()

cou = end-start
print('截图完成！用时{}'.format(cou))