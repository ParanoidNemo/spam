#!/usr/bin/env python

"""This module define a set of functions to avoid repetitive operations.

Global functions defined:
    - insert_data: generate a string from a format string an a dict
    - create_dict: generate a dictionary from a list
    - format_string: generate a format string from an external file"""

import os, re

def insert_data(string, rep_dict):

    """(string) return the string resulting by add the values contained in rep_dict
    into another string that contains the dict keys"""

    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)

    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

def create_dict(rep_list):

    """(dict) return a dict from a given list. The dict keys are progressive int
    envelop by curled brachets"""

    rep_dict = {}

    for index, item in enumerate(rep_list):
        i = "{" + str(index) + "}"
        rep_dict[i] = item

    return(rep_dict)

def format_string(format_file):

    """(string) return a html format string from a given file"""

    format_string = ''

    with open(os.path.expanduser(format_file)) as f:
        for line in f:
            if line.startswith('#'):
                continue
            format_string += line

    format_string = re.sub(r'>\s<', '><', format_string)
    format_string = re.sub(r'\n', '', format_string)

    return(format_string)
