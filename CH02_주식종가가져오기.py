from bs4 import BeautifulSoup as bs
import requests as req

url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = bs(res.text, "html.parser")

# for title in soup.select("a.tltle"):
#     print(title.get_text(strip=True))
    
for tr in soup.select("table.type_5 tr"):
    if len(tr.select("a.tltle")) == 0: # 크롬 개발자도구를 100% 신뢰하지마라 필요시 페이지 소스보기를 해라
        continue
    title = tr.select("a.tltle")[0].get_text(strip=True)
    price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
    print(title,price,change)