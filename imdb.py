import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/chart/top')

#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)

links = (soup.select('.titleColumn'))

#subtext = (soup.select('.ratingColumn imdbRating'))
subtext = (soup.select('.lister-list'))
#print(subtext[0].getText())

#print(links[0].getText())
#subtext = (soup.select('.subtext'))

def Get_Title(links):
    t = []
    y = []
    Movie = tuple()
    for link in links:
        name = link.getText()
        name = name.split('\n')
        t.append(name[2].strip())
        y.append(name[3].strip())
        Movie = (t,y)
    return Movie

title,year = Get_Title(links)



def Get_All(subtext):
    t = []

    for text in subtext:
        name = text.getText().strip()
        name = name.split('\n')

        t.append(name)

    return t

rating = Get_All(subtext)


next_movie_rating = 5
Rating = []
#250 is number of elements in year and title
for i in range(0,250):

    Rating.append(rating[0][next_movie_rating])
    next_movie_rating += 36


#print(rating)
#print(title)
#print(year)
#print(Rating)

Movie = list(zip(title,year,Rating))
for m in Movie:
    print(m)


