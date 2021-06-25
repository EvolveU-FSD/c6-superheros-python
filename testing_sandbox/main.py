from bs4 import BeautifulSoup
from lxml import etree
import requests
base = 'https://metanumbers.com/prime-numbers'
page = requests.get(base)
content = str(page.content)
content = content.split('<body>')[1]
content = content.split('</body>')[0]
content = '<body>'+content+'</body>'
print(content)
doc = etree.fromstring(content)
n = doc.xpath('/body')
for m in n:
    print(m)


# base = 'https://en.wikipedia.org'
# page = requests.get(base + '/wiki/List_of_comic_book_sidekicks')
# soup = BeautifulSoup(page.content,'html.parser')

# tables = soup.find_all(class_="wikitable")
# superheros = []
# for table in tables:
#     rows = table.find_all("tr")
#     for row in rows:
#         cols = row.find_all("td")
#         try:
#             superhero = cols[2].text.strip() or None
#             sidekick = cols[0].text.strip() or None
#             wikipage = cols[2].find('a')
#             year = cols[4].text
#             wiki = None
#             if wikipage:
#                 wiki = wikipage.get('href')
#             superheros.append({"name":superhero, "sidekick":sidekick, "wiki":wiki, "year":year})
#         except Exception as e:
#             print(e, cols)
# superheros.sort(key=lambda x: x['year'] or '0')
# names = {}
# final_list = []
# for superhero in superheros:
#     if superhero['name'] in names:
#         pass
#     else:
#         final_list.append(superhero)
#         names[superhero['name']]=None
# for super in final_list:
    
#     if super['wiki']:
#         page = requests.get(base + super['wiki'])
#         soup = BeautifulSoup(page.content,'html.parser')
#         info_box = soup.find(class_="infobox")
#         if info_box:
#             rows = info_box.find_all('tr')
#             for row in rows:
#                 header = row.find('th')
#                 if header:
#                     if header.text == 'Alter ego':
#                         alterego = row.find('td')
#                         for el in alterego.find_all('br'):
#                             el.replace_with('\n')
                        
#                         super['alterego']= alterego.text.split('\n')[0]
# import json
# f=open('superheros.json','w')
# f.write(json.dumps(final_list))
# f.close