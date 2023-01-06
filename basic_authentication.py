"The Requests package contains an auth module specifically designed to handle HTTP authentication"

  
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url='http://pythonscraping.com/pages/auth/login.php', auth=auth)
print(r.text)
