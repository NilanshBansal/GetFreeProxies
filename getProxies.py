import urllib
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore",category=UserWarning,module="bs4")
import random

headers=[
        ('Host', "free-proxy-list.net"),
        ('Accept', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"),
        ('Accept-Language', "en-GB,en-US;q=0.9,en;q=0.8"),
        ('X-Requested-With', "XMLHttpRequest"),
        ('Referer', "url"),
        ('Connection', "keep-alive"),
        ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"),  #Keep this as last because of pop used
]

proxy_type = input("https? yes or no: ")

opener=urllib.request.build_opener()
opener.addheaders=headers

url='https://free-proxy-list.net/'

response=opener.open(url)

soup=BeautifulSoup(response)

proxyListTable = soup.find("table",{"id":"proxylisttable"})

allRows = proxyListTable.findAll("tr")

proxies=[]
for row in allRows:
    rowData = row.findAll('td')
    url = ''
    if rowData and rowData[4] and rowData[4].text == 'elite proxy' and rowData[6].text == proxy_type:
        url = url + rowData[0].text + ':' + rowData[1].text
        proxies.append(url)

print(proxies)