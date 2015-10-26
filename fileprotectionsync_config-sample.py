# Configuration file for fileprotectionsync.py

editsummary = u'Update [[Commons:Auto-protected files|auto-protection]]'
wikitext_start = u'{{Auto-protected files gallery}}<gallery widths="80" heights="80">\n'
wikitext_end = u'</gallery>'
wikis = [
    {
        'sourcewiki': u'de.wikipedia.org',
        'sourcepages': [u'Wikipedia:Hauptseite', u'Wikipedia:Hauptseite/morgen'],
        # 'targetpage': u'Commons:Auto-protected files/wikipedia/de',
        'targetpage': u'Commons:Sandbox',
    },
    {
        'sourcewiki': u'en.wikipedia.org',
        'sourcepages': [u'Main Page', u'Wikipedia:Main Page/Tomorrow'],
        # 'targetpage': u'Commons:Auto-protected files/wikipedia/en',
        'targetpage': u'Commons:Sandbox',
    },
    {
        'sourcewiki': u'en.wiktionary.org',
        'sourcepages': [u'Main Page'],
        # 'targetpage': u'Commons:Auto-protected files/wiktionary/en',
        'targetpage': u'Commons:Sandbox',
    },
    {
        'sourcewiki': u'fr.wikipedia.org',
        'sourcepages': [u'Wikipédia:Accueil principal'],
        # 'targetpage': u'Commons:Auto-protected files/wikipedia/fr',
        'targetpage': u'Commons:Sandbox',
    },
    {
        'sourcewiki': u'pl.wikipedia.org',
        'sourcepages': [u'Strona główna'],
        # 'targetpage': u'Commons:Auto-protected files/wikipedia/pl',
        'targetpage': u'Commons:Sandbox',
    },
    {
        'sourcewiki': u'zh.wikipedia.org',
        'sourcepages': [u'Wikipedia:首页/全部', u'Wikipedia:首页/明天'],
        # 'targetpage': u'Commons:Auto-protected files/wikipedia/zh',
        'targetpage': u'Commons:Sandbox',
    },
    {
        'sourcewiki': u'bn.wikipedia.org',
        'sourcepages': [u'প্রধান পাত'],
        # 'targetpage': u'Commons:Auto-protected files/wikipedia/bn',
        'targetpage': u'Commons:Sandbox',
    },
]
