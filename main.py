import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
top_100_webpage = response.text

soup = BeautifulSoup(top_100_webpage, "html.parser")

movies_list = soup.select("h2 > strong")
movie_titles = [movie.getText() for movie in movies_list]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
