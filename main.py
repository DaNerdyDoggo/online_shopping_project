import requests
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
  try:
    session = HTMLSession()
    response = session.get(url)
    return response

  except requests.execptions.RequestsExceptions as e:
    print(e)


def get_results(query):
  query = urllib.parse.quote_plus(query)
  response = get_source("http://www.google.com/search?q=" + query)
  return response

def parse_results(response):

  
  css_identifier_result = ".tF2Cxc"
  css_identifier_title = 'h3'
  css_identifier_link = '.yuRUbf a'

  results = response.html.find(css_identifier_result)
  output = []
  
  for result in results:
    item = {
      'title': result.find(css_identifier_title, first=True).text,
      'link': result.find(css_identifier_link, first=True).attrs['href']
    }
    output.append(item)
   
  return output

def google_search(query):
  response = get_results(query)

  return parse_results(response)

print(google_search('Levi Figure'))