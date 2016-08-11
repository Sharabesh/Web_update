from selenium import webdriver

from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox()

def new():
	driver.get('https://accounts.craigslist.org/login/home?lang=en&cc=us')
	username = "allianceAutoGroupva@gmail.com"
	password = "Alliance2015"

	inputfield = driver.find_element_by_id("inputEmailHandle")
	inputfield.send_keys(username)


	passwordfield = driver.find_element_by_id("inputPassword")
	passwordfield.send_keys(password)


	login = driver.find_elements_by_xpath("//*[contains(text(), 'Log In')]")
	login[0].click()

	x = driver.page_source

	count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(">Active</small>"), x))

