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

import os, sys, re
import subprocess, collections
import multiprocessing

from spam import methods
from spam import check

def process_exists(proc):
    command_line = "ps -u " + os.environ["USER"]
    for line in methods.call_command(command_line).split():
        if line == proc:
            return True

DE_DICT = collections.OrderedDict([
        ('cinnamon', 'Cinnamon'),
        ('gnome-session', 'GNOME'),
        ('ksmserver', 'KDE'),
        ('mate-session', 'MATE'),
        ('xfce4-session', 'Xfce'),
        ('lxsession', 'LXDE'),
        ('', 'None'),
        ])

WM_DICT = collections.OrderedDict([
        ('awesome', 'Awesome'),
        ('beryl', 'Beryl'),
        ('blackbox', 'Blackbox'),
        ('bspwm', 'bspwm'),
        ('dwm', 'DWM'),
        ('enlightenment', 'Enlightenment'),
        ('fluxbox', 'Fluxbox'),
        ('fvwm', 'FVWM'),
        ('herbstluftwm', 'herbstluftwm'),
        ('i3', 'i3'),
        ('icewm', 'IceWM'),
        ('kwin_x11', 'KWin'),
        ('metacity', 'Metacity'),
        ('musca', 'Musca'),
        ('openbox', 'Openbox'),
        ('pekwm', 'PekWM'),
        ('ratpoison', 'ratpoison'),
        ('scrotwm', 'ScrotWM'),
        ('subtle', 'subtle'),
        ('monsterwm', 'MonsterWM'),
        ('wmaker', 'Window Maker'),
        ('wmfs', 'Wmfs'),
        ('wmii', 'wmii'),
        ('xfwm4', 'Xfwm'),
        ('emerald', 'Emerald'),
        ('compiz', 'Compiz'),
        (re.compile('xmonad-*'), 'xmonad'),
        ('qtile', 'QTile'),
        ('wingo', 'Wingo'),
        ('', 'None'),
        ])

def fs(mountpoint):
    command_line = "df -TPh " + os.path.expanduser(mountpoint)

    values = [line for line in methods.call_command(command_line).split('\n') if line][1].split()
    free_perc = 100 - int(values[5][:-1])
    free_perc = str(free_perc) + '%'
    values.append(free_perc)

    return(values)

def ram():
    command_line = "free -m"

    values = ''.join(line for line in methods.call_command(command_line).split('\n') if line.startswith('Mem:')).split()

    used_perc = int(values[2]) * 100 // int(values[1])
    free_perc = 100 - used_perc

    values.append(str(used_perc))
    values.append(str(free_perc))

    return(values)

def cpu():
    command_line = "cat /proc/cpuinfo"

    collect_info = [line.split(":") for line in methods.call_command(command_line).split("\n") if line]
    infodict = {}
    for k, v in collect_info:
        infodict[k.strip()] = v.strip()

    return(infodict["model name"])

def machine():

    machine_info = []
    for item in os.uname():
        machine_info.append(item)

    return(machine_info)

def uptime():
    with open("/proc/uptime") as upfile:
        raw_time = upfile.read()
        uptime = int(raw_time.split('.')[0])
        ut = methods.time_convertion(uptime)

    return(ut)

def wm():
    wm = ""
    for key in WM_DICT.keys():
        if process_exists(key):
            wm = key
            break
    return(WM_DICT[wm])

def de():
    de = ""
    for key in DE_DICT.keys():
        if process_exists(key):
            de = key
            break
    return(DE_DICT[de])

def distro():

    """This function check what is the distro you are on"""

    if check.prg("aptitude"):
        distro = "Debian"
    elif check.prg("dnf"):
        distro = "Fedora"
    elif check.prg("pacman"):
        distro = "Arch Linux"
    else:
        distro = "GNU/Linux"

    return(distro)
