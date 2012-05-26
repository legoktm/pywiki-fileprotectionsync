# -*- coding: utf-8  -*-
# Script to create a gallery of files used on one wiki's page
# on another wiki's wiki. Commonly used to protect files on
# a repository wiki that are used on a local wiki. In that case
# the target page on the repository wiki should have cascading sysop-protection.
#
# @author Betacommand
# @author Krinkle
# @license CC-BY-SA 3.0
# @revision 22 (2012-05-27)
#
import wikipedia
import urllib
import simplejson
import fileprotectionsync_config as config
commons_site = wikipedia.getSite('commons','commons')
config.editsummary += ' (BOT - r22)'

def main():
  for wiki in config.wikis:
    str = config.wikitext_start
    mpimages = []
    for pg in wiki['sourcepages']:
      mpimages.extend(get_images(wiki['sourcewiki'], pg))
    mpimages = sorted(set(mpimages))
    for cimage in mpimages:
      str += u'File:%s\n' % cimage
    str += config.wikitext_end
    wikipedia.Page(commons_site, wiki['targetpage']).put(str, config.editsummary)

def get_images(site, title):
  title=urllib.urlencode({'titles': title.encode('utf-8')})
  mpimages = []
  path = u'http://%s/w/api.php?action=query&prop=images&%s&imlimit=500&format=json' % (site, title)
  tx = urllib.urlopen(path)
  json = tx.read()
  data = simplejson.loads(json)
  images = data['query']['pages'][data['query']['pages'].keys()[0]]['images']
  for image in images:
    if image['ns'] == 6:
      # Extract file name (remove File namespace prefix)
      # This allows non-English wikis to be fetched into an English wiki
      # Datei:Awesome_collection:_The_Example_(2006).jpg -> Awesome_collection:_The_Example_(2006).jpg
      mpimages.append(image['title'].split(':', 1)[1])
  return mpimages


if __name__ == '__main__':
    try:
        main()
    finally:
        wikipedia.stopme()