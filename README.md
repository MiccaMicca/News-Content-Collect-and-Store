# News-Content-Collect-and-Store

## Overview

The project demonstrates how to use Scrapy, a web crawling framework, to crawl a news website, store the data into Mongodb and retrieve data through API.
This project is done inspiring by a coding challenge of Insentia called [Data Engineer Coding Challenge](https://github.com/Isentia/Coding-Challenge/blob/master/Data-Engineer-Coding-Challenge.md).

## Environment

* Python 3.7.4
* macOS

## Install

1. The project uses Scrapy, PyMongo

```
pip install scrapy
pip install pymongo
```

See the install section in the documentation at https://docs.scrapy.org/en/latest/intro/install.html and

https://pymongo.readthedocs.io/en/stable/ for more details

2. Set up cloud MongoDB service. Here, MongoDB Atlas is used instead of Compose.io because the latter no longer support a free MongoDB.

   https://www.mongodb.com/cloud/atlas

## Build

1. Start a new project

`scrapy startproject NewsCollector`

2. Create a spider under NewsCollector/spiders

`scrapy genspider -t basic nyt_spider` 

3. Modify items.py, pipelines.py, settings.py as files in the repo.
4. Run spider by spider name

`scrapy crawl nyt_spider`

5. After storing all data in MongoDB, search query by running extract.py and enter query in command line

`python3 extract.py`
