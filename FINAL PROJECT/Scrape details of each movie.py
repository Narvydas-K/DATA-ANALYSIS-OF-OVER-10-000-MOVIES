# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Use movie URLs from 'MovieURLs.csv'
url_df = pd.read_csv('CSV_files/MovieURLs.csv')
movie_urls = url_df['Movie URLs'].tolist()

# Create an empty list to store data of each movie
movie_data = []

# Set the headers and timeout
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
timeout = 10

# Loop through each movie URL
for full_url in movie_urls:
    try:
        response = requests.get(full_url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Check for HTTP errors

        # Get content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get movie title
        movie_title_element = soup.find('span', class_='hero__primary-text')
        movie_title = movie_title_element.text.strip() if movie_title_element else 'N/A'

        # Get movie details (information about movie year and length)
        movie_details_element = soup.find('ul', class_='ipc-inline-list ipc-inline-list--show-dividers sc-d8941411-2 cdJsTz baseAlt')
        movie_details = movie_details_element.text.strip() if movie_details_element else 'N/A'

        # Get movie category details
        movie_category_element = soup.find('a', class_='ipc-chip--on-baseAlt')
        movie_category = movie_category_element.text.strip() if movie_category_element else 'N/A'

        # Get movie rating
        movie_rating_element = soup.find('span', class_='sc-bde20123-1 cMEQkK')
        movie_rating = movie_rating_element.text.strip() if movie_rating_element else 'N/A'

        # Get movie votes
        movie_votes_element = soup.find('div', class_='sc-bde20123-3 gPVQxL')
        movie_votes = movie_votes_element.text.strip() if movie_votes_element else 'N/A'

        # Get movie director
        movie_director_element = soup.find('a', class_='ipc-metadata-list-item__list-content-item--link')
        movie_director = movie_director_element.text.strip() if movie_director_element else 'N/A'

        # Append data into the list movie_data
        movie_data.append({'Title': movie_title, 'Details': movie_details, 'Category': movie_category,
                           'Rating': movie_rating, 'Votes': movie_votes, 'Director': movie_director})

    except requests.exceptions.RequestException as e:
        # Print an error message if data was not scraped from any individual page and continue to the next URL
        print(f"Error processing {full_url}: {e}")
        continue  # Go to the next movie link in the loop

# Create a DataFrame from the list of movie_data
df = pd.DataFrame(movie_data)

# Save the DataFrame to a CSV file
df.to_csv('MovieData.csv', index=False)