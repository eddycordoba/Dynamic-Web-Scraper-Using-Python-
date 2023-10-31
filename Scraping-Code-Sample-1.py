import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'http://quotes.toscrape.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find and extract the quotes
    quotes = soup.find_all('span', class_='text')
    
    # Print the quotes
    for quote in quotes:
        print(quote.get_text())
else:
    print('Failed to retrieve the web page.')