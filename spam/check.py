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

import os, sys
import datetime

#start def the function(s)
def prg(self):      #check if an executable exists in /usr/bin/

    if os.path.exists('/usr/bin/' + self):
        return True
    else:
        return False


def date(timestamp):     #check how much time as passed (default=days) between to given dates

    t = datetime.date.today()
    date_code = t.toordinal()

    with open(timestamp, 'r') as ts:
        for line in ts:
            if line.startswith('#'):
                continue
            elif line.startswith('last'):
                odc = line[5:-2]
                old_date_code = int(odc)

    if date_code > old_date_code:
        print(date_code - old_date_code)
