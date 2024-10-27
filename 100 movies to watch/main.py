import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
LIVE_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(LIVE_URL)
# print(response.text)

# Write your code below this line 👇

website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# print(soup.prettify())
all_movies = soup.find_all(name="h3")
# print(all_movies)
list_movies = [movies.get_text() for movies in all_movies]

print(list_movies[::-1]) #Slice operator, which will reverse the list  "::-1"

movies = list_movies[::-1]  #Slice operator, which will reverse the list  "::-1" list_name[start : end : step]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

