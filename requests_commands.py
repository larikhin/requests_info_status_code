import requests
from bs4 import BeautifulSoup
import csv


url ='https://d3.ru/'

def pr(data):
    print('     ')
    print(data)
    print('     ')
    print(dir(data))

def requests_dir(url):
    pr(requests.api)
    pr(requests.auth)
    pr(requests.certs)
    pr(requests.chardet)
    pr(requests.check_compatibility)
    pr(requests.status_codes)
    pr(requests.codes)
    pr(requests.compat)
    pr(requests.cookies)
    pr(requests.delete)
    pr(requests.exceptions)
    pr(requests.get)
    pr(requests.head)
    pr(requests.hooks)
    pr(requests.logging)
    pr(requests.models)
    pr(requests.options)
    pr(requests.packages)
    pr(requests.patch)
    pr(requests.post)
    pr(requests.put)
    pr(requests.request)
    pr(requests.session)
    pr(requests.sessions)
    pr(requests.structures)
    pr(requests.urllib3)
    pr(requests.utils)
    pr(requests.warnings)
    pr(requests.adapters)
    pr(requests.get(url))

# def get_html(url):
#     r= requests.get(url)
#     pr(r.url)
#     pr(r.apparent_encoding)
#     pr(r.close)
#     pr(r.connection)
#     pr(len(r.content))
#     pr(r.cookies)
#     pr(r.elapsed)
#     pr(r.encoding)
#     pr(r.headers)
#     pr(r.history)
#     pr(r.is_permanent_redirect)
#     pr(r.is_redirect)
#     pr(r.iter_content)
#     pr(r.iter_lines)
#     pr(r.json)
#     pr(r.links)
#     pr(r.next)
#     pr(r.ok)
#     pr(r.raise_for_status)
#     pr(r.raw)
#     pr(r.reason)
#     pr(r.request)
#     pr(r.status_code)
#     pr(len(r.text))


def main():
    # get_html(url)
    requests_dir(url)


if __name__ == '__main__':
    main()
