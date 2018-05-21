import requests
from bs4 import BeautifulSoup


page = requests.get('http://www.ironman.com/triathlon/events/americas/ironman/maryland/results.aspx#axzz5FEQHzO1B')

soup = BeautifulSoup(page, 'lxml')

print(soup)