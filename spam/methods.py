#!/usr/bin/env python

"""This module define a set of functions to avoid repetitive operations.

Global functions defined:
    - insert_data: generate a string from a format string an a dict
    - create_dict: generate a dictionary from a list
    - format_string: generate a format string from an external file"""

import os, re
import subprocess

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

def time_convertion(seconds):

    """(tuple) convert seconds into minutes/hours, return a tuple (hours, minutes, seconds)"""

    minutes = 0
    hours = 0
    days = 0

    while seconds >= 60:
        minutes += 1
        seconds -= 60

    while minutes >= 60:
        hours += 1
        minutes -= 60

    while hours >= 24:
        days += 1
        hours -= 24

    return(days, hours, minutes, seconds)

def call_command(command):
    proc = subprocess.run(command.split(), stdout=subprocess.PIPE, universal_newlines=True)
    return(proc.stdout)
