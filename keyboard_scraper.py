# Web scraper for scraping GB on geekhack
# Author: Lucas Lin

import bs4 as bs
import urllib.request

async def get_all_recent():
    return _get_all_recent()

def _get_all_recent():
    source = urllib.request.urlopen('https://geekhack.org/index.php?board=70.0').read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    tags = soup.find_all("td", {"class": "subject windowbg2"})
    result = []
    for tag in tags:
        link = tag.find("div").find("span").find("a", href=True)['href']
        title = tag.find("div").find("span").find("a", href=True).text
        result.append((link, title))
    return result

def get_title(url):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'html.parser')
    tags = soup.find("div", {"class": "cat_bar"})
    return tags.text.strip().strip("Author").strip()

if __name__ == "__main__":
    # _get_all_recent test
    list = _get_all_recent()
    print(list[0][0])
    print(list[0][1])
    print("\n Passed, Please manually check output")
