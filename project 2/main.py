import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def printList(arr):
  for item in arr:
    print(item)

r = requests.get("https://www.statbunker.com/")
c = r.content
soup = bs(c, "html.parser")

all = soup.find_all("div", {"class":"intRight"})
all = all[0]
all = all.find_all("a", {"class":"pointer"})
links = []
for item in all:
  arr = {}
  arr["name"] = item.text
  arr["href"] = item["href"]
  links.append(arr)

for link in links:
  print(link["name"])
  List = []
  r = requests.get(link["href"])
  c = r.content
  soup = bs(c, "html.parser")
  info = soup.find("tbody").findAll('tr')
  for tr in info:
    temp = []
    item = tr.findAll("td")
    temp.append(item[1].find("div").text)
    temp.append(item[2].text)
    temp.append(item[3].text)
    temp.append(item[4].text)
    temp.append(item[5].text)
    temp.append(item[6].text)
    temp.append(item[7].text)
    temp.append(item[8].text)
    temp.append(item[9].text)
    List.append(temp)
  
  df = pd.DataFrame(List, columns=["Clubs","Matches played","Matches won","Matches drawn","Matches lost","Goals for","Goals against","Goal difference","Points"])
  df.to_csv(link["name"]+".csv",index=False)

