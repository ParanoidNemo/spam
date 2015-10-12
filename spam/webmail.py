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

import os
import re
import imaplib
import email
import datetime

def insert_data(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]), re.M)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)

format_string = ''
with open(os.path.expanduser('~/.kde4/share/apps/be.shell/Themes/Hydrogen/twolame/single_mail.format')) as f:
    for line in f:
        if line.startswith('#'):
            continue
        format_string += line

format_string = re.sub(r'>\s<', '><', format_string)
format_string = re.sub(r'\n', '', format_string)

def process_mailbox(mailbox):

    rv, data = mailbox.search(None, "unseen")

    if rv != 'OK':
        print("No messages found!")

    info = []
    for num in data[0].split():

        rv, data = mailbox.fetch(num, '(RFC822)')

        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        _num = num.decode("ASCII")
        _from = msg['From']

        if len(msg['Subject']) > 40:
            sub = msg['Subject'][:37] + '...'
        else:
            sub = msg['Subject']

        try:
            _message = sub
        except TypeError:
            _message = ''

        _date = msg['Date']

        _out = [_from, _num, _message, _date]
        o = {}
        for index, item in enumerate(_out):
            i = '{' + str(index) + '}'
            o[i] = item

        outstring = insert_data(format_string, o)

        info.append(outstring)

    return(info)
