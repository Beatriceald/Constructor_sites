import requests
from requests_html import HTMLSession
import os

def icon(query):
    s = HTMLSession()
    #query = input('Enter keyword here: ')
    #endpage = int(input('How many pages do you want to scrape: '))
    endpage = 2
    #create download folder
    cur_dir = os.getcwd()
    output = cur_dir + f'/{query}'
    if not os.path.exists(output):
        os.mkdir(output)
    #create urls variable
    urls = ['https://www.flaticon.com/search/{}?word={}&type=icon'.format(x, query) for x in range(1, endpage)]
    for url in urls:
        r = s.get(url)
        content = r.html.find('div.icon--holder')
        for icon in content:
            icon_title = icon.find('img', first=True).attrs['alt']
            icon_url = icon.find('img', first=True).attrs['data-src']
            return(icon_url)
            




q = 'constructor'

""" Парсер иконки """
def icons():
    data = {'apikey': '0c12c50f7d1b99f083308e547b7e8aeb4660f49f', 'q': 'constructor'}
    request = requests.post('https://api.flaticon.com/v3/app/authentication', data)
    icon = requests.get('https://api.flaticon.com/v3/app/search/icons/', q)
    print (request)

#icons()

    r = request.json()
    if 'data' in r:
        if 'token' in r['data']:
            try:
                #token = requests.get()
                icon = requests.get('https://api.flaticon.com/v3/app/search/icons/', q)
                for i in icon:
                    print(i)
                    #return r['data']['token']
                #return icon
            except(IndexError, TypeError):
                return 'Server Error'
    return 'Server Error 404'

if __name__ == '__main__':
    weather = icons()
    print(weather)

# код воркин - возвращает BearerToken 
# нужно доделать парсер иконки через get запрос к иконкам