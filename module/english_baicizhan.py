import urllib.request;
from urllib.parse import quote
from bs4 import BeautifulSoup
import subprocess
import platform
import datetime
import json
import wget

def LookUp(word, data):
    # Eliminate the end of line delimiter
    if word == "":
        return None
    word = word.splitlines()[0]
    wordUrl = urllib.parse.quote(word, safe='')
    url="http://mall.baicizhan.com/ws/search?w={}".format(wordUrl)
    content = urllib.request.urlopen(url)
    webresult = json.load(content)
    result = {}
    front_word = ""
    back_word = ""
    download_dir = ""

    if "word" not in webresult:
        print("No search result")
        return None

    front_word += word + "<br>"
    front_word += webresult.get("accent","") + "<br>"

    if "download_dir" in data:
        download_dir = data['download_dir']
        try:
            wget.download("http://baicizhan.qiniucdn.com/word_audios/{}.mp3".format(wordUrl), out=download_dir+"Py_"+word+".mp3")
        except urllib.error.HTTPError as e:
            print("No sound file found")
        else:
            front_word += "[sound:Py_"+word+".mp3]"

    back_word = webresult["mean_cn"] + "<br>"
    back_word += webresult.get("st","") + "<br>"
    back_word += webresult.get("sttr","")+ "<br>"

    result['front_word'] = front_word
    result['back_word'] = back_word

    return result
