from pathlib import Path
from bs4 import BeautifulSoup
from const import ROOT_DIR
import re

def extract_title(tag_element):
  title = tag_element.find('a', {'id': re.compile('jotTitle*')}).contents[0]
  return title

def extract_link(tag_element):
  link_prefix = 'https://jobs.apple.com'
  link_suffix = tag_element.find('a', {'id': re.compile('jotTitle*')})['href']
  return link_prefix+ link_suffix

def extract_location(tag_element):
  location = tag_element.find('span', {'id': re.compile('storeName*')}).contents[0]
  return location

def get_job_links(jobs):
  job_links = []
  for job in jobs:
    job_links.append(job['link'])
  return job_links

def make_jobs():
  files = Path(f'{ROOT_DIR}/site_data/apple').glob('*')
  jobs = []
  id = 1
  for file in files:
    with open(file) as fp:
      soup = BeautifulSoup(fp, 'html.parser')
      tbody_elements = soup.find_all('tbody', {'id': re.compile('accordion_(PIPE|REQ)*')})
      for element in tbody_elements:
        job = {}
        job['id'] = id
        job['title'] = extract_title(element)
        job['link'] = extract_link(element)
        job['location'] = extract_location(element)
        jobs.append(job)
        id += 1
  return jobs