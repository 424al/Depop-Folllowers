import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


##USER INFORMATION
user = ('greenpie')
userpass = ('Rhs168909')
## URL TO ACCOUNT YOU WANT TO FOLLOW ITS FOLLOWERS
desired = ('https://www.depop.com/jrenner26/')

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.depop.com/login/?redirect=/');

print('Logging In')
####SIGN IN TO DEPOP
username = driver.find_element_by_name('username')
username.send_keys(user)

password = driver.find_element_by_name('password')
password.send_keys(userpass)
password.submit()
time.sleep(5)


#elem = driver.find_element_by_id('Logout')
#if elem.is_displayed():
	#	print('login successful')
# GOES TO DESIRED ACCOUNT'S PROFILE
driver.get(desired)
time.sleep(3)

# OPENS UP FOLLOWER LIST
driver.find_element_by_css_selector('[data-css-1k6tg18]').click()
time.sleep(5)

scrolls = driver.find_elements_by_css_selector('[data-css-63oe3q]').send_keys(Keys.END)

follow = driver.find_elements_by_css_selector('[class="sc-lhVmIH bTiqlv"]')

followtwo = driver.find_elements_by_css_selector('[class="sc-ksYbfQ lmeZvI"]')

followthree = driver.find_elements_by_name('follow')

for element in range(len(follow,)):
	follow[element].click()
	follow = driver.find_elements_by_css_selector('[class="sc-lhVmIH bTiqlv"]')

for element in range(len(followtwo,)):
	followtwo[element].click()
	followtwo = driver.find_elements_by_css_selector('[class="sc-ksYbfQ lmeZvI"]')

for element in range(len(followthree,)):
	followthree[element].click()
	followthree = driver.find_elements_by_name('follow')

	






