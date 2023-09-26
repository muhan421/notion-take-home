import csv
import os
import sys
from pprint import pprint
from notion_client import Client

def get_notion_api_key():
    # Retrieve the Notion API token from the environment vars
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        print("Could not load .env because python-dotenv not found.")
        sys.exit(1)

    # Load environment variables from 'take-home.env'
    load_dotenv('take-home.env')
    NOTION_KEY = os.getenv('NOTION_KEY', "")
    return NOTION_KEY

def get_database_id():
    # Retrieve the Database ID from the environment vars
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        print("Could not load .env because python-dotenv not found.")
        sys.exit(1)

    # Load environment variables from 'take-home.env'
    load_dotenv('take-home.env')
    DATABASE_ID = os.getenv('DATABASE_ID', "")
    return DATABASE_ID

# Remove extra whitespace and convert to lowercase
def clean_book_title(title):
    cleaned_title = title.strip().lower()
    return cleaned_title

# Extracts book title, rating, and number of favorites from a Notion page retrieval response
def process_page_retrival_response(results):
    book_title = results['properties']["Book Title"]["title"][0]["text"]["content"]
    rating = results['properties']["Rating"]["number"]
    num_favorites = results['properties']["Favorites"]["number"]
    return book_title, rating, num_favorites

# Adds a new page to a Notion database with the given data.
def add_page_to_db(notion, database_id, page_data):
    book_title, avg_rating, num_favorites = page_data

    # Create a new page structure with properties for book title, rating, and favorites.
    new_page = {
        "Book Title": {
            "title": [
                {
                    "text": {
                        "content": book_title
                    }
                }
            ]
        },
        "Rating": {
            "number": avg_rating
        },
        "Favorites": {
            "number": num_favorites 
        }
    }

    # Create the new page in the Notion database.
    notion.pages.create(parent={"database_id": database_id}, properties=new_page)

# Checks the status of a book entry in the Notion database.
# Return Schema: If an entry for the given book-title exists, if that entry is the same as the one in the given data, page_id in the notion db (if book exists)
def check_book_status_in_db(notion, book_title, page_data):
    results = notion.databases.query(
        **{
            "database_id": get_database_id(),
            "filter": {"property": "Book Title", "title": {"equals": book_title}},
        }
    ).get("results")

    # Check for duplicate entries in the database.
    #TODO: Add logic to handle duplicate entires
    if len(results) > 1: 
        print("Error: Duplicate entires in database!!")
     
    if not results: 
        return False, False, None

    page_id = results[0]['id']
    results = notion.pages.retrieve( **{ "page_id": page_id })
    curr_book_title, curr_avg_rating, curr_num_favorites = process_page_retrival_response(results)
    book_title, avg_rating, num_favorites = page_data

    # Compare the retrieved data with the given data to determine if an update is needed.
    if curr_book_title == book_title and curr_avg_rating == avg_rating and curr_num_favorites == num_favorites:
        return True, True, page_id
    else:
        return True, False, page_id

# This function modifies an existing page in the Notion database with new data.
def modify_page(notion, page_id, page_data):
    book_title, avg_rating, num_favorites = page_data
    
    # Create a new page structure with updated properties for book title, rating, and favorites.
    new_page = {
        "Book Title": {
            "title": [{
                "text": {
                    "content": book_title
                }
            }]
        },
        "Rating": {
            "number": avg_rating
        },
        "Favorites": {
            "number": num_favorites 
        }
    }
    
    # Update the page in the Notion database with the new data.
    results = notion.pages.update( **{ "page_id": page_id, "properties": new_page })

# This function reads and processes data from a CSV file and returns a dictionary of book data.
def collect_data_from_csv(file_name): 
    book_data = {}
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            # Process data here
            book_title, reviewer, rating = row
            book_title = clean_book_title(book_title)
            rating = float(rating)
            
            # Handle the creation of the book title entry in book data.
            if book_title not in book_data: book_data[book_title] = {}
            book_entry = book_data[book_title]

            # Store reviewer ratings in the book entry.
            book_entry[reviewer] = rating
    return book_data

# Calculates book metrics such as average rating and the count of 5-star reviews for a given book.
def calc_book_metrics(book_name, book_entry):
    ratings = book_entry.values()
    
    # Calculate the average rating of the book, rounded to 2 decimal places.
    avg_rating = round(sum(ratings) / len(ratings), 2)
    
    # Count the number of 5-star reviews for the book.
    fav_count = 0
    for rating in ratings:
        if rating == 5: fav_count += 1
    return book_name, avg_rating, fav_count

'''
This is the main function that orchestrates the data processing and Notion database 
interactions to maintain a Notion database of book reviews, ensuring that the database
is up-to-date with the latest book review data from the 'ratings.csv' file.
'''
def main(file_name):
    # Retrieve the Notion API key and database ID.
    notion_key = get_notion_api_key()
    database_id = get_database_id()
    
    # Initialize the Notion client.
    notion = Client(auth=notion_key)

    # Collect book data from the CSV file.
    #TODO: Add checks to ensure that the the CSV is properly formatted with the correct schema
    book_data = collect_data_from_csv(file_name)

    for book_title in book_data.keys():
        # Calculate book metrics for the current book.
        page_data = calc_book_metrics(book_title, book_data[book_title])
        
        # Check the status of the book in the Notion database.
        book_in_db, exact_page_in_db, page_id = check_book_status_in_db(notion, book_title, page_data)
        if book_in_db:
            if not exact_page_in_db:
                # Modify the page entry if it exists but needs updating.
                modify_page(notion, page_id, page_data)
        else:
            # Add a new page entry to the database if it doesn't exist.
            add_page_to_db(notion, database_id, page_data)
        

if __name__ == '__main__':
    main("ratings.csv")