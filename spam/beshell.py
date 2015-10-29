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
module).

Global functions defined:
    - beshell.clone: download the source code into default project dir
    - beshell.up: check if there are any update avaiable and install it
    - beshell.install: compile and install BE::Shell on your system

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

global home, remote
global project_dir
global beshell_dir

home = os.path.expanduser('~')
remote = 'git://git.code.sf.net/p/be-shell/code'
project_dir = os.path.join(home, 'project')
beshell_dir = os.path.join(project_dir, 'be-shell-code')
g = git.cmd.Git(beshell_dir)
g2 = git.cmd.Git(project_dir)

if os.path.isdir(os.path.expanduser('~/.kde4')):
    default = os.path.expanduser('~/.kde4')
else:
    default = os.path.expanduser('~/.kde')

class Configuration:

    def config_dir():

        """(str) Return the absolut path of the configuration directory"""

        cfg_dir = os.path.join(default, 'share', 'config')
        return(cfg_dir)

    def main_file():

        """(str) Return the absolut path of the main configuration file"""

        cfg_file = os.path.join(Configuration.config_dir(), 'be.shell')
        return(cfg_file)

    def main_dir():

        """(str) Return the absolut path of the main configuration directory"""

        main_dir = os.path.join(default, 'share', 'apps', 'be.shell')
        return(main_dir)

class Theme:

    def name():

        """(str) Return the name of the theme actually used."""

        cfg = open(Configuration.main_file())
        cfg.seek(0, 0)  #to be sure, set the offset to the start of the file explicity
        for line in cfg:
            if line.startswith('Theme'):
                outstring = line[6:-1]
        return(outstring)

    def path():

        """(str) Return the absolut path of the directory of the theme in use."""

        outstring = os.path.join(Configuration.main_dir(), 'Themes', Theme.name())
        return(outstring)

    def l_list():

        """(lst) Return a list of locally installed themes"""

        theme_dir = os.path.join(Configuration.main_dir(), 'Themes')
        i = 0
        d = {}
        for line in os.listdir(theme_dir):
            t = line
            if not t.startswith('.'):
                d[i] = t
                i += 1
        return(d)

    def d_list():

        """(lst) Return a list of locally downloaded themes"""

        try:
            theme_dir = os.path.join(project_dir, 'Bedevil', 'be.shell', 'Themes')
        except FileNotFoundError as ex:
            print(ex)

        i = 0
        d = {}
        for line in os.listdir(theme_dir):
            t = line
            if not t.startswith('.'):
                d[i] = t
                i += 1
        return(d)

class Cmd:

    def install_theme(cfg_file, theme_dir):

        """(void) install choosen configuration file and theme"""

        shutil.copy2(cfg_file, Configuration.config_dir())
        os.rename(cfg_file, 'be.shell')
        print("Configuration file copied..\n")
        shutil.copytree(theme_dir, os.path.join(beshell.Configuration.main_dir, 'Themes'))
        print("Theme directory copied..\nPlease reload the shell to see the applied theme")

    def clone():

        """This function clone the source code of BE::Shell into the default project
        directory (~/project/be-shell-code), creating it if doesn't exists"""

        while not os.path.isdir(project_dir):
            os.makedirs(project_dir)
        else:
            print('Cloning package(s) from remote repo..')
            g2.clone(remote, 'be-shell-code')

    def up():

        """(void) check the status of the installation of BE::Shell on your
        system, compare it with the actual status on the github repo and if there
        are some changes download and install the new version"""

        if os.path.isdir(beshell_dir):

            ctrl_seq = 'Already up-to-date.'
            git_out = g.pull()

            if git_out != ctrl_seq:

                os.chdir(beshell_dir)

                if os.path.isdir('build'):
                    shutil.rmtree('build')
                    install()
                else:
                    install()

            else:
                print(git_out)

        else:
            print("BE::Shell source code not found into the default directory (~/project/be-shell-code); in order to use this features you need to clone the repo into that path.\nYou could use the clone function to do so")

    def install():

            os.chdir(beshell_dir)

            print("Running configure")
            subprocess.run(['./configure'], stdout=subprocess.PIPE, universal_newlines=True)

            os.chdir('build')

            print('Running make, please wait..')
            make_out = subprocess.run(['make'], stdout=subprocess.PIPE, universal_newlines=True)

            print('Make process end correctly.\nStart installation..')
            install_out = subprocess.run(['sudo', 'make', 'install'], stdout=subprocess.PIPE, universal_newlines=True)

            print('Everything done, BE::Shell is now installed.\nIf you want to start it run "kquitapp plasmashell; sleep 2; be.shell"')

    def backup():

        bk_path = os.path.expanduser('~/.local/share/be.shell/backup')

        try:
            os.makedirs(bk_path)
        except FileExistsError:
            pass
        except Exception as ex:
            print(ex)

        tmp_dir = tempfile.mkdtemp(dir=bk_path)
        _tmp_dir = os.path.join(tmp_dir, Theme.name())

        shutil.copytree(Theme.path(), _tmp_dir)
        shutil.copy2(Configuration.main_file(), _tmp_dir)

        os.chdir(bk_path)

        for dirs in os.listdir(os.getcwd()):
            _dir = dirs
            archive.compress(_dir, bk_path, name=Theme.name())
            shutil.rmtree(tmp_dir)

        print('Everything done correctly. To restore your backup launch the script with the xxx flag')
