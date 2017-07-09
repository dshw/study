# -*- coding:utf-8 -*-
# !/usr/bin/env python
import sys, os
from tcsoa import log, driver

log = log.getLogger(fileloglevel='DEBUG')

if __name__ == '__main__':
    driver.add_path(['cases', 'data', 'util'])

    case_dir = '/cases/'

    driver.run(relative_case_dir=case_dir)
