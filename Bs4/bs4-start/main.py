from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title) # Gets the entire title
print(soup.title.name) #Get the name of the title
print(soup.title.string) #Gets the string which is in the title tag

print(soup.p)

anchor_tags = (soup.find_all(name="a"))
print(anchor_tags)   #all the tags

for tag in anchor_tags:  # all tags in the text
    # print(tag.getText()) #gets the text value in the links
    print(tag.get("href")) #gets all the links


#attribute names
heading = soup.find(name="h1", id="name")
print(heading)

heading = soup.find(name="h3", class_="heading")
print(heading)

#To get specific item
company_url = soup.select_one(selector="p a") # A-tag which sits inside a P-tag
print(company_url)

#Id is selected using Pound sign (#)
name = soup.select_one(selector="#name")
print(name)

#Class is selected using Pound sign (.)
heading = soup.select(".heading")
print(heading)