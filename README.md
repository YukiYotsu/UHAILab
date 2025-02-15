# 👋 Moi!
I'm Yuki Yotsumoto. This is the README markdown for the AI Lab course at the University of Helsinki 🇫🇮 in 2025.

*Last modified: 15.02.2025*

## List of used main technique   
<img src="https://skillicons.dev/icons?theme=light&perline=6&i=python,github,vscode"/>  

and https://www.wordfrequency.info/ as the dictionary file [5].  

## How to start my App  
### How to do setting  
The newer Poetry should be maintained by Homebrew. So you cannot use:
```
poetry shell

The command "shell" does not exist.
```  
After **cloning** my repository on your machine, **launch** Poetry at the root directory of the installed project.
To implement this, you have to install Poetry in advance.
Finish the initialization of the project by running the command:  
```
poetry install
```  
When executing the command, you might be led to the following notification:  
```  
Installing the current project: poetry-testi (0.1.0)
The current project could not be installed: [Errno 2] No such file or directory: '~/poetry-testi/README.md'
If you do not want to install the current project use --no-root
```  
This is because Poetry is also trying to install (some) existing projects here. When you want to install only project dependencies, use this:  
```  
poetry install --no-root
```  

---

### How to install *customtkinter* in Poetry?  
My App uses 'CustomTkinter' library which is made based on UI-library 'Tkinter', which helps the project **generate UI**. So execute the command below to use my project (after moving to the root directory):  
`poetry add --dev customtkinter` 

And you will get the notification:
```
Updating dependencies
Resolving dependencies... (0.6s)

Package operations: 3 installs, 0 updates, 0 removals

  - Installing darkdetect (0.8.0)
  - Installing packaging (24.2)
  - Installing customtkinter (5.2.2)

Writing lock file
``` 
This is finally completion of installing. How to use this? It is explained on [the page](https://customtkinter.tomschimansky.com/tutorial/).  
### How to use '*tkinter*' which is a GUI library for my project.  
My application uses 'tkinter' library which help the project generate GUI. So execute the command below to use my project:  
```
brew install python-tk
```
You will get the answer like the following one: 
```
==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
acme.sh                     sdl3
.
.
.
==> Downloading https://ghcr.io/v2/homebrew/core/tcl-t
Already downloaded: /Users/takumi/Library/Caches/Homebrew/downloads/be646597f3d79273593a6a054e9ad1fcc722de45fe4be5464b2a5275f8b7303b--tcl-tk-9.0.1-1.bottle_manifest.json
==> Pouring tcl-tk--9.0.1.arm64_sequoia.bottle.1.tar.g
🍺  /opt/homebrew/Cellar/tcl-tk/9.0.1: 3,150 files, 38MB
==> Installing python-tk@3.13
==> Pouring python-tk@3.13--3.13.1.arm64_sequoia.bottl
🍺  /opt/homebrew/Cellar/python-tk@3.13/3.13.1: 6 files, 160.5KB
==> Running `brew cleanup python-tk@3.13`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```  

**Move** to the directory named 'GRASP' with ```cd ``` command and **Start** the application with the command:  
```  
poetry run python __main__.py
```  
The new window (my project's App) appears.  

---

### Import *jellyfish*  
If you have not installed it, use the commands:  
```
brew install jellyfish
```
After that, in Poetry environment, 
> jellyfish is a library for approximate & phonetic matching of strings.  
```
poetry add --dev jellyfish
```  

### How to implement *coverage*
To update (generate lock file):  
```  
poetry add requests
```  
If you have not installed coverage, use the command:  
```  
poetry add --dev coverage
```  
**Move** to 'tests' directory and **Execute** coverage test:  
```  
poetry run coverage run test_prime.py
```  
And then, you will get the report using:  
```  
poetry run coverage report
```  
For example;  
```  
takumi@takuminoMacBook-Pro tests % poetry run coverage report
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
/Users/takumi/Documents/GitHub/UHAILab/GRASP/__init__.py       0      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/core.py          96      9    91%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/ui.py            58     46    21%
test_prime.py                                                 78      0   100%
------------------------------------------------------------------------------
TOTAL                                                        232     55    76%
```  

## Directory structure  
All the documents are stored in the same directory named "Documentation".  
All the files should not be changed for stable implementing.

UHAILab/  
&emsp;┣━━━━ README.md (this file)  
&emsp;┣━━━━ ver2_vocabulary.csv  
&emsp;┣━┳━━ GRASP/  
&emsp;┃&emsp;┣━━━━ ```__init__.py```  
&emsp;┃&emsp;┣━━━━ core.py  
&emsp;┃&emsp;┣━━━━ ui.py  
&emsp;┃&emsp;┗━━━━ ```__main__.py```  
&emsp;┣━┳━━ Tests/  
&emsp;┃&emsp;┣━━━━ ```__init__.py```  
&emsp;┃&emsp;┗━━━━ test_prime.py    
&emsp;┗━┳━━ Documentation/  
&emsp;&emsp;&emsp;┣━━━━ implementation.md  
&emsp;&emsp;&emsp;┣━━━━ specification.md  
&emsp;&emsp;&emsp;┣━━━━ userguide.md  
&emsp;&emsp;&emsp;┣━━━━ testing_report.md  
&emsp;&emsp;&emsp;┣━━━━ week1report.md  
&emsp;&emsp;&emsp;┣━━━━ week2report.md  
&emsp;&emsp;&emsp;┣━━━━ week3report.md  
&emsp;&emsp;&emsp;┣━━━━ week4report.md  
&emsp;&emsp;&emsp;┣━━━━ week5report.md  
&emsp;&emsp;&emsp;┗━━━━ week6report.md 

## Trouble Shooting
#### What is 'ver2_vocabulary.csv'?  
It is used as the vocabulary to compare target words with rightly-spelled words.    
#### In the case where you want to use shell **mandatorily**.  
I have not tried this, but just in case.  
First, install plugin:  
```
poetry self add poetry-plugin-shell
```
But you might receieve error. If so, the cause should be 'The ```shell``` command was moved to a plugin: ```poetry-plugin-shell```, Poetry official page said [4].  
You can install poetry with *pip* to solve this error, you should not use pip though according to the course page.
> Varoitus: pip
Olet saattanut asentaa Pythonin tarvitsemia riippuvuuksia pip-komennolla. Älä käytä pipiä tällä kurssilla sillä jos teet niin, teet 99.9% todennäköisyydellä jotain väärin.  

~~**Where and What is the function named "connectiontest"?**  
It is used only for confirming the stable connection between files placed at some different folders. "connectiontest" is (or used to be) set in "```__main__.py```".~~  

## Reference
When I make this README file, I refer to shun198's article. Thanks to shun198 [1] [2].  
And I think of the structure of this project, I refer to sari-bee's repository[3] which seems to have been made in the same course.  
I have changed the vocabulary file into *Word frequency Top 5000*'s file to check if words are correctly-spelled. You can get access with the link [5].    

[1] https://qiita.com/shun198/items/c983c713452c041ef787  
[2] https://github.com/shun198  
[3] https://github.com/sari-bee/tieteellinen_laskin?tab=readme-ov-file  
[4] https://python-poetry.org/docs/cli/#script-project  
[5] https://www.wordfrequency.info/  

