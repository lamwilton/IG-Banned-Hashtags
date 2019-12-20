# IG_Banned_Hashtags
Receives IG post URL from user input and opens the URL by chrome driver. Then using BeautifulSoup HTML parser to get
hashtags and find matches with the included dictionary file. Does not use Instagram API.

Requirements: Google Chrome installed, chromedriver.exe and dict.txt in the same directory of this program  (included)

Sample output:
```
Post url: https://www.instagram.com/p/B6GF1bZg8n3/
Hashtags of this post (9):
{'nsfwpost', 'bdsm', 'ddlg', 'nsfwtextposts', 'kinks', 'ddlgpost', 'bdsmkink', 'nsfwconcept', 'nsfw'}
Found banned hashtags:
{'ddlg', 'bdsm', 'nsfw'}
```
