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

global format_file
format_file = os.path.join(beshell.Theme.path(), 'twolame', 'playlist.format')
format_file2 = os.path.join(beshell.Theme.path(), 'twolame', 'current_song.format')

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

    cs = client.currentsong()['title'][:20]

    client.iterate = True
    playlist_info = []

    for song in client.playlistinfo():

        pos_val = int(song['pos']) + 1
        pos = str(pos_val)
#        _pos_val = str(pos_val)

#        if len(_pos_val) == 1:
#            pos = str('0' + str(pos_val))
#        else:
#            pos = str(pos_val)

        if len(song['title']) > 30:
            title = str(song['title'])[:28] + '..'
        else:
            title = song['title']

        artist = song['artist']

        if len(song["time"]) >= 3:
            time = int(song["time"])/60
            time = str(time)
            if len(time) > 4:
                time = time[:4]
            elif len(time) == 3:
                time = time + '0'
        elif int(song["time"]) >= 60:
            time = int(song["time"])/60
            time = str(time)
            if len(time) > 4:
                time = time[:4]
            elif len(time) == 3:
                time = time + '0'
        else:
            time = '0.' + song["time"]

        out = [pos, title, artist, time]

        o = methods.create_dict(out)

        if title[:20] == cs:
            outstring = methods.insert_data(methods.format_string(format_file2), o)
        else:
            outstring = methods.insert_data(methods.format_string(format_file), o)

        playlist_info.append(outstring)

    return(playlist_info)

#retrive cover image(s)
def cover_finder(path, client):

    """(image) return the cover image for the current song or a blank one if
    any cover is found"""

    path = os.path.expanduser(path)
    default_image = os.path.join(beshell.Theme.path(), 'twolame', 'blank.jpg')

    if os.path.exists(path):
        i = os.path.join(path, process_mpd(client)[5], process_mpd(client)[7], 'cover.jpg')
        if os.path.isfile(i):
            im = i
        else:
            im = default_image
    else:
        im = default_image

    return(im)

def cover(path, client):

    """(dict) return a dict with the cover found by cover_finder function"""

    try:
        client.connect('localhost', 6600)
    except Exception:
        pass

    im = cover_finder(path, client)

    return({'{cover}': im})
