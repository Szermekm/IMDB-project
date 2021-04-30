# IMDB Webscraping documentation

***

*Program Name:* IMDB Webscraping

*Author:* Mátyás Szermek

*Created:* 29/04/2021

*Version:* 1.0.0

***

## Table of contents

1. Supporting libraries
   - BeautifulSoup
   - Requests
   - CSV
2. Python file description

***

### BeautifulSoup

In this program this library is used to filter and select classes from the retrived DOM structure. 

***

### Requests library

This library is used to send the request to IMDB's website, enabling the communication through IMD's exposed API.

***

### CSV Library

This library is used to generate the output of the program in CSV format.

***



### Python file description

The program extracts the movie IDs from the specific movie links.

The get_cast function inserts the movie IDs in to the "fullcredits" URLs.

The function scrapes through the 250 cast list with BeautifulSoup and creates the variable cast_list.

The for loop counts the appearances of actors in the list.

The best_actors list contains the 5 actors with the most appearances in the cast_list and their number of appearances.

The csv library writes the best_actors list to a csv file named best_actors.csv.

