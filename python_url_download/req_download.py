import requests
import sys
url = sys.argv[1]
r = requests.get("http://"+url+"/favicon.ico", allow_redirects=True)
open("/home/test/"+url+'_facebook.ico', 'wb').write(r.content)
