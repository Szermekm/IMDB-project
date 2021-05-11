from bs4 import BeautifulSoup
import requests


def scrape_cast(movie_id):
    url = 'https://www.imdb.com/title/'+movie_id+'/fullcredits'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    cast_list = [a.text.strip() for a in soup.select('table.cast_list td:nth-of-type(2) a')]
    return(cast_list)

def scrape_top_chart():
    url = 'https://www.imdb.com/chart/top/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    movie_list = [a.attrs.get('href')[7:16] for a in soup.select('td.titleColumn a')]
    actors_dict = {}
    for movie in movie_list:
        cast_list = scrape_cast(movie)
        for actor in cast_list:
            count_actor = actors_dict.get(actor, 0)
            actors_dict[actor] = count_actor + 1
    all_actors = sorted(actors_dict.items(), key=lambda x: x[1], reverse=True)
    return all_actors[:5]