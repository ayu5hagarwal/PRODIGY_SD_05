import requests
from bs4 import BeautifulSoup
import csv

def scrape_products(url):
    """Scrapes product information from an e-commerce website.

    Args:
        url: The URL of the e-commerce website.

    Returns:
        A list of dictionaries, where each dictionary represents a product with its name, price, and rating.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the elements containing product information (adjust selectors as needed)
    product_containers = soup.find_all('div', class_='product-container')

    products = []
    for container in product_containers:
        name = container.find('h3', class_='product-title').text.strip()
        price = container.find('span', class_='product-price').text.strip()
        rating = container.find('span', class_='product-rating').text.strip()
        products.append({'name': name, 'price': price, 'rating': rating})

    return products

def save_to_csv(products, filename):
    """Saves the scraped product data to a CSV file.

    Args:
        products: A list of dictionaries representing the products.
        filename: The name of the CSV file.
    """

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'price', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

if __name__ == '__main__':
    url = 'https://www.example.com/products'  # Replace with the actual URL
    products = scrape_products(url)
    save_to_csv(products, 'products.csv')