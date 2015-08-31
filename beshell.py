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

"""Check if your locale installation of BE::Shell is updated.
To do so use the default project directory define above as
beshell_dir. If there are some updates it sync the git repo
and start the compilation process. After that start the installation
process (it obviusly require root access so you need sudo to
complete that)

e.g.
>>> beshell.up()
Running make, please wait..
...
Everything done, BE::Shell is now up to date."""

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

"""Same as up() above. Before start the make process clone the repo and
run configure to check the dependencies. Right now doesn't resolve it,
just print error if someone missing.

e.g.
>>> beshell.install()"""
class Configuration:

    def __init__(self):
        self.default = os.path.expanduser('~/.kde4')

    def default_path():
        if os.path.isdir(os.path.expanduser('~/.kde4')):
            default = os.path.expanduser('~/.kde4')
        else:
            default = os.path.expanduser('~/.kde')
        return(default)

    def config_dir():
        cfg_dir = '/home/nemo/.kde4/share/config'
        #main_dir = os.path.join(self.default, 'share/apps/be.shell')
        #cfg_file = os.path.join(cfg_dir, 'be.shell')
        return(cfg_dir)

    def main_file():
        cfg_file = os.path.join(cfg_dir, 'be.shell')
        return(cfg_file)

    def main_dir():
        main_dir = os.path.join(default, 'share/apps/be.shell')
        return(main_dir)

"""Check the system to find where be.shell theme and configs are located,
following the default path (~/.kde or ~/.kde4).

Return a dict that contain three keys (config, theme, file) associated
with the abs path for the choosen keys file (configuration dir, theme dir,
be.shell main config file)

e.g
>>> beshell.config_dir()
{'config': '/home/nemo/.kde4/share/config', 'theme': '/home/nemo/.kde4/share/apps/be.shell/', 'file': '/home/nemo/.kde4/share/config/be.shell'}"""

class Theme:

    config_dir = Configuration.config_dir()
    def name():
        cfg = open(os.path.join(config_dir, 'be.shell'))
        for line in cfg:
            l = cfg.readline()
            if l.startswith('Theme'):
                outstring = l[6:-1]
        return(outstring)

    def path():
        cfg = open(os.path.join(config_dir, 'be.shell'))
        for line in cfg:
            l = cfg.readline()
            if l.startswith('Theme'):
                outstring = os.path.join(config_dir, 'Themes', l[6:-1])
        return(outstring)

"""Check the actual theme and theme directory applied to BE::Shell.

Return a dict that contain two keys (dir, name) associated
with the abs path for the choosen keys file (theme dir, theme name)

e.g
>>> beshell.config_dir()
{'dir': '/home/nemo/.kde4/share/apps/be.shell/Themes/Hydrogen', 'name': 'Hydrogen'}"""
