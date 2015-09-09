# -*- coding: utf-8 -*-
import urllib
import pygtk
pygtk.require('2.0')
import gtk

#***********************[Get Url from Clipboard]***********************
clipboard = gtk.clipboard_get()
url_name = clipboard.wait_for_text()
#url_name = "https://www.youtube.com/watch?v=WYeDsa4Tw0c" #test url

#***********************[Get Youtube-Page and Create File]***********************
youtube_page = urllib.urlopen(url_name)
youtube_page = youtube_page.read()
youtube_page.join("")

file_name = "youtube_page_temp.html"
fw = open(file_name,'w')
fw.write(youtube_page)
fw.close()

#***********************[Read Youtube-Page and Extract Values]***********************
f = open(file_name, 'r')

i = 0

views_label_start = "</ul></div></div></div><div id=\"watch8-sentiment-actions\"><div id=\"watch7-views-info\"><div class=\"watch-view-count\">"
views_label_end = "</div>"

likes_label_start = "      <button class=\"yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked"
likes_label_end = "</span></button>"

dislikes_label_start = "      <button class=\"yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked"
dislikes_label_end = "</span></button>"

mid_label = "<span class=\"yt-uix-button-content\">"

for line in f:
	i+=1
	if (line.find(views_label_start)<>-1):
		views_count = ""
		#print i,line
		for j in range(len(views_label_start),(len(line)-len(views_label_end)-1)):
			views_count += line[j]
	if (line.find(likes_label_start)<>-1):
		likes_count = ""
		#print i,line
		for j in range((line.find(mid_label)+len(mid_label)),(len(line)-len(likes_label_end)-1)):
			likes_count += line[j]
	if (line.find(dislikes_label_start)<>-1):
		dislikes_count = ""
		#print i,line
		for j in range((line.find(mid_label)+len(mid_label)),(len(line)-len(dislikes_label_end)-1)):
			dislikes_count += line[j]

#***********************[Print Values and Processed Data]***********************
print ""
#print "File Name:",file_name
print "Views:",views_count
print "Likes:",likes_count
print "Dislikes:",dislikes_count

views_count = views_count.replace(".","")
views_count = int(views_count.replace(" προβολές",""))
likes_count = int(likes_count.replace(".",""))
dislikes_count = int(dislikes_count.replace(".",""))
V_L = int(views_count) / (int(likes_count)*1.0)
L_D = int(likes_count) / (int(dislikes_count)*1.0)

print "V/L:",V_L
print "L/D:",L_D
print ""

f.close()
