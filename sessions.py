''' if you’re dealing with a more complicated site that frequently modifies cookies without warning, or if you’d rather not
even think about the cookies to begin with? The Requests session function works
perfectly'''

import requests
session = requests.Session()
params = {'username': 'username', 'password': 'password'}
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)
