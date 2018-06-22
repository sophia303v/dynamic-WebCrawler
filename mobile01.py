# encoding:utf-8

import requests 
import re
from bs4 import BeautifulSoup
import json
import time # for debug

category = { # category url in "game"
    'Misc.': 'https://www.mobile01.com/forumtopic.php?c=23',
    'SonyPlayStation' : 'https://www.mobile01.com/forumtopic.php?c=23&s=37',
    'XboxOne/Xbox360': 'https://www.mobile01.com/topiclist.php?f=282',
    'Nintendo': 'https://www.mobile01.com/forumtopic.php?c=23&s=38',
    'Blizzard': 'https://www.mobile01.com/forumtopic.php?c=23&s=39',
    'EA': 'https://www.mobile01.com/forumtopic.php?c=23&s=40',
    'onlineGame': 'https://www.mobile01.com/forumtopic.php?c=23&s=43',
    'PCGame': 'https://www.mobile01.com/topiclist.php?f=283',
    'webGame': 'https://www.mobile01.com/topiclist.php?f=334',
    'mobileGame': 'https://www.mobile01.com/forumtopic.php?c=23&s=41',
    'GameMisc.': 'https://www.mobile01.com/topiclist.php?f=179',
    'perpherial': 'https://www.mobile01.com/topiclist.php?f=685',
    'VR': 'https://www.mobile01.com/topiclist.php?f=737'
}

# fetch all links in this category

def get_all_links():
    links = []
    for page in pages:
        print(url + "&p=" + str(page) + ".html")
        print("===")
        r = requests.get(url + "&p=" + str(page)+ ".html")
        soup = BeautifulSoup(r.text, 'html.parser')
        forum = soup.findAll('span', {'class': 'subject-text'})  # find the forum list
        for info in forum:
            link = ""
            try:
                link = info.findAll('a', href=True)[0]
                if link.get('href') != '#':
                    links.append(base_url + link.get("href"))
                    #print(base_url + link.get("href"))
                    #print('===')
            except:
                link = None
    linksNum = len(links)
    return links
#def read_linksFile(file):
# 這個沒用到
def output_linksFile(links):
    flo = open('linksf_game_sonyPlaystation','a')
    for link in links:
        flo.write(link)
        flo.wrtie('\n')
    flo.close()    
    
# fetch content in one article
def get_post_content(link):
    post_url = link
    print("=== reading links: " + post_url + " ===")
    print("===")
    post_r = requests.get(post_url + ".html")
    post_soup = BeautifulSoup(post_r.text, 'html.parser')

    return post_soup

# analyze the post content and output to file
def analyze_and_output(post_soup):
    tag = post_soup.find('p', {'class':'nav'}).getText()
    topic = post_soup.find('h1', {'class': 'topic'}).getText()
    content = post_soup.find('div', {'class': 'single-post-content'}).getText()
    popularity = post_soup.find('div', {'class': 'info'}).getText()
    date = post_soup.find('div', {'class': 'date'}).getText()

    tags = []

    tags = tag.split('»')
    popularity = popularity.split()

    date = date.split()
    modifiedDate = (date[0] + ' ' + date[1])


    datatest = [ {  'link': link,
                    'tags' : tags,
                    'Date' : modifiedDate, 
                    'popularity' : popularity[1], 
                    'content' : content, 
                    'topic' : topic
                     } ]
    
    jsonfile = json.dumps(datatest,ensure_ascii=False,sort_keys=True)
    print(jsonfile)

    # file Output
    fo = open(outFile,"a")
    #fo.write("#" + str(articleNum))
    fo.write(jsonfile)
    fo.write('\n')
    fo.close()

# Initial url setting

base_url = "https://www.mobile01.com/"   # the prefix url of post page
url = category['SonyPlayStation']  # the url of category, now is "game -> sonyPlaystation"
outFile = "game_sonyPlayStation_5.txt"
pages = range(5, 6)  # the range of page. Because I can only fetch 5 articles with the robust Internet, I only set 1 page a time. 
linksNum = 0        # for debug
articlesNum = 25     # 網路斷掉時，看斷在哪個文章, 從那個文章開始

# main:

print("===== Starts to fetch =====")
print("===== Getting all links... =====")
links = get_all_links()
#output_linksFile(links)
del links[0:articlesNum]  
print("===== fetching each article... =====")
for link in links:
    print('the ', articlesNum,' th article')

    post_soup = get_post_content(link)
    analyze_and_output(post_soup)
    articlesNum +=1

print('linksNum = ', linksNum)
print('articlesNum = ', articlesNum)
