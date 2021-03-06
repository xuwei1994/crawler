#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from MultipleProcesses import process_crawler
from MongoCache import MongoCache
import re


down_num = 1
def main(url, max_threads):

    cache = MongoCache(db_name="thread")
    process_crawler(args=url, cache=cache, max_threads=max_threads, timeout=10)


if __name__ == '__main__':
    max_threads = int(sys.argv[1])
    url = 'https://bbs.hupu.com/lol'
    main(url, max_threads)
    #https://bbs.hupu.com/20578540.html