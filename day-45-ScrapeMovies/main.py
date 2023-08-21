import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
title_list = soup.find_all(name="h3", class_="title")
title_list.reverse()  # tha same with title_list[::-1]
# for title in title_list:
#     print(title.get_text())

with open("movies.txt", "w") as file:
    for title in title_list:
        file.write(title.get_text() + "\n")





