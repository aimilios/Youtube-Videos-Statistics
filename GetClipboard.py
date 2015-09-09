# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

clipboard = gtk.clipboard_get()
text = clipboard.wait_for_text()

print text

