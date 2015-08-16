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

#!/usr/bin/env python

#import std module(s)
import os, sys
import os.path
import subprocess

#import downloaded module(s)
import git

#import custom module(s)
import check

project_dir = os.path.expanduser('~/project/be-shell')
g = git.cmd.Git(project_dir)

def up(): #DA FINIRE
    if check.dir(project_dir):
        ctrl_seq = 'Already up-to-date.'
        git_out = g.pull()
#-------------------------------------------------------------------------------
#----------------DA QUI DA RICONTROLLARE A MENTE FRESCA-------------------------
#-------------------------------------------------------------------------------
        if git_out != ctrl_seq:
            os.chdir('build')
            #Prova 1 -- PROBLEMA, NON PRINTA IN TEMPO REALE
            make_out = str(subprocess.check_output('make', shell=True), 'utf-8')
            print(make_out, end='[')
            #Prova 2 -- PROBLEMA, NON ESCE ALLA FINE DELL'OPERAZIONE
            subprocess.Popen('make')
#-------------------------------------------------------------------------------
#---------------Da qui inizio istruzioni di installazione post make-------------
#-------------------------------------------------------------------------------
            install_out = str(subprocess.check_output('sudo make install', shell=True), 'utf-8') #verificare se chiama sudo o se bisogna usare un metodo particolare
            print(install_out)
            print('Everything done, BE::Shell is now up to date')
    else:
        print('Project directory not found')

def install(): #DA CREARE

def theme():
    if os.path.isdir(os.path.expanduser('~/.kde4')):
        cfg_dir = os.path.expanduser('~/.kde4/share/config/')
        be_dir = os.path.expanduser('~.kde4/share/apps/be.shell/')
    else:
        cfg_dir = os.path.expanduser('~.kde/share/config/')
        be_dir = os.path.expanduser('~.kde/share/apps/be.shell/')
    cfg = open(cfg_dir + 'be.shell')
    for line in cfg:
        l = cfg.readline()
        if l.startswith('Theme'):
            theme = l[6:-1]
            theme_dir = be_dir + 'Themes/' + l[6:-1]
