from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")

yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
articles_a = soup.find_all("a", {"rel": True})
article_texts = []
article_links = []
for article in articles_a:
    article_texts.append(article.get_text())
    article_links.append(article.get("href"))
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all("span", {"class": "score"})]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_index = article_upvotes.index(max(article_upvotes))

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])













# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title.name)
# # print(soup.prettify())
#
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#     # print(tag.getText)
#     # print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# name = soup.select_one(selector="#name")  # like css anchor
# print(name)
#
# heading = soup.select(".heading")
# print(heading)



