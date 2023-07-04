##################################################
#                                                #
#    AppStoreVersionChecker Script               #
#                                                #
#    Version: 0.1                                #
#    Developed by: Pavan                         #
#    GitHub: https://github.com/pavan2318/       #
#                                                #
##################################################

# Usage: python appstore_version_checker.py
# -------------------------------------------
# This script retrieves the current running version of an application on the Apple App Store.
# It prompts the user to enter the Apple App Store URL for the application and then fetches
# the version information from the App Store webpage's response.

# Prerequisites:
# - Python 3.x
# - Requests library (Install using 'pip install requests')
# - Beautiful Soup library (Install using 'pip install beautifulsoup4')

# Changelog:
# -------------------------------------------
# Version 0.1 (2023-07-01):
# - Initial release of AppStoreVersionChecker
# - Added functionality to retrieve the current running version
# - Implemented parsing of HTML response to extract version information
# - Provided a command-line interface for user interaction
# - Supported customization of the App Store URL

import requests
from bs4 import BeautifulSoup

# Accept URL from the user
url = input("Enter the Apple Play Store URL for the application: ")

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element with the specified class
    element = soup.find(class_="l-column small-6 medium-12 whats-new__latest__version")

    if element:
        # Extract the value
        value = element.text.strip()
        print("Current running version:", value)
    else:
        print("Element not found.")
else:
    print("Error:", response.status_code)
