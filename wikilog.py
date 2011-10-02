# Script to log messages to a wikipage from IRC
# For help on installing, check README
# version 1.0.2
# 
# (C) Krinkle, 2010
# (C) Pywikipedia bot team, 2003-2010
#
# Distributed under the terms of the MIT license.
#
import wikipedia
import datetime

site=wikipedia.getSite('en','cvnwiki')
logname=u"Developer_Log"
rightsname=u"Rights_Log"

months=["January","February","March","April","May","June","July","August","September","October","November","December"]

def log(message,author):
	targetpage=wikipedia.Page(site,logname)
	lines=targetpage.get().split('\n')
	position=0
	# Try extracting latest date header
	for line in lines:
		position+=1
		if line.startswith("=="):
			undef,month,day,undef=line.split(" ",3)
			break

	# Um, check the date
	now=datetime.datetime.utcnow()
	logline="* %02d:%02d %s: %s" % ( now.hour, now.minute, author, message )
	if months[now.month-1]!=month or now.day!=int(day):
		lines.insert(0,"")
		lines.insert(0,logline)
		lines.insert(0,"== %s %d =="%(months[now.month-1],now.day))
	else:
		lines.insert(position,logline)
	targetpage.put('\n'.join(lines),"%s (%s)"%(message,author))

def rights(message,author):
	targetpage=wikipedia.Page(site,rightsname)
	lines=targetpage.get().split('\n')
	position=0
	# Try extracting latest date header
	for line in lines:
		position+=1
		if line.startswith("=="):
			undef,month,day,undef=line.split(" ",3)
			break

	# Um, check the date
	now=datetime.datetime.utcnow()
	logline="* %02d:%02d %s: %s" % ( now.hour, now.minute, author, message )
	if months[now.month-1]!=month or now.day!=int(day):
		lines.insert(0,"")
		lines.insert(0,logline)
		lines.insert(0,"== %s %d =="%(months[now.month-1],now.day))
	else:
		lines.insert(position,logline)
	targetpage.put('\n'.join(lines),"%s (%s)"%(message,author))
