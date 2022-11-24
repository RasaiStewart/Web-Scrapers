import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'

print(url)

page = requests.get(url)

print(page)

soup = bs4.BeautifulSoup(page.text, "html.parser")

print(page.text)

movies = soup.find_all('div', {'class':'lister-item-content'})

len(movies)

movies[0]

titles = [ m.find('a').text for m in movies]

len(titles)

print(titles)

release = [m.find('span', {'class':'lister-item-year text-muted unbold'}).text for m in movies]

print(release)

imdb_rating = [m.find('div', {'class': 'inline-block ratings-imdb-rating'})['data-value'] for m in movies]

imdb_rating = [m.find('div', {'class': 'inline-block ratings-imdb-rating'}).text.replace('\n', '') for m in movies]

print(imdb_rating)

directors = [m.find_all('p')[2].text.split('|')[0].strip() for m in movies]

print(directors)