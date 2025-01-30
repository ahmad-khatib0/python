from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def main():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bs = BeautifulSoup(html.read(), "html.parser")

    nameList = bs.find_all("span", {"class": "green"})
    for name in nameList:
        print(name.get_text())

    all_headers = bs.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    print(all_headers)

    # if you want to find the number of times “the prince” is surrounded by tags on the page:
    nameList = bs.find_all(text="the prince")
    print(len(nameList))

    # The additional kwargs parameter allows you to pass any additional named arguments you want
    # into the method. Any extra arguments that find or find_all doesn’t recognize will be used
    # as tag attribute matchers. For example:
    title = bs.find_all(id="title", class_="text")
    title = bs.find(id="title")  # this better because you are looking for an ID
    print(title)

    bs.find(attrs={"id": "text"})  # using attrs dic instead


def navTrees():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bs = BeautifulSoup(html, "html.parser")

    for child in bs.find("table", {"id": "giftList"}).children:
        print(child)

    for sibling in bs.find("table", {"id": "giftList"}).tr.next_siblings:
        # print all rows of products from the product table, except for the first title row
        print(sibling)

    # print the price
    print(
        bs.find(
            "img", {"src": "../img/gifts/img1.jpg"}
        ).parent.previous_sibling.get_text()
    )

    # regular expressions
    images = bs.find_all("img", {"src": re.compile("..\/img\/gifts/img.*.jpg")})
    for image in images:
        print(image["src"])

    ## Lambda Expressions
    bs.find_all(lambda tag: len(tag.attrs) == 2)
    # use lambda functions to replace existing BeautifulSoup functions:
    bs.find_all(lambda tag: tag.get_text() == "Or maybe he's only resting?")


if __name__ == "__main__":
    main()

    navTrees()
