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

"""This module define a set of functions to check and control the status of
beshell and it's abs path. In order to work it depends to 2 (two) extra modules
gitpython and check (the first one you could install using pip, the second one
it's only avaible on the same github repo that you have used to download this
module.)

Global functins defined:
- beshell.up: check if there are any update avaiable and install it
- beshell.install: download, compile and install BE::Shell on your system

Classes releated functions:

Class beshell.Configuration:
define a set of function to check the abs path of your actual configuration file
and directory
    - Configuration.config_dir: return the configuration dir abs path
    - Configuration.main_file: return the be.shell main file abs path
    - Configuration.main_dir: return the directory you are using to store
    installed themes, scripts and other usefull stuff

Class beshell.Theme:
define two function that return the theme name you are using and the abs path
to that theme
    - Theme.name: return the theme name
    - Theme.path: return the abs path of the theme in use
    - Theme.l_list: return a list of installed beshell themes
    - Theme.d_list: return a list of downloaded themes

For more in depth usage and example check the docstring contained in the functions"""

#import std module(s)
import os, sys
import subprocess

#import downloaded module(s)
import git

global project_dir
global beshell_dir

project_dir = os.path.expanduser('~/project')
beshell_dir = os.path.join(project_dir, 'be-shell')
g = git.cmd.Git(beshell_dir)
g2 = git.cmd.Git(project_dir)

if os.path.isdir(os.path.expanduser('~/.kde4')):
    default = os.path.expanduser('~/.kde4')
else:
    default = os.path.expanduser('~/.kde')

def up():

    """This function check the status of the installation of BE::Shell on your
    system, compare it with the actual status on the github repo and if there
    are some changes download and install the new version"""

    if os.path.isdir(beshell_dir):
        ctrl_seq = 'Already up-to-date.'
        git_out = g.pull()

        if git_out != ctrl_seq:
            os.chdir(os.path.join(beshell_dir, 'build'))
            print('Running make, please wait..')
            make_out = subprocess.check_call('make')
            print('Make process end correctly.\nStart installation..')
            install_out = subprocess.check_call(['sudo', 'make', 'install'])
            print('Everything done, BE::Shell is now up to date.')
        else:
            print(git_out)

def install():
    remote = 'git://git.code.sf.net/p/be-shell/code'
    while not os.path.isdir(project_dir):
        os.makedirs(project_dir)
    else:
        os.chdir(project_dir)
        print('Cloning package(s) from remote repo..')
        clone_out = g2.clone(remote, 'be-shell')
        os.chdir(project_dir)
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
        cfg_file = os.path.join(Configuration.config_dir(), 'be.shell')
        return(cfg_file)

    def main_dir():
        main_dir = os.path.join(default, 'share/apps/be.shell')
        return(main_dir)

class Theme:

    def name():

        """(str) Return the name of the theme actually used.

        e.g.
        >>> beshell.Theme.name()
        'Hydrogen'"""

        cfg = open(Configuration.main_file())
        cfg.seek(0, 0)
        for line in cfg:
            if line.startswith('Theme'):
                outstring = line[6:-1]
        return(outstring)

    def path():

        """(str) Return the absolut path of the theme in use.

        e.g.
        >>> beshell.Theme.path()
        '/home/nemo/.kde4/share/apps/be.shell/Themes/Hydrogen'"""

        cfg = open(Configuration.main_file())
        cfg.seek(0, 0)
        for line in cfg:
            if line.startswith('Theme'):
                outstring = os.path.join(Configuration.main_dir(), 'Themes', line[6:-1])
        return(outstring)

    def l_list():

        """(lst) Return a list of locally installed themes"""

        theme_dir = os.path.join(Configuration.main_dir(), 'Themes')
        for line in os.listdir(theme_dir):
            t = line
            if not t.startswith('.'):
                print(t)

    def d_list():

        """(lst) Return a list of locally downloaded themes"""

        try:
            theme_dir = os.path.join(project_dir, 'Bedevil', 'be.shell', 'Themes')
            for line in os.listdir(theme_dir):
                t = line
                if not t.startswith('.'):
                    print(t)
        except FileNotFoundError as ex:
            print(ex)
