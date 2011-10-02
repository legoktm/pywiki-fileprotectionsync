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
def main():

  str = u'<noinclude>This is an automatically compiled / updated gallery of images used on [[:en:Main Page]] and [[:en:Wikipedia:Main Page/Tomorrow]] </noinclude>as of \'\'\'{{ISOdate|{{subst:CURRENTYEAR}}-{{subst:CURRENTMONTH}}-{{subst:CURRENTDAY2}}}}\'\'\'<noinclude>. Please do not manually alter the image list.</noinclude><gallery widths="245" heights="147">\n'
  mpimages = []
  commons_site = wikipedia.getSite('commons','commons')
  path = u'http://en.wikipedia.org/w/api.php?action=query&prop=images&titles=Main%20Page&imlimit=500&format=json'
  tx = urllib.urlopen(path)
  json = tx.read()
  data = simplejson.loads(json)
  images = data['query']['pages']['15580374']['images']
  for image in images:
    if image['ns']==6:
      mpimages.append(image['title'])
  path = u'http://en.wikipedia.org/w/api.php?action=query&prop=images&titles=Wikipedia:Main%20Page/Tomorrow&imlimit=500&format=json'
  tx = urllib.urlopen(path)
  json = tx.read()
  data = simplejson.loads(json)
  images = data['query']['pages']['6119248']['images']
  for image in images:
    if image['ns']==6:
      mpimages.append(image['title'])
  mpimages = sorted(set(mpimages))
  for cimage in mpimages:
    str+=u'%s\n' % cimage
  str+=u'</gallery>'
  wikipedia.Page(commons_site,u'Commons:Sandbox').put(str,'(BOT) fileprotectionsync-commonswiki-enwiki.py r11)')
if __name__ == '__main__':
    try:
        main()
    finally:
        wikipedia.stopme()