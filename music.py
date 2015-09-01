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
from mpd import MPDClient
from PIL import Image

#initialize client
client = MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect('localhost', 6600)
status = client.status()['state']

#retrive mpd info
def state():
    mpd_status = mpd_client.status()['state']
    mpd_volume = mpd_client.status()['volume']
    return(mpd_status, mpd_volume)

#retrive current song info
def current():
    if not mpd_status == 'stop':
        c_artist = mpd_client.currentsong()['artist']
        c_title = mpd_client.currentsong()['title']
        c_album = mpd_client.currentsong()['album']
        c_track = mpd_client.currentsong()['track']
    else:
        c_artist = 'n/a'
        c_title = 'n/a'
        c_album = 'n/a'
        c_track = 'n/a'
    return(c_track, c_title, c_artist, c_album)

#retrive mpd option
def option():
    mpd_random = mpd_client.status()['random']
    mpd_repeat = mpd_client.status()['repeat']
    mpd_consume = mpd_client.status()['consume']

#retriving playlist info
def playlist():
    client.iterate = True
    for song in client.playlistinfo():
        if len(song['pos']) == 1:
            pos_val = int(song['pos']) + 1
            pos = str('0' + str(pos_val))
        else:
            pos_val = int(song['pos']) + 1
            pos = str(pos_val)
        if len(song['title']) > 30:
            title = str(song['title'])[:28] + '..'
        else:
            title = song['title']
        print(pos, '-', title, song['artist'])

#retrive cover image(s)
#def cover_finder():

def cover():
    im = Image.open('/home/nemo/.local/share/be.shell/blank.jpg') #aggiungere l'output di cover finder
    re_im = im.resize((400, 400))   #resize the image
    cover_im = re_im
    return(cover_im)
    #box = (0, 200, 400, 400)        #choose the dimensions of the crop image
    #region = re_im.crop(box)        #crop the image with box dimensions
    #region.show()                   #show image in preview window
