## Scraping of HTML pages by url

# -------------- Imports -------------

import json

from newspaper import Article

# -------------- Main functions ------

## Web scraping and filtering
def get_data(item):

    terms = ["Esquizofrenia", "esquizofrenia", "Esquizofrénico", "esquizofrénico", "Esquizofrenico", "esquizofrenico", "Esquizofrénica", "esquizofrénica", "Esquizofrenica", "esquizofrenica", "Esquizofrénicas", "esquizofrénicas", "Esquizofrenicas", "esquizofrenicas", "Esquizofrénicos", "esquizofrénicos", "Esquizofrenicos", "esquizofrenicos", "Esquizofrenicamente", "esquizofrenicamente", "Esquizofrenizar", "esquizofrenizar"]
    data = {}

    try:
        page = Article(item["linkToOriginalFile"], language="pt")
        page.download()
    except: print("Error in scraping: can't get the page")

    try:
        page.parse()
        page.nlp()

        title = page.title
        content = page.text
        authors = page.authors
        publish_date = page.publish_date

        if any(term in title for term in terms) or any(term in content for term in terms):
            data["headline"] = title
            data["journal"] = item["journal"]
            data["content"] = content
            data["authors"] = authors
            data["publishDate"] = str(publish_date)
            data["archiveDate"] = str(item["tstamp"])
            data["linkToArchive"] = item["linkToArchive"]

            data = clean(data)

            return data   

    except:
        print("Can't scap. | " + item["linkToArchive"])

    return None


# -------------- Auxiliae functions ------

## Clean unnecessary info and normalize
def clean(data):

    data["content"] = data["content"].replace("\n", " ")
    if "DN Online: " in data["headline"]: data["headline"] = data["headline"].replace("DN Online: ", "")
    if "JORNAL PUBLICO: " in data["headline"]: data["headline"] = data["headline"].replace("JORNAL PUBLICO: ", "")
    if "EXPRESSO On.Line:" in data["headline"]: data["headline"] = data["headline"].replace("EXPRESSO On.Line:", "")
    if "EXPRESSO: " in data["headline"]: data["headline"] = data["headline"].replace("EXPRESSO: ", "")
    if " 00:00:00" in data["publishDate"]: data["publishDate"] = data["publishDate"].replace(" 00:00:00", "")

    if len(data["archiveDate"]) > 7:
        year_archive = data["archiveDate"][0:4]
        month_archive = data["archiveDate"][4:6]
        day_archive = data["archiveDate"][6:8]
        data["archiveDate"] = year_archive + '-' + month_archive + '-' + day_archive


    title = data["headline"].lower()
    content = data["content"].lower()
    authors = data["authors"]
    
    if len(title) > 0:
        if title in content: # remove title from content
            data["content"] = data["content"].replace(title, "")
    
    if len(authors)!=0:
        for author in authors: # remove authors from content
            author = author.lower()
            if ("por " + author) in content:
                data["content"] = data["content"].replace(("por " + author), "")
                break
            elif author in content:
                data["content"] = data["content"].replace(author, "")
    
    if data["journal"] in content: # remove journal URL from content
        data["content"] = data["content"].replace(data["journal"], "")

    return data
        
    



        
