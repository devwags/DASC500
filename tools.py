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

def extract_summary(tag_element):
  print(f'Manual Interject: ')
  summary = tag_element.find('div', {'id': 'jd-job-summary'})
  if summary is not None:
    return summary.find('span').contents[0]
  return None


def extract_description(tag_element):
  description = tag_element.find('div', {'id': 'jd-description'})
  if description is not None:
    return description.find('span').contents[0]
  return None

def extract_min_quals(tag_element):
  quals = tag_element.find('div', {'id': 'jd-minimum-qualifications'})
  if quals is not None:
    results = []
    list_items = quals.find_all('li', {'role': 'listitem'})
    for li in list_items:
      results += li.find('span').contents
    return results
  return None

def extract_pref_quals(tag_element):
  quals = tag_element.find('div', {'id': 'jd-preferred-qualifications'})
  if quals is not None:
    results = []
    list_items = quals.find_all('li', {'role': 'listitem'})
    for li in list_items:
      results += li.find('span').contents
    return results
  return None

def extract_key_quals(tag_element):
  quals = tag_element.find('div', {'id': 'jd-key-qualifications'})
  if quals is not None:
    results = []
    list_items = quals.find_all('li', {'role': 'listitem'})
    for li in list_items:
      results += li.find('span').contents
    return results
  return None

def extract_education_experience(tag_element):
  xp = tag_element.find('div', {'id': 'jd-education-experience'})
  if xp is not None:
    return xp.find('span').contents[0]
  return None

def extract_pay_range(tag_element):
  pay_element = tag_element.find('div', {'id': 'jd-posting-supplement-footer-0'})
  if pay_element is not None:
    pay_string = str(pay_element.find('span').contents[0])
    pay_range = re.findall('\$.....?.0', pay_string)
    return pay_range
  return None