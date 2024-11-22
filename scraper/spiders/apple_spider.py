from pathlib import Path
from bs4 import BeautifulSoup
import scrapy

class AppleSpider(scrapy.Spider):
  name = "apple"

  def start_requests(self):
    urls = [
      'https://jobs.apple.com/en-us/search?location=united-states-USA&search=data&sort=relevance&page=1',
      'https://jobs.apple.com/en-us/search?location=united-states-USA&search=data&sort=relevance&page=2'
    ]

    for url in urls:
     yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    page = response.request.url[-1]
    filename = f"apple-{page}.html"
    Path(filename).write_bytes(response.body)
    self.log(f"Saved file {filename}")