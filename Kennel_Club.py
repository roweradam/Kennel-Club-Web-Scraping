# Import libraries
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt

# Create pull request from Kennel Club Website
url = r'https://www.thekennelclub.org.uk/search/breeds-a-to-z/'
page = rq.get(url)

# Prefix of website for later url extraction
prefix = r'https://www.thekennelclub.org.uk/'

# Parse data using beautiful soup
soup = bs(page.content, "html.parser")

"""
Getting breed, category and url link
"""
# Search for dog breed, category and url link
breed_titles = soup.find_all(attrs={"class":"m-breed-card__title"})
breed_categories = soup.find_all(attrs={"class":"m-breed-card__category"})
breed_links = soup.find_all("a", {"class", "m-breed-card__link"})

# Create list of breed titles
breeds = []
for i in breed_titles:
    breeds.append(i.string)

# Create list of categories
categories = []
for i in breed_categories:
    categories.append(i.string)

# Create list of url links
links = []
for a in breed_links:
    links.append(prefix + a["href"])

"""
Getting Other Information
"""
# Initiate lists for each data category
size = []
exercise = []
size_of_home = []
grooming = []
coat_length = []
sheds = []
lifespan = []
vulnerable_native_breed = []
town_or_country = []
size_of_garden = []

# Seach html for each summary list
breed_summary = soup.find_all("div", {"class":"m-breed-summary m-breed-card__summary-list"})
# itterate over each breed summary
for data in breed_summary:
    # within the breed summary for each for, get all elements of the list
    dog_info = data.find_all("dd")
    # initiate a list to temporarily store the data
    out = []
    # itterate over info in list and append it to the out list
    for info in dog_info:
        out.append(info.string)
    # take each element from the out list and append it to the relavent list for its data category
    size.append(out[0])
    exercise.append(out[1])
    size_of_home.append(out[2])
    grooming.append(out[3])
    coat_length.append(out[4])
    sheds.append(out[5])
    lifespan.append(out[6])
    vulnerable_native_breed.append(out[7])
    town_or_country.append(out[8])
    size_of_garden.append(out[9])

# Create dictionary of all data collected
dog_info_dict = {"Breed":breeds, "Category":categories, "URL":links, "Size":size,
                 "Exercise":exercise, "Size_Of_Home": size_of_home, "Grooming":grooming,
                 "Coat_Length":coat_length, "Sheds":sheds, "Lifespan":lifespan,
                 "Vulnerable_Native_Breed":vulnerable_native_breed, "Town_Or_Country":town_or_country,
                 "Size_of_Garden":size_of_garden}

# Create dataframe with data
df = pd.DataFrame(dog_info_dict)

# Get the data and time of the run to add to file name
todays_date = dt.datetime.now().strftime("%Y%m%d%H%M")

# Export file as csv
df.to_csv(r"C:\Users\arwill\OneDrive - The University of Liverpool\Documents\Kennel Club Web Scraping\Kennel_Club_Breed_AtoZ_{}.csv".format(todays_date))







