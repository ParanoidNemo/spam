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

def fs_info(mountpoint):

    stat = os.statvfs(os.path.expanduser(mountpoint))
    free = "{0:.2f}".format(stat.f_bavail * stat.f_frsize / 1000000000)    # results in Gb (free space)
    tot = "{0:.2f}".format(stat.f_frsize * stat.f_blocks / 1000000000)       # results in Gb (total space)
    used = "{0:.2f}".format(float(tot) - float(free))

    pfree = 100 * float(free) // float(tot)
    _pfree = str(pfree)
    pused = 100 * float(used) // float(tot)
    _pused = str(pused)

    return{'mount': mountpoint, 'free': free, 'tot': tot, 'used': used, 'pfree': _pfree, 'pused': _pused}