# Introduction

Ankiword can be used to add word to Anki deck. With ankiword, you need just 
provide the front side of the card, the back side is the query result in online
dictionary.

Ankiword is tested on Mac OS X, but it may work on any platform with python 3 
installed.

Most part of this project is stolen from [AnkiEasy](https://github.com/ex860/Ankieasy)

# Usage

1. Install [anki](https://apps.ankiweb.net/, or from brew cask) application and python3
2. Clone this git repo or just download the [zip file](https://github.com/liangguo/ankiword/archive/master.zip)
3. python3 setup.py install ("python setup.py install" for Windows user)
4. Modify the config.json (see below for more information)
5. run ** python3 ankiword <word to add> ** ("python ankiword" for Windows user) to add words to anki
6. Open anki and check your deck.

# Command Syntax

The syntax of ankiword is 

```
	python3 ankiword <word to add>
```

** <word to add> ** is the word you want add to anki

# Config

Config.json is the ankiword configuration profile, it contains following fields.

- deck : Anki deck you want add cards to. 
- collection: A system path indicates to your anki collection (it's different in different OS)
- download_dir: A system path point to your anki media files.
- dict_source: what language you want to use to lookup.
  	- english_yahoo
  	- english_baicizhan
	- english_cambridge
	- japanese
- card_type: anki card type
	- basic
	- basic_reverse
	- japanse_recognition_recall
