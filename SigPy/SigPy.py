# import
import urllib.request, urllib.parse
import base64
import json

# backend access parameters
url = 'https://backend.sigfox.com/api/devices/XXXXXXXX/messages'
usr = "login"
pwd = "password"

# access to sigfox backend-api
base64string = base64.encodestring(('%s:%s' % (usr, pwd)).encode("utf-8"))[:-1]
headers = {
    "Authorization": "Basic %s" % base64string.decode("utf-8")
}
req = urllib.request.Request(url, headers=headers)

# gets json raw data for dump...
with urllib.request.urlopen(req) as res:
    html = res.read().decode("utf-8")
    data = json.loads(html)  
    print(json.dumps(data, indent=2))