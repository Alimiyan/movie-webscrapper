import requests
import lxml
from bs4 import BeautifulSoup

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = "https://www.rottentomatoes.com/top/bestofrt/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
f = requests.get(url, headers = headers)
movies_lst = []
soup = BeautifulSoup(f.content, 'lxml')
movies = soup.find('table', {
    'class': 'table'
  }).find_all('a')
num = 0
for anchor in movies:
    urls = 'https://www.rottentomatoes.com' + anchor['href']
    movies_lst.append(urls)
    num += 1
    movie_url = urls
    movie_f = requests.get(movie_url, headers = headers)
    movie_soup = BeautifulSoup(movie_f.content, 'lxml')
    movie_content = movie_soup.find('div', {
    'class': 'movie_synopsis clamp clamp-6 js-clamp'
    })
    print(colors.OKGREEN, num,':', 'Movie: ' + anchor.string.strip(), colors.ENDC,'\n','url: ', urls, '\n',)
    print('Movie info: ' + movie_content.string.strip())
    print("-" * 90)