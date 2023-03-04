import requests as re
from bs4 import BeautifulSoup
import pandas as pd

url = ""

r = re.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find('div', {'class': ''})

text = results.get_text(strip=True)

df = pd.DataFrame({'Text': [text]})

df.to_csv('output.csv', index=False)

cs = pd.read_csv('output.csv')

print(cs)
print(text)

