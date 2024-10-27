from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
# print(response.text)
yc_webpage = response.text

### Gets only the first article in the List

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
# print(article_tag.getText())  # Gets the Headline Text
#
# article_link = soup.find(name="a", class_="storylink")
# print(article_link.get("href")) #Gets the Link
#
# article_upvote = soup.find(name="span", class_="score")
# print(article_upvote.getText()) #Gets the points

article_text = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    links = article_tag.get("href")
    article_links.append(links)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_text)
print(article_links)
print(article_upvote)

#To find the largest in the list
highest_number = max(article_upvote)
largest_index = article_upvote.index(highest_number)
print(f"The largest index is: {largest_index}")
print(article_text[largest_index], article_links[largest_index])