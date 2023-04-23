import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


url = "https://www.scrapethissite.com/pages/simple/"


response = requests.get(url)
content = response.content


soup = BeautifulSoup(content, "html.parser")


countries = soup.find_all("div", class_="country")


data = []


for country in countries:
    name = country.find(class_="country-name").get_text()
    info = country.find(class_="country-capital").get_text()
    population = country.find(class_="country-population").get_text()
    area = country.find(class_="country-area").get_text()
    data.append([name, info, population, area])


print(tabulate(data, headers=["Country Name", "Country Capital", "Population", "Area(Km²)"]))
