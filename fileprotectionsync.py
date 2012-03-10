# -*- coding: utf-8  -*-
# Script to create a gallery of files used on one wiki's page
# on another wiki's wiki. Commonly used to protect files on
# a repository wiki that are used on a local wiki. In that case
# the target page on the repository wiki should have cascading sysop-protection.
#
# @author Betacommand
# @maintainer Krinkle
# @license CC-BY-SA 3.0
# @revision 15 (2011-10-16)
#
import wikipedia
import urllib
import simplejson
commons_site = wikipedia.getSite('commons','commons')
config_data = {
  'summary': u'Update [[Commons:Auto-protected files|auto-protection]] (BOT - r16)',
  'text_start': u'{{Auto-protected files gallery}}<gallery widths="50" heights="30">\n',
  'text_end': u'</gallery>'
}
config_wikis = [
  {
    'sourcewiki': u'en.wikipedia.org',
    'sourcepages': [u'Main Page',u'Wikipedia:Main Page/Tomorrow'],
#    'targetpage': u'Commons:Auto-protected files/wikipedia/en',
    'targetpage': u'Commons:Sandbox',
  },
#  {
#    'sourcewiki': u'zh.wikipedia.org',
#    'sourcepages': [u'Wikipedia:首页/全部',u'Wikipedia:首页/明天'],
##    'targetpage': u'Commons:Auto-protected files/wikipedia/zh',
#    'targetpage': u'Commons:Sandbox',
#  },
]

def main():
  for config in config_wikis:
    str = config_data['text_start']
    mpimages = []
    for pg in config['sourcepages']:
      mpimages.extend(get_images(config['sourcewiki'],pg))
    mpimages = sorted(set(mpimages))
    for cimage in mpimages:
      str+=u'%s\n' % cimage
    str+=config_data['text_end']
    wikipedia.Page(commons_site,config['targetpage']).put(str,config_data['summary'])
def get_images(site,title):
  title=urllib.urlencode({'titles':title.encode('utf-8')})
  mpimages = []
  path = u'http://%s/w/api.php?action=query&prop=images&%s&imlimit=500&format=json' % (site,title)
  tx = urllib.urlopen(path)
  json = tx.read()
  data = simplejson.loads(json)
  images = data['query']['pages'][data['query']['pages'].keys()[0]]['images']
  for image in images:
    if image['ns']==6:
      mpimages.append(image['title'])
  return mpimages


if __name__ == '__main__':
    try:
        main()
    finally:
        wikipedia.stopme()