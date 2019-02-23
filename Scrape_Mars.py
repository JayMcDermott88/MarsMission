#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()



# In[8]:


NASAurl = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
response=requests.get(NASAurl)


# In[12]:


soup = bs(response.text, 'html.parser')
print(soup.prettify())


# In[13]:


NASA_title = soup.title.text
print(NASA_title)


# In[21]:


NASA_news = soup.find_all('div', class_='content_title')[0].find('a').text.strip()
print(NASA_news)


# In[24]:


NASA_p = soup.find_all('div', class_='rollover_description_inner')[0].text.strip()
print(NASA_p)


# In[44]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[45]:


SpaceURL = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(SpaceURL)


# In[46]:


html = browser.html
soup_image = bs(html, 'html.parser')


# In[47]:


URLlink = soup_image.find_all('a', class_='button fancybox')[0].get('data-fancybox-href')


# In[48]:


featured_image_url = "https://www.jpl.nasa.gov" + URLlink

print(featured_image_url)


# In[49]:


browser.visit(featured_image_url)


# In[50]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[51]:


TwitterURL = "https://twitter.com/marswxreport?lang=en"
browser.visit(TwitterURL)


# In[52]:


html = browser.html
soup_tweet = bs(html, 'html.parser')


# In[56]:


mars_weather = soup_tweet.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[0].text.strip()
print(mars_weather)


# In[57]:


FactsURL = "https://space-facts.com/mars/"


# In[63]:


facts = pd.read_html(FactsURL)
facts


# In[65]:


df = facts[0]
df.columns = ['Description', 'Values']
df


# In[67]:


df.to_html('Facts.html')


# In[68]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[69]:


USGSURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(USGSURL)


# In[71]:


html = browser.html
soup_USGS = bs(html, 'html.parser')


# In[72]:


hemisphere= []


# In[73]:


dict={}


# In[ ]:


results = soup_ISGS.find_all('h3')


# In[ ]:


#for result in results

