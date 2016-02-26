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

"""This module define a set of functions that retrive information from mpd.
It depends from mudicpd module; you could install it using pip

Global functions defined:
    - process_mpd: connect to mpd and retrive information about current song and
    mpd options
    - playlist: return the actual playlist from mpd
    - cover_finder: retrive the cover for the current song
    - cover: return a dict contains the cover image"""

#import std module(s)
import os, sys, io
import re

#import web module(s)
import musicpd
from spam import beshell
from spam import methods

theme = beshell.Theme()

global format_file
format_file = os.path.join(theme.path, 'twolame', 'playlist.format')
format_file2 = os.path.join(theme.path, 'twolame', 'current_song.format')

def process_mpd(client):

    """(list) return a list containig mpd options and current song info. Require
    one argument, that is the client obj initialized with musicpd module"""

    try:
        client.connect('localhost', 6600)
    except Exception:           # need to find what execption raise
        pass

    sts, vol = client.status()['state'], client.status()['volume']
    rdm, rpt, con = client.status()['random'], client.status()['repeat'], client.status()['consume']

    if sts != 'stop':
        try:
            artist = client.currentsong()['artist']
            title = client.currentsong()['title']
            album = client.currentsong()['album']
            track = client.currentsong()['track']
        except Exception:
            artist = 'n/a'
            title = 'n/a'
            album = 'n/a'
            track = 'n/a'
    else:
            artist = 'n/a'
            title = 'n/a'
            album = 'n/a'
            track = 'n/a'

    return([sts, vol, rdm, rpt, con, artist, title, album, track])

#retriving playlist info
def playlist(client):

    """(list) return a html formatted list containig the actual playlist retrived from mpd"""

    try:
        client.connect('localhost', 6600)
    except Exception:
        pass

    try:
        cs = client.currentsong()['title'][:20]
    except Exception:
        cs = "n/a"

    client.iterate = True
    playlist_info = []

    for song in client.playlistinfo():

        pos_val = int(song['pos']) + 1
        pos = str(pos_val)

        if len(song['title']) > 30:
            title = str(song['title'])[:28] + '..'
        else:
            title = song['title']

        artist = song['artist']

        t = methods.time_convertion(int(song["time"]))
        time = str(t[2]) + '.' + str(t[3])

        tl = time.split(sep='.')

        if len(tl[-1]) < 2:
            time = time + '0'

        out = [pos, title, artist, time]

        o = methods.create_dict(out)

        if title[:20] == cs:
            outstring = methods.insert_data(methods.format_string(format_file2), o)
        else:
            outstring = methods.insert_data(methods.format_string(format_file), o)

        playlist_info.append(outstring)

    return(playlist_info)

#retrive cover image(s)
def cover(path, client):

    """(string) return the cover image for the current song or a blank one if
    any cover is found"""

    try:
        client.connect('localhost', 6600)
    except Exception:
        pass

    path = os.path.expanduser(path)
    default_image = os.path.join(theme.path, "twolame", "blank.jpg")

    if os.path.exists(path):
        i = os.path.join(path, process_mpd(client)[5], process_mpd(client)[7], "cover.jpg")
        i2 = os.path.join(path, process_mpd(client)[5], process_mpd(client)[7], "cover.png")
        if os.path.isfile(i):
            im = i
        elif os.path.isfile(i2):
            im = i2
        else:
            im = default_image
    else:
        im = default_image
    
    return(im)
