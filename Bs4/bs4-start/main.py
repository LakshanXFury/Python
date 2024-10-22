from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title) # Gets the entire title
print(soup.title.name) #Get the name of the title
print(soup.title.string) #Gets the string which is in the title tag

print(soup.p)