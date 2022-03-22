#!/bin/bash

source /home/jayas/Documents/Projects/netmeds_scraping/venv/bin/activate  #path to your venv
export PYTHONPATH='/home/jayas/Documents/Projects/netmeds_scraping/'
scrapy crawl netmeds -o data.json
