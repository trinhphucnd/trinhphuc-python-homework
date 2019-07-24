from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url ="https://www.apple.com/itunes/charts/songs/"

data = urlopen(url).read().decode("utf8")

html_content = data

soup = BeautifulSoup(html_content,"html.parser")

section = soup.find("section","section chart-grid")
div =section.find("div","section-content")

li_list = div.find_all("li")

datas = []

for li in li_list:
    data={}
    
    a =li.h3.a
    b =li.h4.a

    data['artists'] = b.string
    data['names'] = a.string
    datas.append(data)
    
# pyexcel.save_as(records=datas, dest_file_name="information.xls")

count = 0
for data in datas:
    options = {
        'default_search': 'ytsearch', 
        'max_downloads': 1
    }
    dl = YoutubeDL(options)
    keysearch = (datas[count]['artists']+datas[count]['names'] )
    dl.download([keysearch])
    count += 1

