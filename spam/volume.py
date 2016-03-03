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

import os, sys
import alsaaudio

def alsa_info(mixer):

    if mixer.getmute()[0] == '0':
        mute = False
    else:
        mute = True

    try:
        if mixer.getvolume()[0] != mixer.getvolume()[1]:
            mixer.setvolume(int(mixer.getvolume()[0]))
            volume = mixer.getvolume()[0]
        else:
            pass
    except IndexError:
        volume = mixer.getvolume()[0]

    return([mute, str(volume)])
