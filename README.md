# IndependentBreweryScraping
Python web scrape application mining Brewery information

This data mining script accesses https://www.brewersassociation.org/directories/breweries/ and scrapes the listed brewery information from the site and saves to a csv file to the local directory

When loaded, the website defaults to US breweries and these are the listings that are scraped. The application uses Selenium so could easily be enhanced to alter the dropdowns on the site to select different territories or just specific US states of interest 

NB. To re-use this script for your own purpose, you will need to install the Google Chrome web driver (https://chromedriver.chromium.org/downloads) and alter line xxx in the code to point at your own version of the driver
