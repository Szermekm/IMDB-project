# IMDB Webscraping documentation

***

*Program Name:* IMDB Webscraping

*Author:* Mátyás Szermek

*Created:* 29/04/2021

*Version:* 1.0.0

***

## Table of contents

1. Development environment
2. Dependencies
   - BeautifulSoup
   - Requests
   - gspread
   - schedule
3. Usage	
4. Python file description

***
## 1. Development environment

To run this programm you need Python version 3+, the pip package manager and the external packages listed in the dependencies to be installed on your machine. You will also need a Google Cloud Project with a Google Service Account.
A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs.
How to set up the Google Cloud Project: 
 1. Create a Google Cloud Project
 2. Enable Sheets API
 3. Create a service account
 4. Generate a new key for the service account
 5. Save the key as `client_secret.json` into the projects root library
 6. Create a Google sheet with the list of emails in the first column and share it with the service account

***

## 2. Dependencies


### BeautifulSoup

BeautifulSoup is used to parse html documents. In this program this library is used to filter and select classes from the retrived DOM structure. 

### Requests

This library is used to send http requests, enabling us to download html pages from the IMDB website.

### gspread

This library is used to read and write Google Spreadsheets. This library provides an interface for working with Google Sheets API.

### schedule

This library is used to schedule jobs periodically. It used to schedule the execution of the programm for every week.

## 3. Usage

To use the programm run the following command in the terminal: 

`python main.py EMAIL_SHEET_URL`

EMAIL_SHEET_URL is the URL of the Google Sheet where the email addresses are listed in the first column and that is shared with the Google Service Account. 

***

## 4. Python file description

The program extracts the movie IDs from the specific movie links.

#### scraping.py

The scrape_cast function downloads the cast of each inserted movie IDs.

The scrape_top_chart function collects the movie IDs from the top250 chart page of IMDB and calls scrape_cast function for each movie ID and returns the 5 most frequently found actors.

#### main.py

The job function contains the main functionality of the programm and is scheduled to run every week on Monday.

The best_actors list contains the 5 actors with the most appearances in the cast_list and their number of appearances.

With the gspread library we create a new empty Google Sheet and we write the top 5 actors in to the first column. 

Then we open the Google Sheet with the email addresses, read the email addresses from the first column and we share the sheet containing the actors with all email address.

All email addresses will receive a message that the Spreadsheet has been shared with them.

***

