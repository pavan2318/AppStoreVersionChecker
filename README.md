# AppStoreVersionChecker
## Introduction

Welcome to the **AppStoreVersionChecker** project!

### Overview
The AppStoreVersionChecker is a Python script designed to retrieve the current running version of an application on the Apple App Store. This script aims to simplify the process of obtaining the latest version information of an application by automating the retrieval from the App Store website.

### Benefits
Using the AppStoreVersionChecker script provides several benefits:
- **Convenience**: Instead of manually visiting the App Store website and searching for the application's version, this script automates the process, saving time and effort.
- **Automation**: The script fetches the application version by searching for a specific HTML element in the App Store webpage's response. It eliminates the need for manual inspection or data extraction.
- **Integration**: The script can be easily integrated into other projects or workflows, allowing developers to programmatically retrieve the current version information for their applications.

### Prerequisites and Dependencies
Before using the AppStoreVersionChecker script, ensure you have the following prerequisites and dependencies in place:
- **Python**: The script requires Python 3.x to run. If you don't have Python installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Requests Library**: The script uses the `requests` library to send HTTP requests to the Play Store website. You can install it using `pip` with the following command: `pip install requests`
- **Beautiful Soup**: The script utilizes the `BeautifulSoup` library to parse and extract data from HTML content. Install it using `pip` with the following command: `pip install beautifulsoup4`

## Installation

To use the PlayStoreVersionChecker script, follow the steps below to install and set up the project.

### System Requirements
- Python 3.x

### Step 1: Clone the Repository
Clone the PlayStoreVersionChecker repository to your local machine using the following command:

```
git clone https://github.com/your-username/PlayStoreVersionChecker.git
```
### Step 2: Navigate to the Project Directory
Navigate to the project directory by executing the following command:
cd PlayStoreVersionChecker

### Step 3: Install Dependencies
The script relies on the requests and beautifulsoup4 libraries. Install them by running the following command:
```
pip install -r requirements.txt
```
### Step 4: Run the Script
You are now ready to run the PlayStoreVersionChecker script. Execute the following command:
```
python appstore_version_checker.py
```
The script will prompt you to enter the Apple Play Store URL for the application. Once you provide the URL, it will fetch the current running version of the application and display it on the console.
