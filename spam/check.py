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

"""This module define a set of functions to check variuos aspects of the system.

Global functions defined:
    - check.prg: check if a program is installed and if is executable is locate in /usr/bin
    - check.date: verify how much time is passed from a date saved into a timestamp file
    - check.distro: check the distro you are on"""

import os, sys
import datetime

#start def the function(s)
def prg(self):

    """(bool) This function check if an executable exists in /usr/bin"""

    if os.path.exists('/usr/bin/' + self):
        return True
    else:
        return False


def date(timestamp):

    """This function check how much time as passed (default value = days) between a give date and today"""

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

def distro():           #check the current distro installed on the system

    """This function check what is the distro you are on"""

    if prg('aptitude'):
        distro = 'debian'
    elif prg('dnf'):
        distro = 'fedora'
    elif prg('pacman'):
        distro = 'archlinux'
    else:
        distro = ''

    return(distro)
