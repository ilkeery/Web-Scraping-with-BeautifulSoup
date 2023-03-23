import requests
from bs4 import BeautifulSoup as bs

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
page = requests.get(url)
soup = bs(page.content, "html.parser")

results = soup.find("tbody", class_="lister-list").find_all("tr",limit=10)
class Movie:
    def __init__(self,name,year,rating):
        self.name = name
        self.year = year
        self.rating=rating
    def __str__(self):
        return f"Movie's name: {self.name.ljust(50)} year: {self.year} rating: {self.rating}"
    
names = []
years = []
ratings = []        
movies = []
movieCount = 0
print("Top 10 IMDB movies.\n")
for i in results:
    names.append(i.find("td", class_="titleColumn").find("a").text)
    years.append(i.find("td", class_="titleColumn").find("span").text.strip("()"))
    ratings.append(i.find("td", class_="ratingColumn imdbRating").text.strip())
    movieCount += 1

print(movieCount)
for n in range(movieCount):
    movies.append(Movie(name=names[n],year=years[n],rating=ratings[n]))

for i in range(movieCount):
    print(movies[i])



