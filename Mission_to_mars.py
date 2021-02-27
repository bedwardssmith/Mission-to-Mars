#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Import Spliter and BeatifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup

# Import dependencies
import pandas as pd


# In[2]:


# set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit the mars nasa news site
url = 'http://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[6]:


# setup the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[7]:


# assign the title and summary text to variables 
slide_elem.find("div", class_="content_title")


# In[9]:


# Use the parent element to find the first 'a' tag and save it as "news_title"
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images
# 

# In[11]:


# Visist URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[12]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[14]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[15]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[16]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'


# In[20]:


# scrape a table using Pandas
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[23]:


# convert data frame back to html
df.to_html()


# In[24]:


# quit browser
browser.quit()

