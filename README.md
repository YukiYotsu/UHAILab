# 👋 こんにちは！
私は四元　祐貴です。ヘルシンキ大学🇫🇮の「アルゴリズムとAI研究」のプロジェクト講義で課題となるアプリケーションのマークダウンを示していきます。

*最終更新日: 2025年2月16日*

## 使用技術 
<img src="https://skillicons.dev/icons?theme=light&perline=6&i=python,github,vscode"/>  

そして辞書ファイルとして次のサイト[5]からファイルを提供していただいています。https://www.wordfrequency.info/  

## アプリの立ち上げ方
### 設定の仕方
**クローン**するかもしくは**zipファイルを入手**した後、**Poetryを起動**してください。このために、Poetryを持っていない人はVisual Studio Codeのターミナルを開くなどして（普通のターミナル上でも可能です）Poetryを前もって入手しておく必要があります。
Poetryを準備した場合、もしくはすでにもっているよという人は、次のコマンドを打ってPoetryの初期化を行ってください。
```
poetry install
```  
コマンドを打つ際、次の注意分が出るかもしれません。
```  
Installing the current project: poetry-testi (0.1.0)
The current project could not be installed: [Errno 2] No such file or directory: '~/poetry-testi/README.md'
If you do not want to install the current project use --no-root
```  
これは、すでにPoetryで既存のプロジェクトがあった場合にそれを初期化し直そうとしていることを意味します。もしプロジェクトの依存関係のみインストールしたい場合は次のコマンドを試してください。
```  
poetry install --no-root
```  
詳しくPoetryについて知りたい場合やわからない場合は**Google上で「Poetry　始め方」や「使い方」など検索**することでわかりやすくなるはずです。
---

### Poetryに*customtkinter*をインストールするには？  
私のアプリは*customtkinter*と呼ばれるPython上の優秀なUIライブラリを使用しています。これにより、かっこいい見た目のアプリが出来上がるわけです。プロジェクトのルートディレクトリに移動した後、次のコマンドをターミナル上で打ってください。インストールができます。
`poetry add --dev customtkinter` 
なお、多くのプログラマーにとって普通、コマンドはターミナル上で打ちます。すると通知文として次のような文が出てくるはずです。
```
Updating dependencies
Resolving dependencies... (0.6s)

Package operations: 3 installs, 0 updates, 0 removals

  - Installing darkdetect (0.8.0)
  - Installing packaging (24.2)
  - Installing customtkinter (5.2.2)

Writing lock file
``` 
これでインストールは完了です。どのように使うかに関しては公式HPをご覧ください。'CustomTkinter'は優秀なのでおすすめです。[the page](https://customtkinter.tomschimansky.com/tutorial/).  
### そもそも*tkinter*を持っていない方へ
私のUIには最も一般的なUIライブラリと言える*tkinter*を使っています。次のコマンドを打つことでインストールが可能です。
```
brew install python-tk
```
次のような答えが得られるはずです。通知文の一部は：
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

私のプロジェクトなのであれば、'GRASP'と名付けられたディレクトリまで```cd```コマンドを使って**移動**し、次のコマンドでアプリを**起動**しましょう！ 
```  
poetry run python __main__.py
```  
アプリが新しく立ち上がるはずです。

---

### *jellyfish*をインポートする
*jellyfish*をスペルチェック時使っています。持っていなければ追加で必要です。  
```
brew install jellyfish
```
その後、先述と同じように下のコマンドを打つことでPoetry仮想環境上でもインストールが可能です。
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
全てのドキュメントは'Documentation'ディレクトリ内に整理してあります。これらは講義を進めていく都合上必要な書類にすぎませんが、私のアプリの仕組みを暴くには最適な選択肢でしょう。😱
なお、全てのディレクトリ構造は下のようにしておかなければなりません。**何もいじらなければ下のままになっているはずです**。

UHAILab/  
&emsp;┣━━━━ README.md (this file)  
&emsp;┣━━━━ ver2_vocabulary.csv  
&emsp;┣━┳━━ GRASP/  
&emsp;┃&emsp;┣━━━━ ```__init__.py```  
&emsp;┃&emsp;┣━━━━ core.py  
&emsp;┃&emsp;┣━━━━ ui.py  
&emsp;┃&emsp;┗━━━━ ```__main__.py```  
&emsp;┣━┳━━ Data/  
&emsp;┃&emsp;┣━━━━ text_general.txt   
&emsp;┃&emsp;┣━━━━ text_technical.txt  
&emsp;┃&emsp;┣━━━━ text_slang.txt  
&emsp;┃&emsp;┣━━━━ text_noise.txt 
&emsp;┃&emsp;┣━━━━ correctly_general.txt  
&emsp;┃&emsp;┣━━━━ correctly_technical.txt  
&emsp;┃&emsp;┣━━━━ correctly_slang.txt  
&emsp;┃&emsp;┗━━━━ correctly_noise.txt  
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

## トラブルシューティング
#### 'ver2_vocabulary.csv'とは？
正しくスペルが綴られた語を並べてあるcsvファイルです。
#### shellコマンドは使えませんか？  
新型のPoetryはshellを使わなくなりました（かつて使っていたみたいです）なので使用不可です。
```
poetry shell

The command "shell" does not exist.
```  
#### ‼️PIPは使わないでください
Poetry仮想環境とpipは相性が悪いようです。少なくとも、私のアプリもヘルシンキ大学の講義の教えに倣っておかなければ安定した動作が保証できません。なので、pipは使わないでください。
> Varoitus: pip
Olet saattanut asentaa Pythonin tarvitsemia riippuvuuksia pip-komennolla. Älä käytä pipiä tällä kurssilla sillä jos teet niin, teet 99.9% todennäköisyydellä jotain väärin.   

## 参考文献
READMEマークダウンファイルを設計する際、shun198さんのGitHub[1]　[2]を参考にしました。ありがとうございます。 
本プロジェクトのディレクトリ構成とプロジェクト設計をする際、sari-beeさんのGitHub[3]を参考にしました。   

[1] https://qiita.com/shun198/items/c983c713452c041ef787  
[2] https://github.com/shun198  
[3] https://github.com/sari-bee/tieteellinen_laskin?tab=readme-ov-file  
[4] https://python-poetry.org/docs/cli/#script-project  
[5] https://www.wordfrequency.info/  

