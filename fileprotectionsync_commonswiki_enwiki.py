# -*- coding: utf-8  -*-
# Script to create a gallery of files used on one wiki's page
# on another wiki's wiki. Commonly used to protect files on
# a repository wiki that are used on a local wiki. In that case
# the target page on the repository wiki should have cascading sysop-protection.
#
# @author Betacommand
# @maintainer Krinkle
# @license CC-BY-SA 3.0
# @revision 11
#
import wikipedia
import urllib
import simplejson
commons_site = wikipedia.getSite('commons','commons')
config_data = [
              # [
              #  site, 
              #  page to update, 
              #  [list of pages to get data from], 
              #  string to include above the gallery
              # ],
                [
                  u'en.wikipedia.org',
                  u'User:Δ',
                  [u'Main Page',u'Wikipedia:Main Page/Tomorrow']
                  ,u'<noinclude>This is an automatically compiled / updated gallery of images used on [[:en:Main Page]] and [[:en:Wikipedia:Main Page/Tomorrow]] </noinclude>as of \'\'\'{{ISOdate|{{REVISIONYEAR}}-{{REVISIONMONTH}}-{{REVISIONDAY2}}}}\'\'\'<noinclude>. Please do not manually alter the image list.</noinclude><gallery widths="245" heights="147">\n'
                  u'Sync. cascading protection of en.wikipedia.org main page (BOT - r12)',
                ],
              ]

def main():
  for config in config_data:
    str = config[3]
    mpimages = []
    for pg in config[2]:
      mpimages.extend(get_images(config[0],pg))
    mpimages = sorted(set(mpimages))
    for cimage in mpimages:
      str+=u'%s\n' % cimage
    str+=u'</gallery>'
    wikipedia.Page(commons_site,config[1]).put(str,config[4])
def get_images(site,title):
  mpimages = []
  path = u'http://%s/w/api.php?action=query&prop=images&titles=%s&imlimit=500&format=json' % (site,title)
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