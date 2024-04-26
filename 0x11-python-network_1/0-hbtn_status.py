#!/usr/bin/python3
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
   html = response.read()
