# The User Guide
Last modified: *23.02.2025*

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
You will get a notification and preparation will complete.  

**Move** to the directory named 'GRASP' with ```cd ``` command and **Start** the application with the command:  
```  
poetry run python __main__.py
```  
The new window (my project's App) appears.  
<img width="700" alt="スクリーンショット 2025-02-22 22 41 53" src="https://github.com/user-attachments/assets/f5358c53-0637-4415-83f1-864454e21201" />  

---

## How to use GRASP spell-checker
This application uses excellent UI generated with *customtkinter* so you will be able to know how to use this.  
### Input 
- **Input**: you can **type** yourself in the white box or **open file**. The suitable file extension is `.txt` but **you can open any file**, and there is **no limitation** for the length of the text file and its size.
If you want to try this application, it is the easiest way to open some file in `Data` directory.
<img width="703" alt="スクリーンショット 2025-02-22 22 42 17" src="https://github.com/user-attachments/assets/4b93115a-ff37-47c3-922b-6b172502aae1" />  
 
### Spell-check
- **Spell-check**: after input, you can check misspelled words or undefined words with the **'Check Spelling' button**. As soon as pressed, spell-check will be done and this execution time depends on the size of the file. Please wait a second. **Misspelled words are highlighted with red lines**.  
<img width="1063" alt="スクリーンショット 2025-02-22 22 42 37" src="https://github.com/user-attachments/assets/8e214c94-df17-4220-8d2d-81df82bae212" />  

### Check result
- **Check** result: **misspelled words are highlighted with red lines**. If there is highlighted words, I recommend you to **look at 'Spelling Suggestions' box** below the 'Input Text' box. GRASP will suggest phrases which are corrected along dictionary file and user-defined CSV file there.
<img width="697" alt="スクリーンショット 2025-02-22 22 43 12" src="https://github.com/user-attachments/assets/851451f6-3c10-47a4-bf76-641e90b6865a" />  


### Define whatever you like
- **Define** whatever you like: there might be some mistakes in spelling suggestions. In this case, you can correct by yourself. **After select any word in 'Input Text' box (in usual way: you can select a word with dragging), press 'Define' button**. You will be asked what you want to define as. The defined words are stored at `user_defined.csv` so that you will be no longer notified with those words.
<img width="703" alt="スクリーンショット 2025-02-22 22 43 54" src="https://github.com/user-attachments/assets/e03ed38f-c7d5-4af5-ab21-6c64445257b0" />  

#### you can do dragging
<img width="701" alt="スクリーンショット 2025-02-22 22 44 13" src="https://github.com/user-attachments/assets/e61d6f72-a156-43fd-9fe6-17eeee676bc7" />  

---

## How to implement *coverage* test
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
Name                                                       Stmts   Miss  Cover
------------------------------------------------------------------------------
/Users/takumi/Documents/GitHub/UHAILab/GRASP/__init__.py       0      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/config.py         6      0   100%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/core.py         134      2    99%
/Users/takumi/Documents/GitHub/UHAILab/GRASP/ui.py            80     65    19%
test_prime.py                                                155      0   100%
------------------------------------------------------------------------------
TOTAL                                                        375     67    82%
```  
