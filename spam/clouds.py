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

"""This module define a set of classes to interact with most of the common cloud
service.

Classes releated functions:

Class clouds.Rclone:
define one function that return informations regardings the cloud service choose;
it depends by rclone.
    - Rclone.space_info: return a list containing space informations

Class clouds.Mega:
define one function that interface with the mega cloud service; it depends by megatools
    -Mega.space_info: return a list containing space informations

For more in depth usage and example check the docstring contained in the functions"""

import os, sys, re
import subprocess

from spam import methods

class Rclone():

    def space_info(remote, service):

        """(list) return a list containing total space, free space, used space
        and service name (e.g. dropbox, drive etc). Require two arguments: the name of
        the remote set with rclone and the name of the cloud service"""

        cloud_storage = remote + ":"

        size = methods.call_command("rclone size " + cloud_storage)

        for line in size.split(sep='\n'):
            if line.startswith("Total size"):
                tot = line

        tot = re.sub(r'\s', '\n', tot)

        l = []
        for item in tot.split(sep='\n'):
            l.append(item)

        used_space = l[2][:-1]

        if service == "dropbox":
            total_space = float(20)
        elif service == "drive":
            total_space = float(15)
        else:
            print("Service not found")
            sys.exit(1)

        free_space = total_space - float(used_space)

        used_space = "{0:.1f}".format(float(used_space))
        free_space = "{0:.1f}".format(free_space)

        pfree = 100 * float(free_space) // int(total_space)
        pused = 100 * float(used_space) // int(total_space)

        out = [str(total_space), str(free_space), used_space, service, str(pfree), str(pused)]

        return(out)

    def compare(remote, local):

        cloud_storage = remote + ":"
        _local = os.path.expanduser(local)

        check = subprocess.run(["rclone", "check", "-q", cloud_storage, _local])

        return(str(check.returncode))

class Mega():

    def space_info(size="gb"):

        """(list) return a list containing total space, free space, used space and
        service name. Have one optional arguments: the measure unit you want to use to
        the output data (default = Gb)"""

        out = []
        _size = "--" + size

        s = methods.call_command("megadf " + _size)

        for line in s.split(sep='\n'):
            line = re.sub(r'\s', '\n', line)
            for line in line.split(sep='\n'):
                if line.isdigit():
                    line = line + '.0'
                    out.append(line)

        out.append("mega")

        pfree = 100 * float(out[2]) // float(out[0])
        pused = 100 * float(out[1]) // float(out[0])

        out.append(str(pfree))
        out.append(str(pused))

        return(out)
