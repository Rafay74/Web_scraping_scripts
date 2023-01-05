from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for links in bs.find_all('a'):
  if 'href' in links.attrs:
    print(links) # this will print all the <a> 
    print(links.attrs['href'])  # without tags , their content
