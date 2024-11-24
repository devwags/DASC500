from pathlib import Path
from tools import make_jobs, get_job_links
from const import ROOT_DIR
import scrapy

class JobDescriptionSpider(scrapy.Spider):
  name = "job_descriptions"

  def start_requests(self):
    jobs = make_jobs()

    for job in jobs:
     yield scrapy.Request(url=job['link'], callback=self.parse, meta={'job': job})

  def parse(self, response):
    job = response.meta['job']

    # Do something with the response

    # Write jobs to csvs
    filename = f"job_description-{}.html"
    Path(f'{ROOT_DIR}/site_data/jobs/{filename}').write_bytes(response.body)
    self.log(f"Saved file {filename}")