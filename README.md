# ico_hash
计算网站特定文件HASH 返回SHODAN搜索语法：http.favicon.hash:-xxxxxxxxxx

python3

import mmh3 
import requests 
import codecs
import sys

使用方法
```
python3 ico_hash.py https://www.xxx.com/favicon.ico
```

