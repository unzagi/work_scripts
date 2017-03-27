from lxml import html
import requests

page = requests.get('https://kb.juniper.net/InfoCenter/index?page=content&id=KB21476')
tree = html.fromstring(page.content)



platform = tree.xpath('//*[@id="moduleAppMain"]/div/div/div[4]/div[3]/h3[7]/text()')
model = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[1]/a[1]/text()')
jtacRV = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[2]/text()')
releaseType = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[3]/text()')
LastUpdated = tree.xpath('//*[@id="Je"]/tbody/tr[12]/td[4]/text()')

print("Platform: " + ' '.join(platform))
print("Model: " + ' '.join(model))
print("JTAC Software: " + ' ' .join(jtacRV))
print("Release Type: " + ' '.join(releaseType))
print("Last Updated: " + ' '.join(LastUpdated))
