## Scraping of HTML pages by url

# -------------- Imports -------------

import json

from utils import try_request

from bs4 import BeautifulSoup

from newspaper import Article

# -------------- Global variables -------------

terms = ["esquizofrenia", "esquizofrénico", "esquizfrenico", "esquizofrénica", "esquizofrenica", "esquizofrénicas", "esquizofrenicas", "esquizofrénicos", "esquizofrenicos", "esquizofrenicamente", "esquizofrenizar"]

# -------------- Main functions ------

def get_data(item):

    timeout = 100
    attempts = 3
    url = item["linkToOriginalFile"]
    journal = item["journal"]
    data = {}
    data["journal"]=journal
    
    page = try_request(endpoint=url, timeout=timeout, attempts=attempts)
    if not page: print("Error in scraping: can't get the page")

    try: soup = BeautifulSoup(page.content, 'html.parser')
    except: print("Error in scraping: can't get the page content")

    if True:
        content = scrap_publico(item["title"], soup)
        if content != None: 
            data["content"] = content
            return data

    return None

        

def scrap_publico(headline, soup):
    content = ""
    try:
        div = soup.find('div',attrs={"class":"entry-body"})
    except:
        try:
            div = soup.find('div',attrs={"class":"noticia"}) 
        except:
            try:
                div = soup.find('div', attrs={"class":"content"})
            except:
                try:
                    div = soup.find('div', attrs={"class":"immersive-story-body"})
                except:
                    try:
                        div = soup.find('div', attrs={"class":"main-content"})
                    except:
                        try:
                            div = soup.find('div', attrs={"class":"story__body"})
                        except:
                            try:
                                div = soup.find('div', {'id': 'texto'})
                            except:
                                try:
                                    div = soup.find('span', {'class': 'ultnottxt'})
                                except:
                                    try:
                                        div = soup.find('div', {'id': 'ctl00_ContentPlaceHolder1_DivNoticia'})
                                        content = div.find('span', {'id': 'ctl00_ContentPlaceHolder1_txtTextos'})
                                        content = content.text
                                        if any(term in content for term in terms):
                                            return content
                                        else: return None
                                    except:
                                        try:
                                            div = soup.find('div', {'id': 'caixasNoticias'})
                                            div = div.find('div', {'id': 'texto'})
                                        except:
                                            print(headline + "   |   Can't scrap.")
                                            print("----------------------------------")
                                            return None
    try:
        for paragraph in div.find_all('p'):
            if paragraph.text not in content:
                content+=paragraph.text+" "
                #print("CONTENT: "+content.text+"\n")   
                #print(headline + "   |   Scaping successful.")
                #print("----------------------------------")
    except:
        try:
            for paragraph in div.find_all('aux'):
                if paragraph.text not in content: content+=paragraph.text+" " 
        except:
            print(headline + "   |   Can't scrap.")
            print("----------------------------------")
            return None
    
    if any(term in content for term in terms):
        return content
    else: return None      

  