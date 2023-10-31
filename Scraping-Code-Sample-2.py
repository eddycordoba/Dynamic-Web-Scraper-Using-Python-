# Import the required libraries
import time
from bs4 import BeautifulSoup
import csv

# This is a dummy dataset to simulate scraped data
dummy_data = [
    {
        "Owner Name": "John Doe",
        "Chapter": "Chapter 1",
        "Company Name": "ABC Inc.",
        "City": "Sample City",
        "Industry": "Sample Industry",
        "Phone Number": "123-456-7890",
        "Email": "johndoe@example.com"
    },
    {
        "Owner Name": "Jane Smith",
        "Chapter": "Chapter 2",
        "Company Name": "XYZ Corp.",
        "City": "Sample Town",
        "Industry": "Another Industry",
        "Phone Number": "987-654-3210",
        "Email": "janesmith@example.com"
    }
]

# Save the dummy data to a CSV file
csv_filename = "Sample_Data.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["Owner Name", "Chapter", "Company Name", "City", "Industry", "Phone Number", "Email"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row
    csv_writer.writeheader()
    
    # Write each data row
    for data_point in dummy_data:
        csv_writer.writerow(data_point)

# Use of dummy data!
print("This is a sample of the kind of data that can be scraped with the project. Actual data has been anonymized and replaced with fictional data.")



