import requests, sys, webbrowser
from bs4 import BeautifulSoup

"""
Assignment: Homework 7, Exercise 3
Name: Samuel Haberkorn
Date: December 3, 2020
Description: The program takes a command line argument and searches google for it. Then opens the top 10 results in the
browser and outputs a file "results.html" containing the links
"""

URL = "https://www.google.com/search?q={term}"
LINK_HTML = "<a href={URL}>{URL}</a><br>"

def main():
    if len(sys.argv) < 2:
        print("Please provide a search term in quotes")
        exit(-1)
    # search results from google
    search = "+".join(sys.argv[1].split(" "))
    response = requests.get(URL.format(term=search))
    # soup stuff to read the response text in
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    # look for the class tag for a dif then get the hyperlinks and append to a List
    for div in soup.find_all("div", class_="kCrYT"):
        a_tag = div.find_all('a')
        if not a_tag:
            continue
        # google tacks on some extra arguments we need to get rid of...
        results.append(a_tag[0]['href'][7:a_tag[0]['href'].index("&sa")])
    # open a file called results and place the top 10 search results there
    file = open("results.html", "w")
    for result in results[:10]:
        # and open the browser and open new tabs there
        webbrowser.open(result, autoraise=True)
        file.write(LINK_HTML.format(URL=result))



if __name__ == '__main__':
    main()
