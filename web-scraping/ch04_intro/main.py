from urllib.error import URLError
from urllib.request import HTTPError, urlopen
from bs4 import BeautifulSoup


def req():
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())

    try:
        bs = BeautifulSoup(html.read(), "html.parser")  # or just html withou read()
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!", e)
    else:
        # this returns only the first instance of the h1 tag found on the page. By convention, only
        # one h1 tag should be used on a single page, but conventions are often broken on the web,
        #  so you should be aware that this will retrieve only the first instance of the tag
        print(bs.h1)  # or
        print(bs.html.body.h1)  # or
        print(bs.body.h1)  # or
        print(bs.html.h1)

        try:
            badContent = bs.nonExistingTag.anotherTag
        except AttributeError as e:
            print("Tag was not found", e)
        else:
            if badContent is None:
                print("Tag was not found")
            else:
                print(badContent)


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), "html.parser")
        title = bs.body.h1
    except AttributeError as e:
        return None

    return title


if __name__ == "__main__":
    req()
    title = getTitle("http://www.pythonscraping.com/pages/page1.html")
    if title == None:
        print("Title could not be found")
    else:
        print(title)
