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
import subprocess

#import downloaded module(s)
import git

#import custom module(s)
import check

project_dir = os.path.expanduser('~/project/')
beshell_dir = os.path.expanduser(project_dir + 'be-shell/')
g = git.cmd.Git(beshell_dir)

if os.path.isdir(os.path.expanduser('~/.kde4')):
    default = os.path.expanduser('~/.kde4')
else:
    default = os.path.expanduser('~/.kde')

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

class Configuration:

    def config_dir():
        cfg_dir = os.path.join(default, 'share/config')
        return(cfg_dir)

    def main_file():
        cfg_file = os.path.join(cfg_dir, 'be.shell')
        return(cfg_file)

    def main_dir():
        main_dir = os.path.join(default, 'share/apps/be.shell')
        return(main_dir)

class Theme():

    def name():
        cfg = open(os.path.join(Configuration.config_dir(), 'be.shell'))
        for line in cfg:
            l = cfg.readline()
            if l.startswith('Theme'):
                outstring = l[6:-1]
        return(outstring)

    def path():
        cfg = open(os.path.join(Configuration.config_dir(), 'be.shell'))
        for line in cfg:
            l = cfg.readline()
            if l.startswith('Theme'):
                outstring = os.path.join(Configuration.config_dir(), 'Themes', l[6:-1])
        return(outstring)
