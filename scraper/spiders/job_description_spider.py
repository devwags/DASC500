from pathlib import Path
from tools import *
from const import ROOT_DIR
import scrapy
import json

class JobDescriptionSpider(scrapy.Spider):
  name = "job_descriptions"

  def start_requests(self):
    jobs = make_jobs()

    for job in jobs:
     yield scrapy.Request(url=job['link'], callback=self.parse, meta={'job': job})

  def parse(self, response):
    job = response.meta['job']

    # Do something with the response
    soup = BeautifulSoup(response.body, 'html.parser')
    job['summary'] = extract_summary(soup)
    job['description'] = extract_description(soup)
    job['key_qualifications'] = extract_key_quals(soup)
    job['minimum_qualifications'] = extract_min_quals(soup)
    job['preferred_qualificaitons'] = extract_pref_quals(soup)
    job['pay_range'] = extract_pay_range(soup)

    # Write jobs to csvs
    filename = f'{ROOT_DIR}/site_data/jobs/jobs.json'
    with open(filename, 'a') as fp:
      json.dump(job, fp, indent=4, ensure_ascii=False)
      fp.write(',')
    self.log(f"Saved file {filename} for job {job['id']}")