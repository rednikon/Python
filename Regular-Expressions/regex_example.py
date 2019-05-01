#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:51:00 2019

@author: veemac
"""

import re

phone = '415 239-3000'

#show the pattern that matches the phone number
pat = "\d{3} \d{3}-\d{4}"
pat = re.compile(pat)
m = re.match(pat, phone)
'matched' if m else 'no match'

m.groupdict()
{'area': '415', 'number': '239-3000',}

d = m.groupdict()

s = "That number has area code {area}"

#Use the dict d to fill in the values in s above. **d unpacks a dictionary
s.format(**d)