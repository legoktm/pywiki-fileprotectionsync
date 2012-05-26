# -*- coding: utf-8  -*-
# Configuration file for fileprotectionsync.py

editsummary = u'Update [[Commons:Auto-protected files|auto-protection]]'
wikitext_start = u'{{Auto-protected files gallery}}<gallery widths="50" heights="30">\n'
wikitext_end = u'</gallery>'
wikis = [
  {
    'sourcewiki': u'en.wikipedia.org',
    'sourcepages': [u'Main Page',u'Wikipedia:Main Page/Tomorrow'],
#    'targetpage': u'Commons:Auto-protected files/wikipedia/en',
    'targetpage': u'Commons:Sandbox',
  },
  {
    'sourcewiki': u'pl.wikipedia.org',
    'sourcepages': [u'Strona główna'],
#    'targetpage': u'Commons:Auto-protected files/wikipedia/pl',
    'targetpage': u'Commons:Sandbox',
  },
  {
    'sourcewiki': u'zh.wikipedia.org',
    'sourcepages': [u'Wikipedia:首页/全部',u'Wikipedia:首页/明天'],
#    'targetpage': u'Commons:Auto-protected files/wikipedia/zh',
    'targetpage': u'Commons:Sandbox',
  },
]
