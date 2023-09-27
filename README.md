# notion-take-home

# Book Review Management Script

## Description

This Python script manages book reviews by interacting with a Notion database. It reads book review data from a CSV file, calculates book metrics, and updates the Notion database with the latest information.

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
     python script_name.py
     ```

## Questions and Answers

- **Was there anything you got stuck on, and if so what did you do to resolve it?**
  - I did not encounter any specific issues while reviewing the code. However, if you encounter errors or issues when running the script, please check your environment variables, CSV file format, and Notion API key and database ID.

- **Do you have any suggestions for improving the API documentation to make it clearer or easier to use?**
  - The provided API documentation for the `main` function is already clear and informative. To make it even clearer, consider adding more specific examples or usage scenarios.

## Sources

- [Notion API Documentation](https://developers.notion.com/docs/getting-started)
  - This documentation provides information on how to use the Notion API to interact with Notion databases.

## Libraries Used

- **Notion Client Library (`notion_client`)**: Used for interacting with the Notion API to read and update data in the Notion database.
- **Python-Dotenv Library (`python-dotenv`)**: Used for loading environment variables from the 'take-home.env' file.




Next step to-dos: 
- Add unit tests to run the scripts on a variety of different csv files and starting databases and ensure that the output is always the same (baed on the csv file)
-     #TODO: Add checks to ensure that the the CSV is properly formatted with the correct schema
      #TODO: Add logic to handle duplicate entires
