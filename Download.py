# -*- coding: utf-8 -*-
import urllib

f = urllib.urlopen("https://www.youtube.com/watch?v=WYeDsa4Tw0c")
f = f.read()
f.join("")

fw = open("DownHtml.html",'w')
fw.write(f)
fw.close()
print f
