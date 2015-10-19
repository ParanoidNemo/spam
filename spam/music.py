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
import re

#import web module(s)
import musicpd
from PIL import Image
from spam import beshell

#-------------------------format informations-----------------------------------

def insert_data(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

format_string = ''
with open(os.path.join(beshell.Theme.path(), 'twolame', 'playlist.format')) as f:
    for line in f:
        if line.startswith('#'):
            continue
        format_string += line

format_string = re.sub(r'>\s<', '><', format_string)
format_string = re.sub(r'\n', '', format_string)

#-------------------------------------------------------------------------------

def process_mpd(client):

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

    try:
        client.connect('localhost', 6600)
    except Exception:
        pass

    client.iterate = True
    playlist_info = []

    for song in client.playlistinfo():

        pos_val = int(song['pos']) + 1
        _pos_val = str(pos_val)

        if len(_pos_val) == 1:
            pos = str('0' + str(pos_val))
        else:
            pos = str(pos_val)

        if len(song['title']) > 30:
            title = str(song['title'])[:28] + '..'
        else:
            title = song['title']

        artist = song['artist']

        _out = [pos, title, artist]
        o = {}

        for index, item in enumerate(_out):
            i = '{' + str(index) + '}'
            o[i] = item

        outstring = insert_data(format_string, o)

        playlist_info.append(outstring)

    return(playlist_info)

#retrive cover image(s)
def cover_finder(path, client):

    path = os.path.expanduser(path)
    default_image = os.path.join(beshell.Theme.path(), 'twolame', 'blank.jpg')

    if os.path.exists(path):
        try:
            im = os.path.join(path, process_mpd(client)[5], process_mpd(client)[7], 'cover.jpg')
        except FileNotFoundError:
            im = default_image
    else:
        im = default_image

    return(im)

def cover(path, client):

    cover = {}
    im = cover_finder(path, client)

    #re_im = im.resize((400, 400))   #resize the image

    cover['{cover}'] = im
    return(cover)

    #box = (0, 200, 400, 400)        #choose the dimensions of the crop image
    #region = re_im.crop(box)        #crop the image with box dimensions
    #region.show()                   #show image in preview window
