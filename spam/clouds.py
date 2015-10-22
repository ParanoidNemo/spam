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

import os, sys, re
import subprocess


class Dropbox():

    def space_info(remote):

        cloud_storage = remote + ':'

        size = subprocess.run(['rclone', 'size', cloud_storage], stdout=subprocess.PIPE, universal_newlines=True)
        size = size.stdout

        for line in size.split(sep='\n'):
            if line.startswith('Total size'):
                tot = line

        tot = re.sub(r'\s', '\n', tot)

        l = []
        for item in tot.split(sep='\n'):
            l.append(item)

        used_space = l[2][:-1]
        total_space = float(20)
        free_space = total_space - float(used_space)

        out = [str(total_space), str(free_space), used_space]

        return(out)

    def compare(remote, local):

        cloud_storage = remote + ':'
        _local = os.path.expanduser(local)

        check = subprocess.run(['rclone', 'check', '-q', cloud_storage, _local])

        return(str(check.returncode))

class Mega():

    def space_info(size):

        out = []
        _size = '--' + size

        s = subprocess.run(['megadf', _size], stdout=subprocess.PIPE, universal_newlines=True)

        for line in s.stdout.split(sep='\n'):
            line = re.sub(r'\s', '\n', line)
            for line in line.split(sep='\n'):
                if line.isdigit():
                    out.append(line)

        return(out)
