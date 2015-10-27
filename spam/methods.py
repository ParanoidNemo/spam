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

def format(format_file):

    format_string = ''

    with open(os.path.expanduser(format_file)) as f:
        for line in f:
            if line.startswith('#'):
                continue
            format_string += line

    format_string = re.sub(r'>\s<', '><', format_string)
    format_string = re.sub(r'\n', '', format_string)

    return(format_string)
