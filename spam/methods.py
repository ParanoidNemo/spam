#!/usr/bin/env python

import os, re

def insert_data(string, rep_dict):

    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)

    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

def create_dict(rep_list):

    rep_dict = {}

    for index, item in enumerate(rep_list):
        i = "{" + str(index) + "}"
        rep_dict[i] = item

    return(rep_dict)
