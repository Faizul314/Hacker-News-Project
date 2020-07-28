import requests
from bs4 import BeautifulSoup
import pprint

res1 = requests.get('https://news.ycombinator.com')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
res3 = requests.get('https://news.ycombinator.com/news?p=3')

soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
soup3 = BeautifulSoup(res3.text, 'html.parser')

links1 = soup1.select('.storylink')
links2 = soup2.select('.storylink')
links3 = soup3.select('.storylink')

subtext1 = soup1.select('.subtext')
subtext2 = soup2.select('.subtext')
subtext3 = soup3.select('.subtext')

mega_links = links1 + links2 + links3
mega_subtext = subtext1 + subtext2 + subtext3

def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key = lambda k: k['votes'], reverse = True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title': title, 'href': href, 'votes': points})
    return sort_stories_by_vote(hn)
pprint.pprint(create_custom_hn(mega_links, mega_subtext))

