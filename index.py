
import requests
from bs4 import BeautifulSoup
import json

def get_page():
    url = 'https://movie.douban.com/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url,headers)
    return response.text

def  parse_page(text):
    soup = BeautifulSoup('text','lxml')
    lists = soup.find_all('li',attrs = {'data-actors':'张优 / 宋词'})
    for li in lists:
        actors = li['data-actors']
        print(actors)


if __name__ == '__main__':
    text = get_page()
    parse_page(text)



