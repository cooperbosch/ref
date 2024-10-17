from bs4 import BeautifulSoup
from requests import get

# Ideally we use links like these that give referee data per team, but this code is broken idk why
# Requests.get gets a not found 404 error even though the url is valid, not sure here

city_url = "https://www.transfermarkt.us/manchester-city/schiedsrichter/verein/281/reldata/GB1&def"
arsenal_url = "https://www.transfermarkt.us/fc-arsenal/schiedsrichter/verein/11/reldata/&2023"

response = get(city_url)
print(response.text)

doc = BeautifulSoup(response.text, "html.parser")

print(doc)
print('hi')