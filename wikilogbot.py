# Script to log messages to a wikipage from IRC
# For help on installing, check README.
#
# @version 1.1.0 (2011-10-02)
# @copyright Krinkle, 2010-2011
# @license Distributed under the terms of the MIT license.
#
from ircbot import SingleServerIRCBot
from irclib import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr
import time
import datetime
import wikilog

class LogBot(SingleServerIRCBot):
	def __init__(self, joinchannels, nickname, server, port, nickserv, nickservpassword, initialstatus, msgs_help, info_help):
		SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
		self.joinchannels = joinchannels
		self.nickname = nickname
		self.nickserv = nickserv
		self.nickservpassword = nickservpassword
		self.currentstatus = initialstatus
		self.msgs_help = msgs_help
		self.info_help = info_help
		self.statuslastmodtime = u'?'
		self.statuslastmodauthor = u'?'
		self.monthsnames=["January","February","March","April","May","June","July","August","September","October","November","December"]

	def on_nicknameinuse(self, c, e):
		c.nick(c.get_nickname() + "_")

	def on_unavailresource(self, c, e):
		c.nick(c.get_nickname() + "_")

	def on_welcome(self, c, e):
		c.privmsg(self.nickserv,"identify "+self.nickservpassword)
		c.privmsg(self.nickserv,"ghost "+self.nickname+" "+self.nickservpassword)
		c.privmsg(self.nickserv,"release "+self.nickname+" "+self.nickservpassword)
		time.sleep(1)
		for ch in self.joinchannels:
			c.join(ch)

	def on_pubmsg(self, c, e):
		author,rest=e.source().split('!')
		line=e.arguments()[0]
		chan=self.channels[e.target()]
		if chan.is_voiced(author) or chan.is_oper(author):
			if line.startswith("!help"):
				c.privmsg(e.target(),self.msgs_help)
			if line.startswith("!info"):
				c.privmsg(e.target(),self.info_help)
			if line.startswith("!log "):
				undef,message=line.split(" ",1);
				try:
					wikilog.log(message,author)
					c.privmsg(e.target(),"Logged the message, "+author+".")
				except: c.privmsg(e.target(),"I failed :(")
			elif line.startswith("!rights "):
				undef,message=line.split(" ",1);
				try:
					wikilog.rights(message,author)
					c.privmsg(e.target(),"Rights log has been updated, "+author+".")
				except: c.privmsg(e.target(),"I failed :(")
			elif line.startswith("!disconnect"):
				 self.disconnect()
			elif line.startswith("!exit"):
				 self.die()
			elif line.startswith("!donick "):
				undef,message=line.split(" ",1);
				c.nick(message)
			elif line.startswith("!updatestatus "):
				undef,message=line.split(" ",1);
				try:
					self.currentstatus = message
					now=datetime.datetime.utcnow()
					self.statuslastmodtime = "%02d:%02d, %d %s %d" % ( now.hour, now.minute, now.day, self.monthsnames[now.month-1], now.year )
					self.statuslastmodauthor = author
					c.privmsg(e.target(),"Status updated, "+author+".")
				except:
					c.privmsg(e.target(), "Error updating status, "+author+".")
			elif line.startswith("!status"):
				c.privmsg(e.target(),"Status: "+self.currentstatus+" (Last modified by "+self.statuslastmodauthor+" at "+self.statuslastmodtime+")")
		else:
			if line.startswith("!status"):
				c.privmsg(e.target(),"Status: "+self.currentstatus+" (Last modified by "+self.statuslastmodauthor+" at "+self.statuslastmodtime+")")

def main():
	server=u"irc.freenode.net"
	port=6667
	joinchannels=["#botwar"]
	nickname=u"wikilogbot"
	nickserv=u"NickServ"
	initialstatus=u"All OK!"
	msgs_help=u"This is the default !help message."
	info_help=u"This is the default !info message."
	nickservpassword=u"**********"
	bot = LogBot(joinchannels, nickname, server, port, nickserv, nickservpassword, initialstatus, msgs_help, info_help)
	bot.start()

if __name__ == "__main__":
	main()
