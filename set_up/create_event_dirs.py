#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:35:59 2022

@author: emmadevin
"""

import pandas as pd
import os
import os.path as path


work_dir = '/Users/emmadevin/Work/USGS_2021/Data_56/'
out_dir = '/Users/emmadevin/Work/USGS_2021/Data_56/gmprocess/event_downloads/data'

l = pd.read_csv(work_dir + 'select56cat.txt', sep = ' ',skiprows=24)

events = l['Event_ID']


for event in events:
    if not path.exists(out_dir + '/ci' + str(event)):
        os.makedirs(out_dir + '/ci' + str(event))