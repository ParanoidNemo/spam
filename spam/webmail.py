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

"""This module define a function that check the email into a choosen inbox.

Global functions defined:
    - process_mailbox: return a info with mailbox unread messages"""

import os
import re
import imaplib
import email
import datetime

from spam import beshell
from spam import methods

global format_file
format_file = os.path.join(beshell.Theme.path(), 'twolame', 'single_mail.format')

def process_mailbox(mailbox):

    """(list) return a list with html formatted unread messages from a choosen mailbox.
    Require as only argument the mailbox initialized and selected using imaplib std
    module functions"""

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

        try:
            if len(msg['Subject']) > 40:
                _sub = msg['Subject'][:37] + '...'
            else:
                _sub = msg['Subject']
        except Exception:
            _sub = ''

        _date = msg['Date']

        _out = [_from, _num, _sub, _date]

        o = methods.create_dict(_out)

        outstring = methods.insert_data(methods.format_string(format_file), o)

        info.append(outstring)

    return(info)
