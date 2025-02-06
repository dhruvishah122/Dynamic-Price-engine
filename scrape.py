# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import csv
# from pymongo import MongoClient

# # Replace with your connection string
# connection_string = "mongodb+srv://dhruvishah116122:Dbms#amazon122@cluster0.ozm10.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Connect to the MongoDB client
# client = MongoClient(connection_string)

# # Access the database
# db = client['priceEngine']  # Replace with your database name

# # Access the collection
# collection = db['Product']  # Replace with your collection name

# # Fetch all documents in the collection
# documents = collection.find()  # Returns a cursor

# # Convert to a list if needed
# documents_list = list(documents)

# # Print each document
# for doc in documents_list:
#     driver = webdriver.Firefox()

# # Replace with the desired Amazon search URL
#     name = doc.get("name", "Unknown") 
#     brand = doc.get("brand", "Unknown")
#     string=" ".join([brand,name])
#     search_url = "https://www.amazon.in/s?k={}".format(string)

# # List to store scraped data
#     product_data = []

#     try:
#         # Navigate to the Amazon search page
#         driver.get(search_url)

#         # Wait for the page to load
#         time.sleep(5)

#         # Find product elements (you can adjust the element's class name based on the HTML structure)
#         name_elements = driver.find_elements(By.CLASS_NAME, "a-size-medium.a-spacing-none.a-color-base.a-text-normal")
#         price_elements = driver.find_elements(By.CLASS_NAME, "a-price-whole")
#         tag_elements1 = driver.find_elements(By.XPATH, '//span[contains(@class, "a-badge a-icon-alt")]')
#         rating_elements = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label*="out of 5 stars"]') 
        
#         for i in range(min(10, len(name_elements))):  # Limit to 10 products
#             try:
#                 name = name_elements[i].text.strip()
#             except Exception as e:
#                 name = "Not Available"
            
#             try:
#                 price = price_elements[i].text.strip()
#             except Exception as e:
#                 price = "Not Available"
            
#             try:
#                 rating = rating_elements[i].get_attribute('aria-label')
#             except Exception as e:
#                 rating = "Not Available"

#             try:
#                 tags = [tag.text.strip() for tag in tag_elements1[i:i+1]]  # Grab each tag
#                 tags_str1 = ", ".join(tags)
#             except Exception as e:
#                 tags_str1 = "No Tags"

#             # Add the scraped data for this product to the list
#             product_data.append([name, price, rating,tags_str1])

#         # Print the scraped data
#         for data in product_data:
#             print(f"Product Name: {data[0]}")
#             print(f"Price: {data[1]}")
#             print(f"Rating: {data[2]}")
#             print(f"Tags: {data[3]}")
#             print("="*50)

#     finally:
#         # Close the browser once done
#         driver.quit()

#     # Save the scraped data to a CSV file
#     with open("iphone_amazon_search_data.csv", "w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Name", "Price", "Rating", "Tags"])  # Write the header
#         writer.writerows(product_data)  # Write the product data rows

#     print("Data saved to iphone_amazon_search_data.csv")


#     # Initialize the Firefox WebDriver

from selenium import webdriver
from model import fun
from selenium.webdriver.common.by import By
import time
import csv
from pymongo import MongoClient

# Replace with your connection string
connection_string = "mongodb+srv://dhruvishah116122:Dbms#amazon122@cluster0.ozm10.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to the MongoDB client
client = MongoClient(connection_string)

# Access the database and collection
db = client['priceEngine']
collection = db['Product']

# Fetch all documents in the collection
documents = list(collection.find())  # Convert cursor to a list

# Initialize the browser
driver = webdriver.Firefox()

# Iterate through all documents in the collection
for index, doc in enumerate(documents, start=1):
    # Extract name and brand
    name = doc.get("name", "Unknown").replace(" ", "_")  # Replace spaces for file naming
    brand = doc.get("brand", "Unknown").replace(" ", "_")
    search_query = " ".join([brand, name])
    
    # Construct the Amazon search URL
    search_url = f"https://www.amazon.in/s?k=best seller+{search_query}"
    print(f"Processing {index}: Searching for: {search_query} | URL: {search_url}")
    
    # List to store product data for the current document
    product_data = []
    
    try:
        # Navigate to the Amazon search page
        driver.get(search_url)
        time.sleep(7)  # Adjust wait time as needed

        # Scrape product details
        name_elements = driver.find_elements(By.CLASS_NAME, 'a-size-base-plus')        
        price_elements = driver.find_elements(By.CSS_SELECTOR, '.a-price .a-price-whole')
        rating_elements = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label*="out of 5 stars"]')
        
        for i in range(min(40, len(name_elements))):
            try:
                product_name = name_elements[i].text.strip()
            except Exception:
                product_name = "Not Available"
            
            try:
                price = price_elements[i].text
            except Exception:
                price = "Not Available"
            
            try:
                rating = rating_elements[i].get_attribute('aria-label')
            except Exception:
                rating = "Not Available"
            
            
            # seller_sales=100
            # seller_price=400
            # seller_stock=20
            product_data.append([product_name, price, rating,100,20,2000])
            
    except Exception as e:
        print(f"Error processing {search_query}: {e}")
    print(product_data)
    # Save the current document's data to a separate CSV file
    csv_filename = f"{brand}_{name}_search_data.csv"
    with open("product_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Comp_name", "Comp_price", "Comp_rating","seller_sales","seller_stock","seller_price"])  # Write headers
        writer.writerows(product_data)  # Write product data rows
    fun()
    print(f"Data for {search_query} saved to product_data.csv")
    
# Close the browser after all documents are processed
driver.quit()
