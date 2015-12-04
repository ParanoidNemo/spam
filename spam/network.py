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

from spam import methods

def wifi_info(interface):
    command_line = "iwconfig %s" %interface

    info = methods.call_command(command_line)

    info_ = [info.split()[0]]

    for item in info.split():
        if item.startswith("ESSID"):
            item = item.split(':')
            info_.append(item[1].strip('"'))
        elif item.startswith('Quality'):
            item = item.split('=')
            item = item[1].split('/')
            q = item[0]
            p = int(q) * 100 // 70
            info_.append(str(p))
        else:
            pass    

    return(info_)
