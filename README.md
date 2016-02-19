[![Build Status](https://travis-ci.org/Krinkle/pywiki-fileprotectionsync.svg?branch=master)](https://travis-ci.org/Krinkle/pywiki-fileprotectionsync)

# pywiki-fileprotectionsync

## Production

* [User:KrinkleBot at Wikimedia Commons](https://commons.wikimedia.org/wiki/User:KrinkleBot)
* [Commons:Auto-protected files](https://commons.wikimedia.org/wiki/Commons:Auto-protected_files)


## Setup

Fetch code:
```bash
# (you in ~/src)
$ git clone --depth 1 https://git.wikimedia.org/git/pywikibot/compat.git pywikibot-compat
$ git clone https://github.com/Krinkle/pywiki-fileprotectionsync.git
```

Configure pywikibot:
```bash
# (you in ~/src/pywikibot-compat)
$ cat .pwd
**

$ cat user-config.py
# -*- coding: utf-8  -*-
family = 'commons'
mylang = 'commons'
usernames['commons']['commons'] = u'KrinkleBot'
sysopnames['commons']['commons'] = u'KrinkleBot'
password_file = '.pwd'
```

Configure fileprotectionsync:
```bash
# (you in ~/src/pywiki-fileprotectionsync)
$ cp fileprotectionsync_config-sample.py fileprotectionsync_config.py
$ $EDITOR fileprotectionsync_config.py

# (you in ~/)
$ cat liveprotect-run.sh 
#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:~/src/pywikibot-compat/:~/src/ts-krinkle-pywiki/
python $HOME/src/ts-krinkle-pywiki/fileprotectionsync.py

$ chmod +x liveprotect-run.sh

$ cat crontab.txt
0,15,30,45 * * * * /usr/bin/jsub -N fileprotectionsync -once -quiet -mem 500m ~/liveprotect-run.sh
```
