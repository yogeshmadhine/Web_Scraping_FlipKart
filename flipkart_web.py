from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up ChromeDriver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Flipkart URL (Example: Search for "laptop")
url = "https://www.flipkart.com/search?q=laptop"
driver.get(url)

# Give some time for page to load (5 seconds)
time.sleep(5)

# Extract page source and parse it using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the browser
driver.quit()

# Extract product details
products = []
for product in soup.find_all('div', {'class': '_2kHMtA'}):
    name = product.find('div', {'class': '_4rR01T'}).text if product.find('div', {'class': '_4rR01T'}) else "No Name"
    price = product.find('div', {'class': '_30jeq3 _1_WHN1'}).text if product.find('div', {'class': '_30jeq3 _1_WHN1'}) else "No Price"
    rating = product.find('div', {'class': '_3LWZlK'}).text if product.find('div', {'class': '_3LWZlK'}) else "No Rating"
    
    products.append([name, price, rating])

# Save data to CSV file
df = pd.DataFrame(products, columns=['Product Name', 'Price', 'Rating'])
df.to_csv('output.csv', index=False)

print("✅ Data Scraped Successfully and Saved to output.csv ✅")
