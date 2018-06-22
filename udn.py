from selenium import webdriver
from time import sleep

import requests 
import re
from bs4 import BeautifulSoup
import json

my_url = 'https://udn.com/news/breaknews/1/7#breaknews'
outFile = 'udn_test.txt'
articlesNum = 0

#chromeDriver = "/home/sophia/Desktop/nima-scripts/webCrawler/chromedriver"
driver = webdriver.Firefox()
driver.get(my_url)
'''
    first, we use selenium to find all links
'''

def find_all_link_View():
    links = []
    views = []
# FIND ALL LINKS
    scroll_down = driver.find_elements_by_class_name('bbox')
    # find_element_by_link_text('link文字')
    driver.execute_script("arguments[0].scrollIntoView();", scroll_down[0])
    scroll_down[0].click()
    sleep(10)

    title_element = driver.find_elements_by_css_selector('h2 a')
    views = driver.find_elements_by_class_name('view')

    postNum = len(title_element)
    for i in range(postNum):
        driver.execute_script("arguments[0].scrollIntoView();", title_element[i])
        print('link: ')
        print (title_element[i].get_attribute('href'))
        links.append(title_element[i].get_attribute('href'))
        print (title_element[i].text)
        print (views[i].text)
        views.append(views[i].text)

    print ('link number=', postNum)

    return links , views
'''
    Second, we use beautifulSoup(x) selenium(o) to find post content
'''
def get_post_content(link):
    post_url = link
    print("=== reading links: " + post_url + " ===")
    print("===")
    post_r = requests.get(post_url + ".html")
    #driver_post = webdriver.Chrome(chromeDriver)
    #driver_post.get(post_url)
    post_soup = BeautifulSoup(post_r.text, 'html.parser')

    return post_soup
'''
    Third, we survey every post and output the database spec to file
'''
def analyze_and_output(post_soup, view,link):
    catagory = post_soup.find('nav')
    tags = []
    tags_a = catagory.find_all('a')
    tags_b = catagory.find_all('b')
    for t in tags_a:
        tags.append(t.getText())
    for t in tags_b:
        tags.append(t.getText())
    topic = post_soup.find('h1', {'class': 'story_art_title'}).getText()
    
    content = []
    content = post_soup.find_all('p')
    for p in content:
        content.append(p)
    popularity = view.text
    date = post_soup.find('div', {'class': 'story_bady_info_author'}).getText()


    #tags = catagory.split('/')
    #popularity = popularity.split()
    print ('content', content)
    date = date.split()
    print('date split:', date)
    sleep(10)
    modifiedDate = (date[0] + ' ' + date[1])


    datatest = [ {  'link': link,
                    'tags' : tags,
                    'Date' : modifiedDate, 
                    'popularity' : popularity, 
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


# FIND content IN post

links, views = find_all_link_View()
for i in range(len(links)):
    print('the ', articlesNum,' th article')
    print (links[i])
    post_soup = get_post_content(links[i])
    analyze_and_output(post_soup, views[i],links[i])
    articlesNum +=1
driver.close()

