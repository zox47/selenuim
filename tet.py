from selenium import webdriver

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

from selenium.webdriver.chrome.options import Options

import pause

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4")
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
