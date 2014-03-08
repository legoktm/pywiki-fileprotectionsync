# [![Build Status](https://travis-ci.org/Krinkle/ts-krinkle-pywiki.png?branch=master)](https://travis-ci.org/Krinkle/ts-krinkle-pywiki) Krinkle's pywiki plugins


## Setup

Fetch code:
```bash
(you in ~/src) $ git clone --depth 1 https://git.wikimedia.org/git/pywikibot/compat.git pywikibot-compat
(you in ~/src) $ git clone https://github.com/Krinkle/ts-krinkle-pywiki.git
```

Configure pywikibot:
```bash
(you in ~/src/pywikibot-compat) $ cat .pwd
**
(you in ~/src/pywikibot-compat) $ cat user-config.py
# -*- coding: utf-8  -*-
family = 'commons'
mylang = 'commons'
usernames['commons']['commons'] = u'KrinkleBot'
usernames['cvnwiki']['en'] = u'Clogger'
sysopnames['commons']['commons'] = u'KrinkleBot'
password_file = '.pwd'
```

Configure fileprotectionsync:
```bash
(you in ~/src/ts-krinkle-pywiki) $ cp fileprotectionsync_config-sample.py fileprotectionsync_config.py
(you in ~/src/ts-krinkle-pywiki) $ nano fileprotectionsync_config.py

(you in ~) $ chmod +x liveprotect-run.sh; cat liveprotect-run.sh
#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:~/src/pywikibot-compat/:~/src/ts-krinkle-pywiki/
python $HOME/src/ts-krinkle-pywiki/fileprotectionsync.py

(you in ~) $ chmod +x liveprotect-submit.sh; cat liveprotect-submit.sh
jsub -once -N fileprotectionsync -mem 500m ~/liveprotect-run.sh

(you in ~) $ cat liveprotect-cron.txt
0,15,30,45 * * * * ~/liveprotect-submit.sh > /dev/null
```
