#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:37:18 2018

@author: lijinjin
"""


import requests
from bs4 import BeautifulSoup

# define the function and transit id and page_number to page_url
def getReviews(movie_id):
    reviews=[]
    num = 1
    pnum = str(num)
    url='https://www.rottentomatoes.com/m/'+ movie_id + '/reviews/?page=' + pnum + '&sort='
# start the while loop to choose page
    while url!= None:
        page = requests.get(url)
        if page.status_code!=200: url=None
        else:
            num += 1
            pnum = str(num)
            url='https://www.rottentomatoes.com/m/'+ movie_id + '/reviews/?page=' + pnum + '&sort='
# use BeautifulSoup to analyse the web content            
            soup=BeautifulSoup(page.content,'html.parser')
            divs=soup.select('div#reviews div div div div div.review_area')
            for idx, div in enumerate(divs):
                date=None
                desc=None
                scor=None
# get date
                div_date=div.select('div.review_date')
                if div_date!=[]: date=div_date[0].get_text()
# get description
                div_desc=div.select('div.the_review')
                if div_desc!=[]: desc=div_desc[0].get_text()
# get score
# if there's no score, return 'No Score'
                div_scor=div.select('div.review_desc div.small')
                if div_scor!=[]: scor=div_scor[0].get_text()
                scor = scor.split('|')
                if len(scor) == 2: scor = scor[1]
                else:  scor = 'No Score'    
                reviews.append((date, desc, scor))
    if len(reviews) == 0: 
        return 'Movie Not Found'
    else:
        return reviews

if __name__ == "__main__":
    movie_id='finding_dory'
    reviews=getReviews(movie_id)
    print('the length of reviews is:',len(reviews))