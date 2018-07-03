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
    proxyData = {}
    if rowData and rowData[4] and rowData[4].text == 'elite proxy':
        proxyData['ip'] = rowData[0].text
        proxyData['port'] = rowData[1].text
        proxyData['https'] = rowData[6].text
        proxies.append(proxyData)

#random_proxies = random.sample(proxies,k=10)
# random_proxies = proxies[:10]
random_proxies = proxies
proxyStrings = []
for proxy in random_proxies:
    url = ''
    if proxy['https'] == 'yes':
        # url = url + 'https'
        # url = url + '://' + proxy['ip'] + ':' + proxy['port']
        url = url +  proxy['ip'] + ':' + proxy['port']

        proxyStrings.append(url)
    # else:
    #     url = url + 'http'
            
    # url = url + '://' + proxy['ip'] + ':' + proxy['port']
    # proxyStrings.append(url)

print(proxyStrings)