import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(f'Previous webpage height was: {last_height}. Now the height is: {new_height}')
        if new_height == last_height:
            break

        last_height = new_height

def render_page(url):
	driver = webdriver.Chrome('path to web driver here')
	driver.get(url)
	# time.sleep(3)
	# Call the scroll_down function to scroll to bottom of page and load all data
	scroll_down(driver)
	r = driver.page_source
	driver.close()
	return r

def render_page_test(url):
	driver = webdriver.Chrome('path to web driver here')
	driver.get(url)
	time.sleep(5)
	r = driver.page_source
	driver.close()
	return r

def scrape_company_info(html):
	brewery_info = {}

	try:
		name = html.find('h3').text
		brewery_info['Name'] = name
	except:
		print('No brewery name available')

	try:
		address = html.find('div').text
		brewery_info['Address'] = address
	except:
		print('No brewery address available')

	paragraphs = html.find_all('p', class_='alt mb-0')
	for p in paragraphs:
		try:
			phone = p.find('span', itemprop='telephone').text
			brewery_info['PhoneNumber'] = phone
			continue
		except:
			pass

		try:
			weburl = p.find('a', itemprop='image')['href']
			brewery_info['Website'] = weburl
			continue
		except:
			pass

		try:
			brewtype = p.find('a').text
			brewery_info['BreweryType'] = brewtype
			continue
		except:
			pass

	return brewery_info


count = 1
url = 'https://www.brewersassociation.org/directories/breweries/'
source = render_page(url)
# source = render_page_test(url)
soup = BeautifulSoup(source, 'html.parser')

breweries = soup.find_all('div', class_='company-content')

# for brewery in breweries:
# 	print(f'{count} ' + brewery.find('h3').text)
# 	count +=1

# for brewery in breweries:
# 	print(brewery)
# 	info = scrape_company_info(brewery)
# 	print(info)


with open ('brewery_info.csv', 'w') as f:
	headers = ['Name','Address','PhoneNumber','BreweryType','Website']
	csv_writer= csv.DictWriter(f, fieldnames=headers)
	csv_writer.writeheader()

	for brewery in breweries:
		info = scrape_company_info(brewery)
		csv_writer.writerow(info)






