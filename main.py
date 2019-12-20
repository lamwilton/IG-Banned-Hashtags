from selenium import webdriver
from bs4 import BeautifulSoup

if __name__ == "__main__":
    """
    Receives IG post URL from user input and opens the URL by chrome driver. Then using BeautifulSoup HTML parser to get
    hashtags and find matches with the included dictionary file. Does not use Instagram API.
    """
    # read from dictionary
    with open("dict.txt") as dictFile:
        dictionary = dictFile.readlines()
        dictionary = [word.rstrip("\n") for word in dictionary]
    dictSet = set(dictionary)

    # Use Chrome driver to obtain source HTML file of URL as string
    url = input("Enter post URL: ")
    driver = webdriver.Chrome()
    try:
        driver.get(url)
    except Exception:
        print("Invalid URL")
        exit()
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
    print("Post url: " + url)
    print("Hashtags of this post (" + str(len(hashtags)) + "):")
    print(hashtags)

    # Find banned tags
    result = hashtags.intersection(dictSet)
    if len(result) == 0:
        print("No banned hashtags")
    else:
        print("Found banned hashtags:")
        print(result)
