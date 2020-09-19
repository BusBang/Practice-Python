import bs4
import urllib.request

url = "https://www.forbes.com/global2000/#35589333335d"
html = urllib.request.urlopen(url)
bsobj = bs4.BeautifulSoup(html, "html.parser")
print(bsobj.text)
value_bsobj = bsobj.find('section', {"id":"row-5"})
print(value_bsobj)
# print(value_bsobj.find("h2").text)