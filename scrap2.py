import requests
from bs4 import BeautifulSoup
import pandas as pd

results = []

# Loop through the first 10 pages
for i in range(1, 11):
    # Make a request to the page
    response = requests.get(f"https://www.scrapethissite.com/pages/forms/?page_num={i}")
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table and loop through the rows
    table = soup.find('table', {'class': 'table'})
    rows = table.find_all('tr')

    for row in rows[1:]:
        # Find the columns in the row
        cols = row.find_all('td')

        # Extract the data from the columns
        name = cols[0].text.strip()
        year = cols[1].text.strip()
        wins = int(cols[2].text.strip())
        losses = int(cols[3].text.strip())
        ot_losses = int(cols[4].text.strip()) if cols[4].text.strip() != '' else 0
        pct_wins = float(cols[5].text.strip().replace('%', '')) / 100
        gf = int(cols[6].text.strip())
        ga = int(cols[7].text.strip())
        diff = int(cols[8].text.strip())

        # Append the data to the results list
        results.append((name, year, wins, losses, ot_losses, pct_wins, gf, ga, diff))

# Create a DataFrame from the scraped data
df = pd.DataFrame(results, columns=['Name', 'Year', 'Wins', 'Losses', 'Ot-losses', '% Wins', 'GF', 'GA', '+/-'])

# Filter the DataFrame based on the +/- column
df_filtered = df[df['+/-'] < 300]

# Write the filtered data to a CSV file
df_filtered.to_csv('results.csv', index=False, header=["Team", "Year", "Wins", "Losses", "OT Losses", "% Wins", "GF", "GA", "+/-"], sep=',')

print(df_filtered)
