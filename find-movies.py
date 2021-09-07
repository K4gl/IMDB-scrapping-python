import requests
from bs4 import BeautifulSoup 

number0fMovies=input("enter the number of movies you want to view")

ReqMovies=requests.get("https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+number0fMovies)
parsedMovies=BeautifulSoup(ReqMovies.content,"html.parser")
 
for i in parsedMovies.findAll("div", class_="lister-item mode-advanced"):
    print(i.h3.a.text)
    print(i.find("span", class_="genre").text)
    print(i.find("div", class_="inline-block ratings-imdb-rating").text)
    print("https://www.imdb.com/title/tt0111161/?ref_=adv_li_tt"+(i.a.get("href")))
    print(i.find("img", class_="loadlate").get("loadlate"))
    print("*"*50)

