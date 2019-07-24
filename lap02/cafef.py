from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel


url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

data = urlopen(url).read().decode("utf8")

html_content = data

soup = BeautifulSoup(html_content,"html.parser")
div = soup.find("div",style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")

table = div.find("table", id="tableContent")

datas=[]
tr_list = table.find_all("tr")
for tr in tr_list :
    td_list = tr.find_all("td")
    
    for td in td_list :
        data={}
        data['names'] = td.string
        # print(td.string)
        # print("*"*60)
        datas.append(data)

pyexcel.save_as(records=datas, dest_file_name="cafe.xls")
# print(datas)


