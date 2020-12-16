#!/bin/env python3
import os
import re
import feedparser
import urllib
from bs4 import BeautifulSoup


def extract_image_urls(string):
    soup = BeautifulSoup(string, 'html.parser')
    tags = soup.find_all('img')
    urls = [img['src'] for img in tags]
    return urls

def retrieve_images(from_urls, to_dir):
    for url in from_urls:
       retrieve_image(url, to_dir)

def retrieve_image(from_url, to_dir):
    target_path, changes = re.compile('^https?://').subn(to_dir, from_url)
    print(from_url+' => '+target_path)
    if not os.path.exists(os.path.dirname(target_path)):
        os.makedirs(os.path.dirname(target_path),0o775)
    if not os.path.exists(target_path):
        urllib.request.urlretrieve(from_url, target_path)

feed = feedparser.parse('https://www.fraser-moore.com/diary/rss?l=500')
for entry in feed.entries:
    urls = extract_image_urls(entry.description)
    retrieve_images(urls, os.path.dirname(os.path.realpath(__file__))+'/source_images/')

