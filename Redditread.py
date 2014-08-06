import urllib2
import os
from bs4 import BeautifulSoup
hdr = { 'User-Agent' : 'The python text post reader /u/ioanthecomputerguy using urllib2, espeak and BeautifulSoup4' }
page = urllib2.Request(raw_input("Enter reddit url: "), headers=hdr)
html = urllib2.urlopen(page).read()

soup = BeautifulSoup(html)
mydivs = soup.findAll("div", { "class" : "expando" })
title = soup.findAll("div", { "class" : "title" })
mydiv = mydivs[0]
print mydiv.text
f = open('file.txt','w')
f.write(mydiv.text.encode('utf-8'))
f.close()
opt = str(raw_input("1.Save as wav 2. Play out loud: "))
if opt == "1":
 os.popen("espeak -a 100 -w" + title[0].text + " -f file.txt")
elif opt == "2":
 os.popen("espeak -f file.txt")
os.system("rm file.txt")
 
