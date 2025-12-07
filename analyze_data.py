import pandas as pd

#Importing the most streamed spotify song 2024 dataset into python as spotify_df
spotify_df = pd.read_csv("data/most_streamed_spotify_songs_2024.csv", encoding='ISO-8859-1')

#view spotify_df basic information with head(), info(), and describe()
print(spotify_df.head(), "\n")
print(spotify_df.info(), "\n")
print(spotify_df.describe(), "\n")

#Accessing specific data from spotify_df
#Selects rows with the track called CHIHIRO 
print(spotify_df.loc[spotify_df['Track'] == 'CHIHIRO'], "\n")
#Selects the 2 row of the dataset 
print(spotify_df.iloc[2], "\n")
#Selects all the rows with the Artist Ariana Grande
print(spotify_df.loc[spotify_df['Artist'] == 'Ariana Grande'], "\n")
#Selects all the rows between the 5 and 11 row 
print(spotify_df.iloc[5:11], "\n")
#Selects the single column Album Name
print(spotify_df.loc[:,'Album Name'], "\n")
#Selects a single cell of the Artist name which matches the Track CHIHIRO
print(spotify_df.loc[spotify_df['Track'] == "CHIHIRO", 'Artist'], "\n")

#Using filters for the spotify_df 
#filter to look for albums called HIT ME HARD AND SOFT
filter_one = spotify_df['Album Name'] == "HIT ME HARD AND SOFT"
print(spotify_df[filter_one].head(), "\n")
#filter to look for Tyler, The Creator song with a Spotify Popularity score higher then 70 
filter_two = (spotify_df['Spotify Popularity'] > 70) & (spotify_df['Artist'] == 'Tyler, The Creator')
print(spotify_df[filter_two].head(), "\n")

#Creating a new Total Playlist Count  column which adds all the number of a songs playlist count across different platforms 
spotify_df['Total Playlist Count'] = spotify_df['Spotify Playlist Count'].replace({',': ''}, regex= True).astype(float) + spotify_df['Apple Music Playlist Count'] + spotify_df['Deezer Playlist Count'] + spotify_df['Amazon Playlist Count']
#Drops TIDAL Popularity column from spotify_df dataset
print(spotify_df.head(), "\n")
spotify_df = spotify_df.drop('TIDAL Popularity',axis=1)
#Shows the new Column Total Playlist Count and verifies TIDAL Popularity was drop from the dataset
print(spotify_df.info(), "\n")

#Using groupby() to find the mean for Track Scores across all artist songs
print("Mean of the artist track scores across there songs ")
print(spotify_df.groupby('Artist')['Track Score'].mean())