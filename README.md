# Introduction

Ankiword can be used to add word to Anki. With ankiword, you need just 
provide the word you want add, the description is queried from online
dictionary.

Ankiword is tested on Mac OS X, but it may work on any platform with python 3 
installed.

Most part of this project is stolen from [AnkiEasy](https://github.com/ex860/Ankieasy),
AnkiEasy can be used to add a batch of words to Anki

# Usage

1. Install [anki](https://apps.ankiweb.net/) application and python3
2. Clone this git repo or just download the [zip file](https://github.com/liangguo/ankiword/archive/master.zip)
3. `python3 setup.py install` (`python setup.py install` for Windows user)
4. Modify the config.json (see below for more information)
5. run `python3 ankiword <word>` (`python ankiword` for Windows user) to add words to anki
6. Open anki and check your deck.

# Command Syntax

The syntax of ankiword is 

```
	python3 ankiword [-b <back side of the word> ] [-a <additional contents to the back side of the word>] [-h] <word>
```

## Option description

`-b` or `--back`, optional, specify the back side of the card, if this option is specified, ankiword 
will not lookup online.

`-a` or `--append`, optional, append something to the back of the card. If the card already exist, the 
contents will be appended to the back side

`<word>` is the word you want add to anki


# Config

Config.json is the ankiword configuration profile, it contains following fields.

- deck : Anki deck you want add cards to. 
- collection: A system path indicates to your anki collection (it's different in different OS)
- download_dir: A system path point to your anki media files.
- dict_source: which language/online dictionary you want to use to lookup.
  	- english_yahoo
  	- english_baicizhan
	- english_cambridge
	- japanese
- card_type: anki card type
	- basic
	- basic_reverse
	- japanse_recognition_recall
