from bs4 import BeautifulSoup
from tools import *
from const import ROOT_DIR
import pytest
import re

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

def test_extract_summary():
  with open(f'{ROOT_DIR}/site_data/test_pages/test_job_description_1.html') as file:
    test_html = BeautifulSoup(file, 'html.parser')

  assertion_string = ("Apple is a place where extraordinary people gather to do their best work. If you’re"
    " excited by the idea of making a real impact, a career with Apple might be your dream job… Just be prepared"
    " to dream big! An expert in advanced analytics, you are passionate about turning data into impactful insights,"
    " and driving creative data science solutions. You are skilled at creating analytical models and interactive"
    " visualizations. You are a motivated self-starter, comfortable navigating through ambiguity to evaluate complex"
    " data, analyze data from multiple angles, build analytical workflows, to deliver findings that directly impact"
    " the business. If this describes you, then you should consider joining us."
  )

  assert extract_summary(test_html) == assertion_string

def test_extract_description():
  with open(f'{ROOT_DIR}/site_data/test_pages/test_job_description_1.html') as file:
    test_html = BeautifulSoup(file, 'html.parser')

  assertion_string = (
    "- You have outstanding communication skills, proven data science and advanced analytics capabilities, strong business acumen, and an innate drive to deliver results\n"
    "- You are a self-starter, comfortable with ambiguity, and enjoy working in a fast-paced dynamic environment - Innovative and strategic approach to reporting and business analytics\n "
    "- Develop custom models, algorithms, and interactive visualizations to deliver Supply Chain insights - Wrangle and analyze data to identify patterns, trends, and feature engineering\n"
    "- Evaluate business needs through in-depth conversations with business users to understand the domain and apply data science for insights\n"
    "- Present key findings to leadership to evaluate business impact, in non-technical terms"
  )

  assert extract_description(test_html) == assertion_string

@pytest.mark.parametrize("html_file, expected_result",[
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_1.html', None),
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_2.html', [
    'BS+3 years of relevant proven experience',
    ("(BS in Computer Science, Electrical Engineering or"
     " related. MS in Computer Science, Electrical Engineering"
     " or related preferred)"
    )
  ])
])
def test_extract_min_quals(html_file, expected_result):
  with open(html_file) as file:
    test_html = BeautifulSoup(file, 'html.parser')

  if expected_result is None:
    assert extract_min_quals(test_html) is None
  else:
    assert extract_min_quals(test_html) == expected_result

@pytest.mark.parametrize("html_file, expected_result",[
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_1.html', None),
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_2.html', [
    "Proficiency with large datasets' processing, extraction, analysis and reporting",
    "Deep knowledge & hands-on experience with Oracle and Cassandra database design & architecture",
    "Strong proficiency with Python programming language",
    "Strong proficiency with query plans and crafting curated datasets",
    "Strong skills with Linux operating systems running in production.",
    "Knowledge of the semiconductor process is helpful",
    "Experience with STDF parsing code development is helpful",
    "Experience in Machine Learning is helpful",
    "Experience in building data API is helpful",
    "Proven record of taking ownership and optimally delivering results.",
    "Ability to learn new technologies"
  ])
])
def test_extract_pref_quals(html_file, expected_result):
  with open(html_file) as file:
    test_html = BeautifulSoup(file, 'html.parser')

  if expected_result is None:
    assert extract_pref_quals(test_html) is None
  else:
    assert extract_pref_quals(test_html) == expected_result

@pytest.mark.parametrize("html_file, expected_result",[
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_1.html', 'Demonstrated collaboration as well as leadership and influencing skills'),
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_2.html', None)
])
def test_extract_key_quals(html_file, expected_result):
  with open(html_file) as file:
    test_html = BeautifulSoup(file, 'html.parser')

  if expected_result is None:
    assert extract_key_quals(test_html) is None
  else:
    assert extract_key_quals(test_html)[-1] == expected_result

@pytest.mark.parametrize("html_file, expected_result",[
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_1.html', "Bachelor’s degree required in Data Science, Machine Learning, Computer Science, Mathematics or Statistics. MSc in Data Science or Operations Research"),
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_2.html', None)
])
def test_extract_education_experience(html_file, expected_result):
  with open(html_file) as file:
    test_html = BeautifulSoup(file, 'html.parser')

  if expected_result is None:
    assert extract_education_experience(test_html) is None
  else:
    assert extract_education_experience(test_html) == expected_result

@pytest.mark.parametrize("html_file, expected_result",[
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_1.html', None),
  (f'{ROOT_DIR}/site_data/test_pages/test_job_description_2.html', ['$13,600', '$248,700'])
])
def test_extract_pay_range(html_file, expected_result):
  with open(html_file) as file:
    test_html = BeautifulSoup(file, 'html.parser')

  if expected_result is None:
    assert extract_pay_range(test_html) is None
  else:
    assert extract_pay_range(test_html) == expected_result
