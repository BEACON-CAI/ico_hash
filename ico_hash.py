import mmh3 
import requests 
import codecs
import sys


url = sys.argv[1]
response = requests. get(url)
favicon = codecs.encode(response.content, "base64") 
hash = mmh3.hash(favicon)
print('http.favicon.hash:'+str(hash))