import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
html = response.text
# print(html)

soup = BeautifulSoup(html, "html.parser")
all_h3 = soup.find_all(name='h3', class_="title")
movies = [all_h3[i].getText() for i in reversed(range(len(all_h3)))]
print(movies)

with open("movies.txt", 'a', encoding='utf-8') as f:
    for i in range(len(movies)):
        f.write(movies[i])
        f.write('\n')

