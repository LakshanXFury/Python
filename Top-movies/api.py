import requests


api_key = "61e528dacff24903d942a0faf48300a2"

movie = "Terminator"

parameter = {
    "query": movie,
    "api_key": api_key,
    "language":"en-US"
}

response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameter)
print(response.json()['results'])