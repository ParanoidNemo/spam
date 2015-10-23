#!/usr/bin/env python

#   Copyright (C) 2015 by Andrea Calzavacca <paranoid.nemo@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import os, re

def insert_data(string, rep_dict):

    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)

    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

def create_dict(rep_dict, rep_list):

    for index, item in rep_list:
        i = "{" + str(index) + "}"
        rep_dict[i] = item

    return(rep_dict)
