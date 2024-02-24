from bs4 import BeautifulSoup
import requests
import time

page = 0

while True:
    page += 1
    url = f'https://www.jumia.co.ke/catalog/?q=phones&page={page}#catalog-listing'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'lxml')

        content = soup.find_all('article', class_='prd _fb col c-prd')

        for i in content:
            link = i.find('a', class_='core')['href']
            name = i.select_one('.info h3.name').text.strip()
            price = i.select_one('.info div.prc').text.strip()
            print(f"Name: {name} : {price}")
            print(f"Link: https://www.jumia.co.ke{link}")
            print('\n')
            
        

    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

    print('sleeping for 5s')
    time.sleep(5)

    if page == 10:
        print('Stoping scraping')
        break