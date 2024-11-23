from pathlib import Path
from const import ROOT_DIR
import scrapy

class AppleSpider(scrapy.Spider):
  name = "apple"

  def start_requests(self):
    for i in range(1,78):
     yield scrapy.Request(url=f'https://jobs.apple.com/en-us/search?location=united-states-USA&search=data&sort=relevance&page={i}', callback=self.parse)

  def parse(self, response):
    page = response.request.url
    suffix = str(page).split('=')[-1]
    filename = f"apple-{suffix}.html"
    Path(f'{ROOT_DIR}/site_data/apple/{filename}').write_bytes(response.body)
    self.log(f"Saved file {filename}")