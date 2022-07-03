import requests
import lxml
from bs4 import BeautifulSoup

def latest(manga_url):
  url = manga_url
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
  }
  f = requests.get(url, headers = headers)
  soup = BeautifulSoup(f.content, 'lxml')
  movies = soup.find('div', {
      'class': 'panel-story-chapter-list'
    }).find_all('a')
  return movies[0].next_element, len(movies)


