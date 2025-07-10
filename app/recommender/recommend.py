import os
import requests
import json

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

MOOD_GENRE_MAP = {
    "happy": ["35", "10749"],  # Comedy, Romance
    "sad": ["18"],             # Drama
    "excited": ["28", "53"],   # Action, Thriller
    "curious": ["99"],         # Documentary
}

def get_movies_by_genre(genre_ids):
    movies = []
    for genre_id in genre_ids:
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres={genre_id}"
        res = requests.get(url)
        data = res.json()
        if 'results' in data:
            movies.extend(data['results'][:5])
    return movies

def recommend_movies(mood):
    genre_ids = MOOD_GENRE_MAP.get(mood.lower(), ["35"])  # default to comedy
    return get_movies_by_genre(genre_ids)

