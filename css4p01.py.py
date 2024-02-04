# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:17:28 2024

@author: radzi
"""

import pandas as pd

file_path = "C:/Users/radzi/Downloads/CSS/Project/movie_dataset.csv"

# Load the dataset into a Pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame to understand the structure
print(df.head())

# Find the highest-rated movie based on the 'rating' column
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

# Display information about the highest-rated movie
print("Highest Rated Movie:")
print(highest_rated_movie)

# Calculate the average revenue of all movies
average_revenue = df['Revenue (Millions)'].mean()

# Display the result
print(f"Average Revenue of All Movies: {average_revenue}")

# Filter movies from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

# Display the result
print(f"Average Revenue of Movies from 2015 to 2017: {average_revenue_2015_to_2017}")

# Count the number of movies released in the year 2016
movies_2016 = df[df['Year'] == 2016]

# Get the count of movies released in 2016
num_movies_2016 = movies_2016.shape[0]

# Display the result
print(f"Number of Movies Released in 2016: {num_movies_2016}")

# Count the number of movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Get the count of movies directed by Christopher Nolan
num_nolan_movies = nolan_movies.shape[0]

# Display the result
print(f"Number of Movies Directed by Christopher Nolan: {num_nolan_movies}")

# Count the number of movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Get the count of movies with a rating of at least 8.0
num_high_rated_movies = high_rated_movies.shape[0]

# Display the result
print(f"Number of Movies with a Rating of at Least 8.0: {num_high_rated_movies}")

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()

# Display the result
print(f"Median Rating of Movies Directed by Christopher Nolan: {median_rating_nolan_movies}")

# Group by release year and calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()

# Display the result
print(f"Year with the Highest Average Rating: {year_highest_average_rating}")

# Filter movies from 2006 to 2016
movies_2006_to_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]

# Get the number of movies made in 2006 and 2016
num_movies_2006 = movies_2006_to_2016[movies_2006_to_2016['Year'] == 2006].shape[0]
num_movies_2016 = movies_2006_to_2016[movies_2006_to_2016['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

# Display the result
print(f"Percentage Increase in Number of Movies from 2006 to 2016: {percentage_increase:.2f}%")

# Combine all actors' names into a single string
all_actors_str = ','.join(df['Actors'].fillna('').astype(str).values)

# Split the string into a list of actors
all_actors_list = [actor.strip() for actor in all_actors_str.split(',')]

# Find the most common actor
most_common_actor = max(set(all_actors_list), key=all_actors_list.count)

# Display the result
print(f"Most Common Actor in All Movies: {most_common_actor}")

# Extract all unique genres from the dataset
unique_genres = set(','.join(df['Genre'].fillna('').astype(str).values).split(','))

# Count the number of unique genres
num_unique_genres = len(unique_genres)

# Display the result
print(f"Number of Unique Genres: {num_unique_genres}")

# Get the unique release years
unique_years = df['Year'].unique()

# Display the result
print("List of Unique Release Years:")
for year in sorted(unique_years):
    print(year)
    


