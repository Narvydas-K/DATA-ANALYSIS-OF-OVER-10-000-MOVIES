import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = 'MovieData.csv'
df = pd.read_csv(file_path)

#extracting information about hours from 'details' and converting to int
df[['Hours']] = df['Details'].str.extract(r'(\d?)h')
df['Hours'] = pd.to_numeric(df['Hours'], errors='coerce').fillna(0).astype(int)

#extracting information about minutes from 'details' and converting to int
df[['Minutes']] = df['Details'].str.extract(r'(\d{1,2})\s?m')
df['Minutes'] = pd.to_numeric(df['Minutes'], errors='coerce').fillna(0).astype(int)

#creating a new column about movie length information in minutes (int)
df['Length (min)'] = df['Hours'] * 60 + df['Minutes']

#creating a new column about movie year information
df['Year'] = df['Details'].str.slice(0, 4)

#transforming values from 'votes' to int
def value_to_int(x):
    if type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return int(float(x.replace('K', '')) * 1000)
        return 1000
    if 'M' in x:
        if len(x) > 1:
            return int(float(x.replace('M', '')) * 1000000)
        return 1000000
    return 0

df['Votes'] = df['Votes'].apply(value_to_int)
# print(df[['Title', 'Year', 'Length (min)', 'Category', 'Rating', 'Votes', 'Director']].head(100).to_string(index=False))
# Kokios kategorijos filmai turi aukščiausius reitingus
# Creating horizontal bar chart for average ratings by movie category
avg_category_rating = df.groupby('Category')['Rating'].mean().round(1).sort_values()
plt.figure(figsize=(10, 6))
bars = avg_category_rating.plot(kind='barh', color='skyblue')
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width()}',
             va='center', ha='left', fontsize=10, color='black')
plt.xlabel('Rating')
plt.ylabel('Category')
plt.title('Average Ratings by Movie Category')
plt.show()

# Kokie direktoriai sukūrę daugiau nei vieną filmą su aukštesniu nei 8 reitingu
# Creating a bar chart to show TOP movie director who created most films with rating >8
filtered_df = df[df['Rating'] > 8]
top_10_directors = filtered_df.groupby('Director')['Director'].count().nlargest(10)
plt.figure(figsize=(10, 6))
top_10_directors.plot(kind='bar', color='skyblue')
plt.xlabel('Director')
plt.ylabel('Number of Movies Created with Rating > 8')
plt.title('Top Movie Directors')
plt.xticks(rotation=20, ha='right')
plt.show()

# Ar per metus keitėsi filmų ilgiai
# Creating Line Chart for movie lenght distrubution by year
avg_movie_length = df.groupby('Year')['Length (min)'].mean()
plt.figure(figsize=(10, 6))
plt.plot(avg_movie_length.index, avg_movie_length.values, marker='o', linestyle='-')
plt.xlabel('Years')
plt.ylabel('Average Movie Length (min)')
plt.title('Changes in Average Movie Length Over Years')
plt.grid(True)
plt.xticks(avg_movie_length.index[::10])
plt.show()

# Kokia vidutinė filmų trukmė kiekvienoje kategorijoje
# Creating horizontal bar chart for average movie length by category
avg_category_length = df.groupby('Category')['Length (min)'].mean().astype(int).sort_values(ascending=False)
plt.figure(figsize=(10, 6))
bars = avg_category_length.plot(kind='barh', color='skyblue')
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width()}',
             va='center', ha='left', fontsize=10, color='black')
plt.xlabel('Length')
plt.ylabel('Category')
plt.title('Average Movie Length by Category')
plt.show()

#Filmu pasiskirstymas pagal kategorijas
#Creating a bar chart for movie distribution by category
category_distribution = df['Category'].value_counts()
plt.figure(figsize=(10, 8))
plt.bar(category_distribution.index, category_distribution, color='skyblue')
plt.xlabel('Category')
plt.ylabel('Number of Movies')
plt.title('Movie Distribution by Category')
plt.xticks(rotation=45, ha='right')
plt.show()

df['Year'] = df['Year'].astype(int)

# Išleidimo metų ir reitingo santykis

plt.figure(figsize=(10, 7), facecolor='black')
ax = plt.axes()
ax.set_facecolor('black')
rating_by_year = df.groupby('Year')['Rating'].mean().reset_index()
sns.lineplot(x='Year', y='Rating', data=rating_by_year, color='tab:purple', linewidth=2.5, marker='.',
             markersize=5)
plt.grid(color='cyan', linewidth=0.2)
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')
plt.title('Rating by year', color='khaki', fontsize=25)
plt.xlabel('Year', color='slateblue', fontsize=18)
plt.ylabel('Rating', color='slateblue', fontsize=18)
plt.show()



# ar filmų reitingas priklauso nuo filmo ilgio

reitingas = df['Rating']
ilgis = df['Length (min)']
plt.figure(facecolor='black')
ax = plt.axes()
ax.set_facecolor('black')
np.corrcoef(reitingas, ilgis)
plt.grid(color='cyan', linewidth=0.2)
plt.scatter(reitingas, ilgis, s=3, c=reitingas, cmap='Blues')
plt.title('Movie length and rating correlation', fontsize=15, color='khaki')
plt.xlabel('Rating', color='slateblue')
plt.ylabel('Movie length', color='slateblue')
plt.xticks(color='white', fontsize=10)
plt.yticks(color='white', fontsize=10)
plt.plot(np.unique(reitingas), np.poly1d(np.polyfit(reitingas, ilgis, 1))(np.unique(reitingas)), color='red')
plt.show()

#Filmų skaičius metuose

plt.figure(figsize=(10, 7),facecolor='black') #aplink grafika spalva
ax = plt.axes()
ax.set_facecolor('black') #paties grafiko spalva
movies_by_year = df.groupby('Year')['Title'].count().reset_index()
sns.lineplot(x='Year', y='Title', data=movies_by_year, color='tab:purple', linewidth=2.5, marker='.',
             markersize=5)
plt.grid(color='cyan', linewidth=0.2)
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')
plt.title('Number of movies in a year', color='khaki', fontsize=25)
plt.xlabel('Year', color='slateblue', fontsize=18)
plt.ylabel('Number of movies', color='slateblue', fontsize=18)
plt.show()