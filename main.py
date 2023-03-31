#      Get started - Guide
#
#      1. Get access token
#   Open mastodon. And, open "Preferences".
#   Open development tab. Click "New application".
#   Set name, Scopes. And, submit.
#
#      2. Install mastodon.py
#   Install mastodon.py.
#   Open, commandline. and, install.
#   `pip install mastodon.py`
#
#       3. Done stand by. Let's run.
#   `cd < Downloaded directory >`
#   `python main.py`

from mastodon import Mastodon
import re

allhash = [
    'helloworld'
]

mastodon = Mastodon(
    client_id='###',
    client_secret='###',
    access_token='###',
    api_base_url='https://mstdn.jp'
)

print('\nLocal\n')

toots = mastodon.timeline_local()

for toot in toots:
    print(toot['account']['display_name'] + ' : ' + re.sub(re.compile('<.*?>'), '', toot['content']))


print('\nHome\n')

toots = mastodon.timeline_home()

for toot in toots:
    print(toot['account']['display_name'] + ' : ' + re.sub(re.compile('<.*?>'), '', toot['content']))


print('\nPublic\n')

toots = mastodon.timeline_public()

for toot in toots:
    print(toot['account']['display_name'] + ' : ' + re.sub(re.compile('<.*?>'), '', toot['content']))

for hs in allhash:
    print('\nHashtag - '+hs+'\n')
    toots = mastodon.timeline_hashtag(hashtag='')
    for toot in toots:
        print(toot['account']['display_name'] + ' : ' + re.sub(re.compile('<.*?>'), '', toot['content']))