from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel


url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

data = urlopen(url).read().decode("utf8")

html_content = data

soup = BeautifulSoup(html_content,"html.parser")
div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")

table = div.find("table", id="tableContent")

datas = []

tr_list = table.find_all("tr")
for tr in tr_list:
    data = {}
    td_list = tr.find_all("td","b_r_c")
    for td in td_list:
        
        data[''] = td_list[0].string.lstrip()
        data['Quý 1'] = td_list[1].string
        data['Quý 2'] = td_list[2].string
        data['Quý 3'] = td_list[3].string
        data['Quý 4'] = td_list[4].string
        if td ==td_list[0]:
            break
    datas.append(data)
    
pyexcel.save_as(records=datas, dest_file_name="cafe.xls")

print(datas)