import scraperwiki
import lxml.html
html = scraperwiki.scrape("http://www.juniper.net/support/downloads/?p=srx300#sw")
root = lxml.html.fromstring(html)

##print(html)
print(root)
print(html)

##
##path = tree.xpath('//*[@id="swjFix"]/text()')
##
##print(tree)
##
##platform = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[1]/text()')
####jtacRV = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[2]/text()')
####releaseType = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[3]/text()')
##LastUpdated = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[4]/text()')
##
##print("Platform: " + ' '.join(platform))
##print("JTAC Software: " + ' ' .join(jtacRV))
##print("Release Type: " + ' '.join(releaseType))
##print("Last Updated: " + ' '.join(LastUpdated))
