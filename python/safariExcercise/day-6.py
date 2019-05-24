import requests
import re
from bs4 import BeautifulSoup

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('{.*?}')
    return re.sub(clean, '', text)

urlPage = 'https://www.geeksforgeeks.org/get-post-requests-using-python/'
page = requests.get(urlPage)
soup = BeautifulSoup(page.text,"lxml")
print(soup.get_text())
