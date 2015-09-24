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

#import std module(s)
import os, sys
import shutil

def compress(_path, location, name='new_archive', extension='tar'):
    while not os.path.isdir(os.path.expanduser(location)):
        os.makedirs(os.path.expanduser(location))
    else:
        c_name = name + '.' + extension
        if os.path.exists(os.path.join(os.path.expanduser(location), c_name)):
            print(c_name + ' already exists in ' + os.path.expanduser(location))
        else:
            os.chdir(os.path.expanduser(location))
            shutil.make_archive(name, extension, base_dir=os.path.expanduser(_path))

def extract(dst, location, name, extension='tar'):

    try:
        archive_name = os.path.join(os.path.expanduser(location), name + '.' + extension)
        if os.path.isfile(archive_name):
            os.chdir(os.path.expanduser(location))
            shutil.unpack_archive(archive_name, os.path.expanduser(dst), extension)
    except FileNotFoundError:
        print("File doesn't exists or is a dir")
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    compress()
