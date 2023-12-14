# importing required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set up Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

service.start()
driver = webdriver.Chrome(service=service)

# Using this URL to find TOP rated IMDB 10000 movies (what have at least 10000 votes)
url = "https://www.imdb.com/search/title/?title_type=feature&sort=user_rating,desc&num_votes=10000"
driver.get(url)

# Function to scroll down and click the "50 more" button to load dynamic content (to load move movies)
def scroll_and_click():
    for scroll in range(200):  # Set 200 times to scroll and click the "50 more" button
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load

        # Click the "50 more" button to load more results
        see_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[@class="ipc-see-more__text" and contains(text(), "50 more")]'))
        )
        see_more_button.click()

        time.sleep(5)  # Give the time to load the page

scroll_and_click()

# Extract links to all movies from movie list
soup = BeautifulSoup(driver.page_source, 'html.parser')
movie_links = soup.find_all('a', class_='ipc-title-link-wrapper', tabindex='0')

# Extract and print the full URL for each link
base_url = "https://www.imdb.com"
movie_urls = [base_url + link.get('href') for link in movie_links]

# Save the list of URLs to a CSV file
df = pd.DataFrame({'Movie URLs': movie_urls})
df.to_csv('MovieURLs.csv', index=False)

# Close the browser window
driver.quit()