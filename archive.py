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

#import custom module(s)
import check
import beshell

def compress(_path, location, name='new_archive', extension='tar'):
    check.dir(_path)
    check.dir(location)
    c_name = name + '.' + extension
    if os.path.exists(os.path.join(os.path.expanduser(location), c_name)):
        print(c_name + ' already exists in ' + os.path.expanduser(location))
    else:
        os.chdir(os.path.expanduser(location))
        shutil.make_archive(name, extension, base_dir=os.path.expanduser(_path))

if __name__ == '__main__':
    compress('~/.kde4/share/apps/be.shell/Themes/Hydrogen/', '~/.local/share/be.shell/backup/')
