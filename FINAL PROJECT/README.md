# DATA ANALYSIS OF OVER 10,000 MOVIES

**Details:**<br><br>
Created by: Vidmantas Rauda and Narvydas Kareckas

This is the end project of Data Analysis (BIG DATA) course at Vilnius Coding School.

Project theme: Movie data scraping, cleaning, analysis and visualization. 

The main goal of the project is to implement BID DATA analysis methods to find out meaningful insights from analysing data of over 10000 Top rated movies.

In this project we used Python and CSV files showcasing our practical coding skills acquired at Vilnius Coding School.

**Applied knowledge:**<br><br>
Used libraries: Pandas, MatplotLib, SeaBorn, Selenium, NumPy, Requests, BeautifulSoup

**Files:**<br><br>
Scrape movie URLs.py<br>
Getting URLs of each movie from movie list https://www.imdb.com/search/title/?title_type=feature&sort=user_rating,desc&num_votes=10000 

MovieURLs.csv<br>
Storing scraped movie URLs into one file

Scrape details of each movie.py<br>
Getting details about each movie using movie URLs    

MovieData.csv<br>
Storing scraped details of each movie

Data_Analysis_Visualisation.py<br>
Data cleaning, analyzing and visualization
<br><br>
## Vizualizations



#### 1. Horizontal bar chart for average ratings by movie category:
![ratings_by_category.png](Graphs%2Fratings_by_category.png)

#### 2. Bar chart to show TOP movie director who created most films with rating >8:
![top_directors.png](Graphs%2Ftop_directors.png)

#### 3. Line Chart for movie lenght distrubution by year:
![movie_length_by_year.png](Graphs%2Fmovie_length_by_year.png)

#### 4. Horizontal bar chart for average movie length by category:
![movie_length_by_category.png](Graphs%2Fmovie_length_by_category.png)

#### 5. Bar chart for movie distribution by category:
![distribution_by_category.png](Graphs%2Fdistribution_by_category.png)

#### 6. Line chart for average rating by year:
![rating_by_year.png](Graphs%2Frating_by_year.png)

#### 7. Scatter graph to check correlation between movie length and rating:
![movie_length_rating_correlation.png](Graphs%2Fmovie_length_rating_correlation.png)

#### 8. Line chart to check the number of movies by year:
![number_of_movies_in_year.png](Graphs%2Fnumber_of_movies_in_year.png)


## Conclution<br>
**Movie data analysis shows that:**
1.	Movies have the highest average rating in the Documentary (7.7.) and Western (7.6) categories. The lowest average rating scores are in History (6.2) and Horror (6.2) categories.
2.	Top movie directors, who created the most movies with ratings > 8 are Akira Kurosawa (10 movies) and Martin Scorsese (9 movies).
3.	From 1915 to 1965 average movie length varied a lot (from 30 to 190 minutes) and from 1966 until now average movie length normalized and was between 100 and 120 minutes.
4.	The longest movies on average are in the Biography (122 min) category and the shortest ones (93 min) are in the Animation and Music categories.
5.	Most films were released in the Comedy, Action, and Drama categories, and movies from all remaining categories are a lot less common.
6.	Recently released movies have an average rating of 6.5 – 6.75 and movies with the highest rating (over 8) were released in 1921 and 1926.
7.	Longer movies have slightly better average ratings.
8.	Every year a bigger number of top-rated movies is released. Especially from 1980 to 2018 this curve is very steep. Since 2019 this number has decreased. This can be due to various reasons, one of them – being that we analyzed only movies with over 10000 votes and newer movies didn’t have enough time to get this number of votes.

