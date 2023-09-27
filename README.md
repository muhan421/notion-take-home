# Nahum Maru - Intern Take Home Exercise
## Description

This Python script manages book reviews by interacting with a Notion database. It reads book review data from a CSV file, calculates book metrics (the average rating and the number 5 star ratings) for each book, and updates the Notion database with this latest information. 

## How to Run the Program

1. **Set up your environment:**
   - Make sure you have Python installed on your system.
   - Create a 'take-home.env' file with your Notion API key and database ID.
   - Prepare a CSV file 'ratings.csv' with your book review data (book title, reviewer, rating).

2. **Install Dependencies:**
   - You can use `pip` to install the necessary libraries. Run the following command:
     ```
     pip install notion-client python-dotenv
     ```

3. **Execute the Script:**
   - Run the program by executing the Python script in your terminal:
     ```
     python main.py
     ```

## Running Tests

**Execute `test.py`:**
   - Run the program by executing the Python script in your terminal:
     ```
     python test.py
     ```
**To add tests:**
   - Go to test.py and add test functions to the `TestBookFunctions` class

## Reflections
- ** **
- **Was there anything you got stuck on, and if so what did you do to resolve it?**
  - During the development process, I faced a crucial decision point where I had to determine how to handle updates to existing book review entries in the Notion database. One option was to delete and recreate pages when updates were needed, while the other was to adopt an approach that never deletes pages but instead modifies or adds a page. Within this latter approach, there was also the question of whether the script should update every page with the correct info or if it should check each page to see that it has incorrect info (and needs to be updated) before actually updating the page (to minimize API calls for modifying the page).  After careful consideration, I chose the latter approach that only updates pages when the current page has incorrect data. This ensures that existing data remains intact and avoids unnecessary deletion or duplication of pages. This decision was made to provide a more robust and user-friendly solution for managing book reviews, even if it posed certain complexities in updating existing entries. Further, through preliminary expiriemnts, I found that the latter approach is more efficent than the former and that the additional API calls for checking if a page had incorrect data were less computationally expensive than the additional API calls needs to modify each page (to avoid checking for incorrect data). I quickly tested this via time trials — there is defintely more expiriments to be done and potentially, a more efficient approach. 
- **Suggestions for improving the API documentation to make it clearer or easier to use.**
  - In my experience, the API documentation is very effective at covering the absolute basics. However, I did the feel that the Python SDK was very limited in the number of examples it offered. Having more coverage in the types of examples given and also providing a true UI (like the JS SDK) would make using the Python SDK much easier.


## Sources

- [Notion API Documentation](https://developers.notion.com/docs/getting-started)
  - This documentation provides information on how to use the Notion API to interact with Notion databases.

## Libraries Used

- **Notion Client Library (`notion_client`)**: Used for interacting with the Notion API to read and update data in the Notion database.
- **Python-Dotenv Library (`python-dotenv`)**: Used for loading environment variables from the 'take-home.env' file.

## Next Steps

Here are some next steps to consider for enhancing this script:

- **Add Unit Tests:** Develop unit tests to run the script on a variety of different CSV files + starting databases and check that the corresponding is always the same for different starting databases to ensure idempotency (was unable to implement due to time contraints).
- **CSV Format Checks:** Implement checks to ensure that the CSV file is properly formatted with the correct schema. This can include verifying the presence of required columns and data types.
- **Duplicate Entry Handling:** Add logic to handle duplicate entries in the Notion database. Consider options such as merging duplicate entries or providing clear notifications for users when duplicates are detected.

Feel free to prioritize and implement these next steps to further improve the functionality and reliability of the script.
