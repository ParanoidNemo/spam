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

import os.path
import os
import sys
import datetime

#start def the function(s)
def prg(self):      #check if an executable exists in /usr/bin/
    if os.path.exists('/usr/bin/' + self):
        return True
    else:
        return False

def dir(self):      #check if a dir exists into the given path
    if os.path.isdir(os.path.expanduser(self)):
        return True
    else:
        print('Directory not found, do you want to create one into the default location (~/project/)? [yes/no]')
        anw = input()
        if anw == 'yes':
            os.makedirs(self)
            print('Created directory ' + self)
            return True
        else:
            raise KeyboardInterrupt('Nothing to do')
            sys.exit(1)

#def date(self, mesure=days):     #check how much time as passed (default=days) between to given dates
#    today = datetime.datetime.date(now)
