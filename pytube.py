import requests
import urllib
import urllib.parse
from urllib.parse import *

url = "https://www.youtube.com/watch?v=P9o8BjRVASg"
title = ""
download_link = ""
video_id = (parse_qs(urlparse(url).query))['v'][0]
get_video_info = requests.get('http://www.youtube.com/get_video_info?&video_id=' + video_id)
video_info = get_video_info.text
info_split = video_info.split('&')
for x in info_split:
    key = x.split('=')[0]
    value = x.split('=')[1]
    if key == 'title':
        title = value.replace('+',' ')
for x in info_split:
    key = x.split('=')[0]
    value = x.split('=')[1]
    if key == 'url_encoded_fmt_stream_map':
        raw_video_info = urllib.parse.unquote(value)
        s_split = raw_video_info.split('&')
        for x in s_split:
            token = x.split('=')[0]
            token_value = x.split('=')[1]
            if token == 'url':
                link = urllib.parse.unquote(urllib.parse.unquote(token_value))
                print("Downloading \"" + title + "\"...")
                open(title+'.mp4', 'wb').write(requests.get(link).content)
                print("Downloading finished.")
                break
