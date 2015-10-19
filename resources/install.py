#! /usr/bin/env python

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

import os, sys, shutil, subprocess

#check python version
v = 'python' + sys.version[:3]
_v = float(sys.version[:3])
if _v < 3.4:
    print('Spam need python 3.4 or higher')

#check if spam exists in your config_dir
f = os.path.join('/usr/lib', v, 'site-packages', 'spam.pth')

try:
    if os.path.isfile(f):
        print("Spam path's already registered into python sys.path")
    else:
        with open('spam.pth', 'w') as _f:
            _f.write(os.environ['HOME'] + '.local/share/')
        print('Registering pam into sys.path')
        subprocess.call(['sudo', 'cp', 'spam.pth', f])
except Exception as ex:
    print(ex)
    sys.exit(1)

os.chdir('../')

if os.path.isdir(os.path.expanduser('~/.local/share/spam')):
    print('Spam dir already exists.')
else:
    shutil.copytree('spam', os.path.expanduser('~/.local/share/'))
    print('Spam module correctly installed')
