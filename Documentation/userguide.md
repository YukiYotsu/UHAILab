# The User Guide
Last modified: *22.02.2025*

## How to start my App  
### How to do setting  
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
#### Cannot use shell?   
The newer Poetry should be maintained by Homebrew. So you cannot use:
```
poetry shell

The command "shell" does not exist.
```  