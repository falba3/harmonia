from bs4 import BeautifulSoup
import requests


url = "https://www.idealista.com/venta-viviendas/madrid-madrid/con-precio-hasta_1000000/"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
# with open('results.txt', 'w') as file:
#     file.write(str(soup))

# print(soup)

listings = soup.find_all(class_='item-info-container')

for listing in listings:
    title = listing.find(class_='item-link').text.strip()
    price = listing.find(class_='item-price').text.strip()
    print(f"Title: {title}")
    print(f"Price: {price}")


