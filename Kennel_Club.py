# Import libraries
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

# Create pull request from Kennel Club Website
url = r'https://www.thekennelclub.org.uk/search/breeds-a-to-z/'
page = rq.get(url)

# Parse data using beautiful soup
soup = bs(page.content, "html.parser")




