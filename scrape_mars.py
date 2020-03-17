# Import Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import requests
import datetime 
import pymongo
from pprint import pprint

def init_browser():
# Splinter access browser and Chrome opens web site
    executable_path = {"executable_path": "/Users/Areli/Desktop/web-scraping-challenge/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_facts_data = {}

    #Visiting NASA url
    url='https://mars.nasa.gov/news/'
    browser.visit(url)

    html=browser.html
    soup=bs(html,'html.parser')

    #Scraping the latest news title and news paragraph
    news_title = soup.find("div",class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    print(f"news_title: {news_title}")
    print(f"news_p: {news_p}")

    #Scraping images
    image_url_featured ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url_featured)

    #HTML Object
    img_html=browser.html

    #Parse HTML with BS
    soup=bs(img_html, 'html.parser')

    # Retrieve background-image url from style tag 
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url 
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = main_url + featured_image_url

    # Display full link to featured image
    featured_image_url

    #Using Mongodb to obtain twitter facts
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Declare the database
    db = client.nasa_db

    # Declare the collection
    collection = db.nasa_db

    # Declare the database for weather reports
    db = client.twitter_db

    # Declare the collection
    collection = db.twitter_db


    #get mars weather's latest tweet from the website
    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)

    html_weather = browser.html
    soup = bs(html_weather, "html.parser")

    latest_tweets = soup.find_all('p', class_='TweetTextSize')

    # Loop through returned results
    for latest_tweet in latest_tweets:
        # Error handling
        try:
            # Identify and return title of listing
            report = result.text.strip()
            print('mars_weather: ', report)
            print('---------------')

        except Exception as e:
            print(e)

    mars_facts_url = 'https://space-facts.com/mars/'

    # Used class example 09-panda scraping
    tables = pd.read_html(url)
    tables

    # table first element
    df = tables[0]
    df.columns = ['Comparision', 'Mars', 'Earth']
    df

    # table second element
    df = tables[1]
    df.columns = ['Fun Facts', 'Earth']
    df

    url_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemispheres)

    # Scrap 4 images
    urls = [
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
        'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    ]

    # create empty dictionary to collect images
    image_data = []

    # for loop through m_urls list and perform some web scraping logic for each link
    for url in urls:
        print(url)

        # create empty dictionary
        album = {}
        
        # click link
        browser.visit(url)
        
        # Scrape the image from the img element
        m_html = browser.html
        m_scraper = bs(m_html, 'html.parser')
        
        # scrape the title and image url
        m_title = m_scraper.find('h2', {'class': 'title'}).get_text()
        
        # add title to album
        album['title'] = m_title
    
        # add image to album
        image_data.append(album)
        
        # go back a page in the browser
        browser.back()

        image_data

    # close brower 
    browser.quit()