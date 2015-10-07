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

import imaplib
import email
import datetime

def process_mailbox(mailbox):
    rv, data = mailbox.search(None, "unseen")
    if rv != 'OK':
        print("No messages found!")

    for num in data[0].split():
        rv, data = mailbox.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        _num = num.decode("ASCII")
        print('From:', msg['From'])
        print('Message %s: %s' % (_num, msg['Subject']))
        print('Raw Date:', msg['Date'], '\n')
        #date_tuple = email.utils.parsedate_tz(msg['Date'])
        #if date_tuple:
        #    local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        #    print("Local Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S"))
