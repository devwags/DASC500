#job
# {
#   id:
#   title:
#   location:
#   link:
#   description:
#     summary:
#     description:
#     minimum_qualifications:
#     preferred_qualifications:
#     key_qualifications:
#     pay_and_benefits:

from bs4 import BeautifulSoup
from const import ROOT_DIR
import requests


with open(f'{ROOT_DIR}/site_data/test_pages/test_job_description_2.html', 'wb') as file:
  r = requests.get('https://jobs.apple.com/en-us/details/200573469/data-engineer?team=HRDWR')
  file.write(r.content)