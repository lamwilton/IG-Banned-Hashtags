from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import datetime

if __name__ == "__main__":
    # Use Chrome driver to obtain source HTML file of URL as string
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/p/B6RqMqwHiwt/')
    source = driver.page_source
    driver.close()

    # Create HTML parser
    bs = BeautifulSoup(source, features="html.parser")

    # Add hashtags
    hashtags = set()
    for item in bs.findAll(name='a'):
        if item.string is not None:
            if "#" in item.string:
                hashtags.add(item.string[1:])   # Removes # sign
    print("Hashtags of this post:")
    print(hashtags)

    # read from dictionary
    with open("dict.txt") as file:
        dict = file.readlines()
        dict = [word.rstrip("\n") for word in dict]
    dictSet = set(dict)

    # Find banned tags
    result = hashtags.intersection(dictSet)
    if len(result) == 0:
        print("No banned hashtags")
    else:
        print("Found banned hashtags:")
        print(result)
