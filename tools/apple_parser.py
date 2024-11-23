from bs4 import BeautifulSoup
from pathlib import Path

# Get list of scraped apple files
directory = '../site_data/apple'
files = Path(directory).glob('*')

# Destination for job titles
titles = []

# Iterate through each file and add the job titles to the array above
for file in files:
  print(file)
  with open(file) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    title_elements = soup.find_all('a', {'class': 'table--advanced-search__title'})
    titles += list(map(lambda e: e.contents[0], title_elements))

print(titles)