from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')

# elems = browser.find_elements(By.CSS_SELECTOR, 'p')
# print(elems[0].text)
# print(elems[0].get_property('innerHTML'))

# link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
# link_elem.click()

user_elem = browser.find_element(By.ID, 'login_user')
user_elem.send_keys('your_real_username_here')
password_elem = browser.find_element(By.ID, 'login_pass')
password_elem.send_keys('your_real_password_here')
password_elem.submit()