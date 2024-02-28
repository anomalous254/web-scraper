from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from termcolor import colored

page = 0
data = []

banner_name = '''                                                                                                                    
     ##### #     ##                                       ##               ##### /                    /                 
  ######  /#    #### /                                     ##           ######  /                   #/                  
 /#   /  / ##    ###/                                      ##          /#   /  /                    ##                  
/    /  /  ##    # #                                       ##         /    /  /                     ##                  
    /  /    ##   #                                         ##             /  /                      ##                  
   ## ##    ##   # ##   ####      /###   ###  /###     ### ##    /###    ## ##              /###    ## /###     /###    
   ## ##     ##  #  ##    ###  / / ###  / ###/ #### / ######### / ###  / ## ##             / ###  / ##/ ###  / / #### / 
   ## ##     ##  #  ##     ###/ /   ###/   ##   ###/ ##   #### /   ###/  ## ##            /   ###/  ##   ###/ ##  ###/  
   ## ##      ## #  ##      ## ##    ##    ##    ##  ##    ## ##    ##   ## ##           ##    ##   ##    ## ####       
   ## ##      ## #  ##      ## ##    ##    ##    ##  ##    ## ##    ##   ## ##           ##    ##   ##    ##   ###      
   #  ##       ###  ##      ## ##    ##    ##    ##  ##    ## ##    ##   #  ##           ##    ##   ##    ##     ###    
      /        ###  ##      ## ##    ##    ##    ##  ##    ## ##    ##      /            ##    ##   ##    ##       ###  
  /##/          ##  ##      ## ##    /#    ##    ##  ##    /# ##    ##  /##/           / ##    /#   ##    /#  /###  ##  
 /  #####            #########  ####/ ##   ###   ###  ####/    ######  /  ############/   ####/ ##   ####/   / #### /   
/     ##               #### ###  ###   ##   ###   ###  ###      ####  /     #########      ###   ##   ###       ###/    
#                            ###                                      #                                                 
 ##                   #####   ###                                      ##                                               
                    /#######  /#                                                                                        
                   /      ###/                                                                                          
'''
sub_heading = "Web Scraper for Python Script"

name_color = 'blue'
sub_heading_color = 'yellow'

banner = colored(banner_name, name_color) + '\n' + colored(sub_heading, sub_heading_color)

print(banner)


while True:
    page += 1
    url = f'https://www.jumia.co.ke/catalog/?q=phones&page={page}#catalog-listing'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'lxml')

        content = soup.find_all('article', class_='prd _fb col c-prd')

        for i in content:
            dic = {}
            link = i.find('a', class_='core')['href']
            name = i.select_one('.info h3.name').text.strip()
            price = i.select_one('.info div.prc').text.strip()

            dic['NAME'] = name
            dic['PRICE'] = price
            dic['LINK'] = link

            data.append(dic)
            
        

    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
    print( colored(f'\n[ + ] Total data Scraped {len(data)} data ', 'blue'))
    print(f'\n[info] Sleeping for 5s ')
    print('*'* 30)

    df = pd.DataFrame(data)
    df.to_excel('data.xlsx', index=False)
   
    time.sleep(5)

    if page == 10:
        print('Stoping scraping')
        break