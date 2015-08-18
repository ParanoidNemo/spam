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
import os.path
import subprocess
import getpass

#import downloaded module(s)
import git

#import custom module(s)
import check

project_dir = os.path.expanduser('~/project/')
beshell_dir = os.path.expanduser(project_dir + 'be-shell/')
g = git.cmd.Git(beshell_dir)

def up():
    if check.dir(beshell_dir):
        ctrl_seq = 'Already up-to-date.'
        git_out = g.pull()

        if git_out != ctrl_seq:
            os.chdir(beshell_dir + 'build')
            print('Running make, please wait..')
            make_out = subprocess.check_call('make')
            print('Make process end correctly.\nStart installation..')
            install_out = subprocess.check_call(['sudo', 'make', 'install'])
            print('Everything done, BE::Shell is now up to date.')
        else:
            print(git_out)  #check if needed when I've connection

def install():
    if check.dir(project_dir):
        os.chdir(project_dir)
        print('Cloning package(s) from remote repo..')
        clone_out = g.clone(indirizzo, 'be-shell')       #search how to clone a remote repo
        print('Configuring the system..')
        configure_out = subprocess.check_call('./configure')
        os.chdir('build')
        print('Running make, please wait..')
        make_out = subprocess.check_call('make')
        print('Make process end correctly.\nStart installation..')
        install_out = subprocess.check_call(['sudo', 'make', 'install'])
        print('Everything done, BE::Shell is now installed.\nIf you want to start it run "kquitapp plasmashell; sleep 2; be.shell"')

def config_dir():
    if os.path.isdir(os.path.expanduser('~/.kde4')):
        cfg_dir = os.path.expanduser('~/.kde4/share/config/')
        be_dir = os.path.expanduser('~/.kde4/share/apps/be.shell/')
    else:
        cfg_dir = os.path.expanduser('~/.kde/share/config/')
        be_dir = os.path.expanduser('~/.kde/share/apps/be.shell/')
    return({'config': cfg_dir, 'theme': be_dir})

def theme():
    cfg = open(config_dir()['config'] + 'be.shell')
    for line in cfg:
        l = cfg.readline()
        if l.startswith('Theme'):
            theme_name = l[6:-1]
            theme_dir = config_dir()['theme'] + 'Themes/' + l[6:-1]
    return({'dir': theme_dir, 'name': theme_name})
