from bs4 import BeautifulSoup
import requests
import csv

def get_cast(movie_id):
    url = 'https://www.imdb.com/title/'+movie_id+'/fullcredits'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    cast_list = [a.text.strip() for a in soup.select('table.cast_list td:nth-of-type(2) a')]
    return(cast_list)

url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
movie_list = [a.attrs.get('href')[7:16] for a in soup.select('td.titleColumn a')]
actors_dict = {}
for movie in movie_list:
    cast_list = get_cast(movie)
    print(cast_list)
    for actor in cast_list:
        count_actor = actors_dict.get(actor, 0)
        actors_dict[actor] = count_actor + 1
all_actors = sorted(actors_dict.items(), key=lambda x: x[1], reverse=True)
best_actors = all_actors[:5]
print(best_actors)
with open("best_actors.csv", "w") as f:
    wr = csv.writer(f, delimiter="\n")
    wr.writerow(best_actors)

