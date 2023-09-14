import random
import requests
from bs4 import BeautifulSoup

# This project relies on:
# 1. BeautifulSoup: `pip install beautifulsoup4` or `pip3 install beautifulsoup4`
# 2. Requests: `pip install requests` or `pip3 install requests` 
# Further documentation can be found on:
# https://pypi.org/project/beautifulsoup4/
# https://pypi.org/project/requests/


# Create headers
HEADERS = ({'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# Send a request to the amazon search and get the response
response = requests.get("https://www.amazon.com/s?i=aps&k=inkless%20pen&ref=nb_sb_noss&url=search-alias=aps", headers=HEADERS)

# Parse the HTML content of the response with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the search results on the page
search_results = soup.find_all('div', {'data-component-type': 's-search-result'})

# Create a list to store the prices
prices = []

# Loop through the first 10 search results
for i in range(10):
    result = search_results[i]
    # get the price of the product
    price = result.find('span', {'class': 'a-offscreen'}).text.replace('$', '')
    # Append the price to the list
    prices.append(float(price))
    
# Create a list of prices for the first 10 pieces of search results
product_name = "Inkless pens"
# prices = [17.73, 88.90, 22.59, 28.90, 27.20, 34.00, 30.60, 18.15, 67.15, 32.30]

# Print the message
print("I am interested in ", product_name)

# Find and print the maximum price
maximum_price = max(prices)
print("The highest price is", maximum_price)

# Find and print the minimum price
minimum_price = min(prices)
print("The lowest price is", minimum_price)


# Find and print the median price
prices.sort()
median_price = (prices[len(prices)//2] + prices[len(prices)//2-1])/2
print("The median price is %.2f"% median_price)

# Find and print the average of the maximum and minimum prices
average_price = (maximum_price+minimum_price)/2
print("The average is %.2f" % average_price)

# Compare the average to the median
median_is_larger = median_price > average_price
print("The median is larger than the average? ", median_is_larger)

# Insert the product name to the first position of the list
prices.insert(0, product_name)
print("The updated list with product name is: ", prices)

# Remove the highest price on the list
prices.remove(maximum_price)
print("The updated list without the highest price is: ", prices)

# random number range from 0 to length of the list to select a favorite product
random_number = random.randint(0, len(prices)-1)
# Create another list
favorite_product = ["My favorite product", prices[random_number]]
# Add the favorite product list to the end of the previous list
prices.append(favorite_product)
print("The final list is: ", prices)