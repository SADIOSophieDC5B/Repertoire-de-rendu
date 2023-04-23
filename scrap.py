import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# URL de la page à extraire
url = "https://www.scrapethissite.com/pages/simple/"

# Envoie une requête HTTP à l'URL et récupère le contenu de la page
response = requests.get(url)
content = response.content

# Parse le contenu HTML de la page avec BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Trouve toutes les divs avec la classe "country"
countries = soup.find_all("div", class_="country")

# Initialise une liste vide pour stocker les données
data = []

# Pour chaque div "country", récupère les données des classes spécifiées et les ajoute à la liste "data"
for country in countries:
    name = country.find(class_="country-name").get_text()
    info = country.find(class_="country-capital").get_text()
    population = country.find(class_="country-population").get_text()
    area = country.find(class_="country-area").get_text()
    data.append([name, info, population, area])

# Affiche le tableau de données
print(tabulate(data, headers=["Country Name", "Country Capital", "Population", "Area(Km²)"]))
