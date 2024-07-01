from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags= soup.findAll(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# heading = soup.findAll(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)

# company_url = soup.select_one(selector= "p a")
# print(company_url.get("href"))

headings = soup.select(".heading")
print(headings)