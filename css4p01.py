# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df=pd.read_csv("data_01/movie_dataset.csv")

pd.set_option('display.max_rows',None)

print(df)

print(df.columns)

#Fill NAs or empty fields in Revenue (Millions) column

x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace = True)

print(df)

#Fill NAs or empty fields in Metascore column
x = df["Metascore"].mean()
 
df["Metascore"].fillna(x, inplace = True)

print(df)

print(df.info())

print(df.describe())

print(df['Rating'].max())


#QUESTION 3

# Filter movies from 2015 to 2017
filtered_data = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate average revenue
average_revenue = filtered_data["Revenue (Millions)"].mean()

print(f'The average revenue of movies from 2015 to 2017 is: ${average_revenue:.2f}')

#QUESTION 4

# Count the number of movies released in 2016
movies_2016 = df[df["Year"] == 2016]
number_of_movies_2016 = len(movies_2016)

print(f'The number of movies released in 2016 is: {number_of_movies_2016}')

#Question 5

nolan_movies = df[df['Director'] == 'Christopher Nolan']
number_of_nolan_movies = len(nolan_movies)

print(f'The number of movies directed by Christopher Nolan is: {number_of_nolan_movies}')

#QUESTION 6

# Count the number of movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]
number_of_high_rated_movies = len(high_rated_movies)

print(f'The number of movies with a rating of at least 8.0 is: {number_of_high_rated_movies}')


#QUESTION 7

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating
median_rating_nolan_movies = nolan_movies['Rating'].median()

print(f'The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies}')

#QUESTION 8

# Group by release year and calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f'The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}')

#QUESTION 9

# Filter movies released between 2006 and 2016
movies_2006_to_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]

# Calculate the number of movies made in 2006 and 2016
num_movies_2006 = len(df[df['Year'] == 2006])
num_movies_2016 = len(df[df['Year'] == 2016])

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
print(percentage_increase)

#QUESTION 10

import pandas as pd
from collections import Counter

# Combine all actors into a single list
all_actors = [actor.strip() for actors_list in df['Actors'].str.split(',') for actor in actors_list]

# Find the most common actor
most_common_actor, _ = Counter(all_actors).most_common(1)[0]

print(f'The most common actor in all movies is: {most_common_actor}')

#QUESTIONS 11

# Combine all genres into a single list
all_genres = [genre.strip() for genres_list in df['Genre'].str.split(',') for genre in genres_list]

# Find the number of unique genres
unique_genres_count = len(set(all_genres))

print(f'The number of unique genres in the dataset is: {unique_genres_count}')

#QUESTION 12

# Perform correlation analysis on numerical features
correlation_matrix = df[['Runtime (Minutes)', 'Votes', 'Revenue (Millions)', 'Metascore']].corr()

# Print correlation matrix
print(correlation_matrix)