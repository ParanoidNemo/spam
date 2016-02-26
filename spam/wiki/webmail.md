webmail - Global webmail types
=====

The webmail module supplies one global function that check a particular mailbox, selected via imaplib module, and return a preformatted list containing the unreaded messages.

webmail.**process_mailbox(mailbox)** - Check if there are some unread emails into the selected mailbox and return a formatted list if there are any.