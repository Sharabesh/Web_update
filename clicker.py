"""
Installation Instructions

	1) Install python
	2) Install Splinter 
		Mac--> pip install splinter 
		Source code --> Make sure git is install 
			git clone git://github.com/cobrateam/splinter.git
			$ cd splinter
			$ [sudo] python setup.py install
	3) Install Chrome Driver
		pip install selenium 
	4) Install Homebrew
		Mac) 
			http://brew.sh/
				/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
			brew install chromedriver

		PC) 
			https://code.google.com/p/chromedriver/downloads/list
			Add the .exe file to the path 
				Environment variables
				How to manage environment variables in Windows XP


Install on PC 

	Make sure Sublime Text, Python, Splinter (with Git) are installed; 
	No need to install chromedriver --> make sure firefox is installed 

	Use Windows Task Scheduler to setup python file on login 
			Triggers--> At log on 
			Actions
				Start a Program 
					Program/Script--> Find where python 3.5 is installed on the computer
					Add Arguments--> Clicker.py 
					Start in --> Copy working directory into the file 

					Good to go! 
"""



from splinter import *

from splinter import Browser

import re

def len_counter(browser):
	x = browser.html
	x = x.lower()
	count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("active"), x))
	return count



def tester():
	browser = Browser('chrome')
	browser.visit('http://google.com')
	browser.fill('q', 'splinter - python acceptance testing for web applications')
	button = browser.find_by_name('btnG')
	button.click()
	browser.quit()

def browser_selector():
	try: 
		browser = Browser()
		return browser
	except:
		browser = Browser('chrome')
		return browser



#Initializes Craigslist 
browser = browser_selector()
username = "allianceAutoGroupva@gmail.com"
password = "Alliance2015"
site = str("https://accounts.craigslist.org/login/home")
browser.visit(site)

#Inputs Username and Password 
browser.find_by_id("inputEmailHandle").fill(username)
browser.find_by_id("inputPassword").fill(password)
browser.find_by_text("Log in").last.click()


#finds number of repost requirements 
buttons = browser.find_by_name("go")
buttons = [x for x in buttons if x.value!="delete"]
buttons = [x for x in buttons if x.value!= 'display']
buttons = [x for x in buttons if x.value!= "edit"]
num = len(buttons)


#editing the number of entries to be clicked

num = len_counter(browser)-2

#select the status button 



#run every consequent repost;
for i in range(num):
	headers = browser.find_by_tag("th")
	headers.first.click()
	lst_buttons = browser.find_by_name("go")
	lst_buttons = [x for x in lst_buttons if x.value!="delete"]
	lst_buttons = [x for x in lst_buttons if x.value!= "display"]
	lst_buttons = [x for x in lst_buttons if x.value!= "edit"]
	button_to_press = lst_buttons[i]
	button_to_press.click()

	#Handles optional "do you want to pay for repost argument"
	if browser.find_by_value("no thanks"):
		extra_button = browser.find_by_value('repost').last
		extra_button.click()
	#Runs necessary arguments to successfully repost 
	button3 = browser.find_by_name("go")
	if button3.first.value != 'delete':
		button3.first.click()
		button4 = browser.find_by_name("go").first
		button4.click()
		browser.visit(site)
browser.quit()
print("Success! You reposted " + str(num) + " Ads")







########################################################
####''' Copy and paste for multiple account links'''####
########################################################

#There is no additional necessary documentation 
#This is a test of emacs effectivenes 
