import json

import csv

def main():
    csv_columns = ['journal','headline','content','authors','publishDate','archiveDate','linkToArchive']
    dic_space = {"journal":"-","headline":"-","content":"-","authors":"-","publishDate":"-","archiveDate":"-","linkToArchive":"-"}
    with open('output_scraping') as scraping_file: data = json.load(scraping_file)
    temp = []
    duplicate = False
    with open("repeated.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        for entry in data:
            if len(temp) != 0:
                for entry_temp in temp:
                    if len(entry["content"]) < len(entry_temp["content"]): 
                        if entry["content"] in entry_temp["content"]: 
                            duplicate = True
                            writer.writerow(entry)
                            writer.writerow(entry_temp)
                            writer.writerow(dic_space)
                            break
                    elif len(entry_temp["content"]) < len(entry["content"]): 
                        if entry_temp["content"] in entry["content"]: 
                            duplicate = True
                            writer.writerow(entry)
                            writer.writerow(entry_temp)
                            writer.writerow(dic_space)
                            break
                    else: 
                        if entry_temp["content"]==entry["content"]: 
                            duplicate = True
                            writer.writerow(entry)
                            writer.writerow(entry_temp)
                            writer.writerow(dic_space)
                        break
                        
                if duplicate==False: temp.append(entry)
                else: duplicate = False
            else: temp.append(entry)
    csvfile.close()
    return temp


main()