

#automating gmail

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()


driver.get("https://gmail.com")

loginemail=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
loginemail.send_keys('phoneaddicts007@gmail.com')
nextbtn=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span')
nextbtn.click()
loginpasswd=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
loginpasswd=send_keys('phoneaddicts')
loginpasswd.click()
gmail=driver.get('http://gmail.com')
