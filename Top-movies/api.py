import requests


api_key = "61e528dacff24903d942a0faf48300a2"

movie = "Terminator"

parameter = {
    # "query": movie,
    "api_key": api_key,
    "language":"en-US"
}

movie_id = int(218)
# response = requests.get("https://api.themoviedb.org/3/search/movie/", params=parameter)
response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameter)
print(response.json())