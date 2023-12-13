#INITIALLY THIS CODE WAS USED TO SCRAPE LINKS TO MOVIES AND MOVIE DATA FROM THE PAGE OF EACH MOVIE,
#BUT SOME PAGES WERE NOT LOADED DUE TO VARIOUS REASONS (SERVER, CONNECTION, ETC) AND THIS CODE WAS DIVIDED
#INTO 2 DIFFERENT AND MORE STABLE CODES: 'SCRAPE MOVIE URLS' AND 'SCRAPE DETAILS OF EACH MOVIE' (SEE OTHER FILES)
#
# required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set up Selenium WebDriver
webdriver_path = "C:/Users/Narvydas/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(webdriver_path)
service.start()
driver = webdriver.Chrome(service=service)

url = "https://www.imdb.com/search/title/?title_type=feature&sort=user_rating,desc&num_votes=10000"
driver.get(url)
#vidmanto prisijungimas

# Function to scroll down and click the "50 more" button
def scroll_and_click():
    for _ in range(200):  # Set the number of times you want to scroll and click
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load

        # Click the "50 more" button to load more results
        see_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[@class="ipc-see-more__text" and contains(text(), "50 more")]'))
        )
        see_more_button.click()

        time.sleep(5)  # Give the time to load the page

# Scroll down and click the "50 more" button multiple times
scroll_and_click()

# Extract links after loading additional content
soup = BeautifulSoup(driver.page_source, 'html.parser')
movie_links = soup.find_all('a', class_='ipc-title-link-wrapper', tabindex='0')

# Extract and print the full URL for each link
base_url = "https://www.imdb.com"
movie_data = []  # Initialize an empty list to store movie data

for link in movie_links:
    relative_url = link.get('href')
    full_url = base_url + relative_url

    # Open each movie page
    driver.get(full_url)

    # Extract movie title
    movie_title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="hero__primary-text"]'))
    )
    movie_title = movie_title_element.text.strip()

    # Extract movie details (year amd length)
    movie_details_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//ul[@class="ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt"]'))
    )
    movie_details = movie_details_element.text.strip()

    # Extract movie category and record "N/A" if movie has no category information
    try:
        movie_category_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@class="ipc-chip ipc-chip--on-baseAlt"]'))
        )
        movie_category = movie_category_element.text.strip()
    except:
        movie_category = "N/A"

    # Extract movie rating
    movie_rating_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//span[@class="sc-bde20123-1 cMEQkK"]'))
    )
    movie_rating = movie_rating_element.text.strip()

    # Extract movie votes
    movie_votes_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="sc-bde20123-3 gPVQxL"]'))
    )
    movie_votes = movie_votes_element.text.strip()

    # Extract movie director
    movie_director_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]'))
    )
    movie_director = movie_director_element.text.strip()

    # Append data into list movie_data
    movie_data.append({'Title': movie_title, 'Details': movie_details, 'Category': movie_category, 'Rating': movie_rating, 'Votes': movie_votes, 'Director': movie_director})

# Create a DataFrame from the list of movie_data
# df = pd.DataFrame(movie_data)

# Save the DataFrame to a CSV file
df.to_csv('MovieData.csv', index=False)

# Close the browser window
driver.quit()