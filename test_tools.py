from bs4 import BeautifulSoup
from tools import *

def test_extract_title():
  test_html = '<a class="table--advanced-search__title" id="jotTitle_PIPE-200571456" href="/en-us/details/200571456/data-analyst-retail-store-analytics?team=CORSV">Data Analyst: Retail Store Analytics</a>'
  soup = BeautifulSoup(test_html, 'html.parser')
  assert extract_title(soup) == 'Data Analyst: Retail Store Analytics'

def test_extract_link():
  test_html = '<a class="table--advanced-search__title" id="jotTitle_PIPE-200571456" href="/en-us/details/200571456/data-analyst-retail-store-analytics?team=CORSV">Data Analyst: Retail Store Analytics</a>'
  soup = BeautifulSoup(test_html, 'html.parser')
  assert extract_link(soup) == 'https://jobs.apple.com/en-us/details/200571456/data-analyst-retail-store-analytics?team=CORSV'

def test_extract_location():
  test_html = '<span id="storeName_container_PIPE-200550159">Austin</span>'
  soup = BeautifulSoup(test_html, 'html.parser')
  assert extract_location(soup) == 'Austin'

def test_get_job_links():
  jobs = [
    {
      'id': 1524,
      'title': 'Apple Music Data Engineering Software Engineer',
      'link': 'https://jobs.apple.com/en-us/details/200561894/apple-music-data-engineering-software-engineer?team=SFTWR',
      'location': 'Cupertino'
    },
    {
      'id': 1525,
      'title': 'SSP Data User Studies Research Engineer',
      'link': 'https://jobs.apple.com/en-us/details/200577892/ssp-data-user-studies-research-engineer?team=HRDWR',
      'location': 'Cupertino'
    }
  ]
  assert get_job_links(jobs) == [
    'https://jobs.apple.com/en-us/details/200561894/apple-music-data-engineering-software-engineer?team=SFTWR',
    'https://jobs.apple.com/en-us/details/200577892/ssp-data-user-studies-research-engineer?team=HRDWR'
  ]