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
import os, sys, io
import os.path

#import web module(s)
import mpd

#initialize client
mpd_client = mpd.MPDClient()
mpd_client.timeout = 10
mpd_client.idletimeout = None
mpd_client.connect('localhost', 6600)

#retrive mpd info
mpd_status = mpd_client.status()['state']
mpd_volume = mpd_client.status()['volume']

#retrive current song info
c_artist = mpd_client.currentsong()['artist']
c_title = mpd_client.currentsong()['title']
c_album = mpd_client.currentsong()['album']
c_track = mpd_client.currentsong()['track']

#retrive mpd option
mpd_random = mpd_client.status()['random']
mpd_repeat = mpd_client.status()['repeat']
mpd_consume = mpd_client.status()['consume']

#start defining function
def playlist():
    mpd_client.iterate = True
    for song in mpd_client.playlistinfo():
        if len(song['title']) > 30:
            title = str(song['title'])[:28] + '..'
        else:
            title = song['title']
        print(song['id'] if len(song['id']) is not 1 else '0' + song['id']), '-', title, song['artist'])
