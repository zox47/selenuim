from selenium import webdriver

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


import pause

driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get("https://back.egybest.co/vs-mirror/vidstream.online/f/VPbsLXnm3Y/?vclid=798f4319ae7ddee2884d37936e60620cbfe06a1c9a27e26089a1a085ooooxvPWoxoBoxygZRlzyrvPLVmoxBxoxpVyexoBoxwlWggtyVXDeEEygXurBByoxBxoxmvCoxoBoxIIIokyZVkyZlzVxZRzxoF")
    
driver.find_element_by_xpath('/html/body/div[1]/div/p/a[1]').click()
driver.switch_to.window(driver.window_handles[0])

driver.current_window_handle
pause.seconds(5)

rr = driver.page_source.encode("utf-8")
soup = BeautifulSoup(rr, 'html.parser')

div = soup.find("a", class_="bigbutton",  href=True)
driver.get(div['href'])
