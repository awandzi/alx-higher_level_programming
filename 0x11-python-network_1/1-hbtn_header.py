#!/usr/bin/python3
import urllib.request
import sys
with urllib.request.urlopen(url) as response:
            request_Id = response.headers.get('X-Request-Id')
